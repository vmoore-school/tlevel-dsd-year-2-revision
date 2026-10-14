#!/usr/bin/env python3
"""Build the curriculum scaffold and checklists from tools/curriculum_data.py.

Usage:
    python3 tools/build_curriculum.py           # create missing files, rebuild CHECKLIST.md
    python3 tools/build_curriculum.py --force   # also overwrite lesson/subject READMEs

What it writes:
    curriculum/README.md                     index of subjects and lessons (always rebuilt)
    curriculum/<subject>/README.md           subject overview (created if missing)
    curriculum/<subject>/<lesson>/README.md  lesson requirements (created if missing)
    curriculum/<subject>/<lesson>/resources/ resource folder
    CHECKLIST.md                             master checklist (rebuilt; ticked boxes are kept)
    progress-tracker.csv                     spreadsheet version (created if missing)

Edit curriculum_data.py to add or change lessons, then re-run.
"""
import csv
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curriculum_data import SUBJECTS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM = os.path.join(ROOT, "curriculum")
FORCE = "--force" in sys.argv

ICON = {"K": "✅", "P": "🟨", "N": "🟥"}
LABEL = {"K": "Known (Y1) - revise", "P": "Partial - extend", "N": "New - teach"}

BUILD_STEPS = ["Teaching notes", "Worked examples", "Practice activities",
               "Quiz / retrieval questions", "Resources complete", "Checked against spec"]


def topic_id(si, li, ti):
    return f"{si:02d}.{li:02d}.{ti:02d}"


def lesson_id(si, li):
    return f"{si:02d}.{li:02d}"


def rel(path_from_root, start_dir):
    return os.path.relpath(os.path.join(ROOT, path_from_root), start_dir).replace(os.sep, "/")


def write(path, text, overwrite):
    if os.path.exists(path) and not overwrite:
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True


def counts(topics):
    c = Counter(s for s, _ in topics)
    return " · ".join(f"{ICON[k]} {c[k]}" for k in "KPN" if c[k])


def lesson_readme(si, li, subject, lesson, lesson_dir):
    lid = lesson_id(si, li)
    out = [f"# {lid} {lesson['title']}", "",
           f"> **Subject:** {subject['title']}  ",
           f"> **Spec reference:** {lesson['spec']}  ",
           f"> **Performance Outcomes:** {lesson['pos']}  ",
           f"> **Used in OSP:** {lesson['tasks']}  ",
           f"> **Topic status:** {counts(lesson['topics'])}", "",
           "Key: ✅ known from Year 1 (revise only) · 🟨 partially known (extend) · 🟥 new (teach from scratch)", "",
           "## Assumed prior knowledge (Year 1)", ""]
    out += [f"- {p}" for p in lesson["prior"]]
    out += ["", "## What must be taught", "", "| ID | Status | Requirement |", "|---|---|---|"]
    for ti, (status, text) in enumerate(lesson["topics"], 1):
        out.append(f"| {topic_id(si, li, ti)} | {ICON[status]} | {text} |")
    out += ["", "## Suggested activities", ""]
    out += [f"- {a}" for a in lesson["activities"]]
    out += ["", "## Resources", ""]
    if lesson["resources"]:
        for r in lesson["resources"]:
            out.append(f"- [{os.path.basename(r)}]({rel(r, lesson_dir)})")
    else:
        out.append("- _None yet - add files to `resources/`._")
    if lesson["terms"]:
        out += ["", "## Key terms", "", ", ".join(f"**{t}**" for t in lesson["terms"])]
    out += ["", "## Lesson build status", "",
            "_For whoever is writing this lesson. Tick these off in [CHECKLIST.md](" + rel("CHECKLIST.md", lesson_dir) + ")._", ""]
    out += [f"- {s}" for s in BUILD_STEPS]
    out += ["", "## Teaching notes", "", "_To be written. Cover each requirement above; link worked examples and activities in `resources/`._", ""]
    return "\n".join(out)


def subject_readme(si, subject, subject_dir):
    out = [f"# {si:02d} {subject['title']}", "", subject["intro"], "",
           "| Lesson | Spec | POs | Status |", "|---|---|---|---|"]
    for li, lesson in enumerate(subject["lessons"], 1):
        out.append(f"| [{lesson_id(si, li)} {lesson['title']}]({lesson['folder']}/README.md) | {lesson['spec']} | {lesson['pos']} | {counts(lesson['topics'])} |")
    out.append("")
    return "\n".join(out)


def read_ticks(path):
    """Return the IDs whose checkbox is ticked in an existing CHECKLIST.md."""
    ticked = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*- \[[xX]\] .*?`([0-9.]+(?::[a-z]+)?)`", line)
                if m:
                    ticked.add(m.group(1))
    return ticked


def build_checklist(ticked):
    total = Counter()
    for subject in SUBJECTS:
        for lesson in subject["lessons"]:
            total.update(s for s, _ in lesson["topics"])
    n = sum(total.values())

    out = ["# Year 2 Master Checklist", "",
           "What a student already knows from Year 1, what has to be extended, and what must be taught from scratch,",
           "for the T Level Technical Qualification in Digital Software Development (Pearson 610/5801/4),",
           "Occupational Specialism (Year 2).", "",
           "> This file is generated by `tools/build_curriculum.py`. Ticked boxes are kept when it is rebuilt.",
           "> To add a topic, edit `tools/curriculum_data.py` and re-run the script.", "",
           "## Key", "",
           "| Icon | Meaning | What to do |", "|---|---|---|",
           "| ✅ | Known from Year 1 Core | Quick revision, then apply it in the OSP context |",
           "| 🟨 | Partially known | Year 1 introduced the idea; Year 2 needs more depth or practical use |",
           "| 🟥 | New | Not in the Year 1 Core; must be taught from scratch |", "",
           "## Summary", "",
           "| Status | Topics | Share |", "|---|---|---|"]
    for k in "KPN":
        out.append(f"| {ICON[k]} {LABEL[k]} | {total[k]} | {round(100 * total[k] / n)}% |")
    out.append(f"| **Total** | **{n}** | |")
    out += ["", "| Subject | ✅ | 🟨 | 🟥 | Lessons |", "|---|---|---|---|---|"]
    for si, subject in enumerate(SUBJECTS):
        c = Counter(s for l in subject["lessons"] for s, _ in l["topics"])
        out.append(f"| [{si:02d} {subject['title']}](curriculum/{subject['folder']}/README.md) | {c['K']} | {c['P']} | {c['N']} | {len(subject['lessons'])} |")

    out += ["", "---", "", "## Part A: Topic checklist", "",
            "Tick a topic once it has been **taught/learned and practised**. IDs match the lesson READMEs.", ""]
    for si, subject in enumerate(SUBJECTS):
        out += [f"### {si:02d} {subject['title']}", ""]
        for li, lesson in enumerate(subject["lessons"], 1):
            lid = lesson_id(si, li)
            link = f"curriculum/{subject['folder']}/{lesson['folder']}/README.md"
            out += [f"**[{lid} {lesson['title']}]({link})** ({lesson['spec']})", ""]
            for ti, (status, text) in enumerate(lesson["topics"], 1):
                tid = topic_id(si, li, ti)
                box = "x" if tid in ticked else " "
                out.append(f"- [{box}] {ICON[status]} `{tid}` {text}")
            out.append("")

    out += ["---", "", "## Part B: Lesson build tracker", "",
            "For people building the study guide: tick each step when the lesson material exists.", ""]
    step_keys = ["notes", "examples", "activities", "quiz", "resources", "checked"]
    for si, subject in enumerate(SUBJECTS):
        out += [f"### {si:02d} {subject['title']}", ""]
        for li, lesson in enumerate(subject["lessons"], 1):
            lid = lesson_id(si, li)
            out.append(f"- **{lid} {lesson['title']}**")
            for key, label in zip(step_keys, BUILD_STEPS):
                bid = f"{lid}:{key}"
                box = "x" if bid in ticked else " "
                out.append(f"  - [{box}] `{bid}` {label}")
        out.append("")
    return "\n".join(out)


def build_tracker_csv(path):
    if os.path.exists(path) and not FORCE:
        return False
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "subject", "lesson", "spec_ref", "performance_outcomes", "osp_tasks",
                    "y1_status", "requirement", "confidence_1to5", "taught", "practised", "revised", "notes"])
        for si, subject in enumerate(SUBJECTS):
            for li, lesson in enumerate(subject["lessons"], 1):
                for ti, (status, text) in enumerate(lesson["topics"], 1):
                    w.writerow([topic_id(si, li, ti), subject["title"], lesson["title"], lesson["spec"],
                                lesson["pos"], lesson["tasks"], LABEL[status], text, "", "", "", "", ""])
    return True


def build_index():
    out = ["# Curriculum", "",
           "Everything to be taught in Year 2, organised by subject. Each lesson folder has a `README.md` listing",
           "its requirements, and a `resources/` folder for lesson-specific files.", "",
           "Subjects follow the Occupational Specialism content areas of the specification, plus an assessment-skills",
           "subject (00) and the industry placement (09).", ""]
    for si, subject in enumerate(SUBJECTS):
        out += [f"## [{si:02d} {subject['title']}]({subject['folder']}/README.md)", "", subject["intro"], ""]
        for li, lesson in enumerate(subject["lessons"], 1):
            out.append(f"- [{lesson_id(si, li)} {lesson['title']}]({subject['folder']}/{lesson['folder']}/README.md) - {counts(lesson['topics'])}")
        out.append("")
    return "\n".join(out)


def main():
    created, missing = [], []
    for si, subject in enumerate(SUBJECTS):
        sdir = os.path.join(CURRICULUM, subject["folder"])
        if write(os.path.join(sdir, "README.md"), subject_readme(si, subject, sdir), FORCE):
            created.append(os.path.relpath(os.path.join(sdir, "README.md"), ROOT))
        for li, lesson in enumerate(subject["lessons"], 1):
            ldir = os.path.join(sdir, lesson["folder"])
            res = os.path.join(ldir, "resources")
            os.makedirs(res, exist_ok=True)
            if not os.listdir(res):
                open(os.path.join(res, ".gitkeep"), "w").close()
            if write(os.path.join(ldir, "README.md"), lesson_readme(si, li, subject, lesson, ldir), FORCE):
                created.append(os.path.relpath(os.path.join(ldir, "README.md"), ROOT))
            missing += [r for r in lesson["resources"] if not os.path.exists(os.path.join(ROOT, r))]

    write(os.path.join(CURRICULUM, "README.md"), build_index(), True)
    checklist = os.path.join(ROOT, "CHECKLIST.md")
    write(checklist, build_checklist(read_ticks(checklist)), True)
    build_tracker_csv(os.path.join(ROOT, "progress-tracker.csv"))

    print(f"Created/overwritten {len(created)} README files; rebuilt CHECKLIST.md and curriculum/README.md")
    if missing:
        print("Resources referenced but not found:")
        for m in sorted(set(missing)):
            print("  " + m)


if __name__ == "__main__":
    main()
