# Using & Contributing to this Template

## Use it as your own study guide
1. Click **Use this template** on GitHub (or fork / download it).
2. Read [`docs/research/`](docs/research/) to understand the OSP.
3. Work through [`curriculum/`](curriculum/README.md) in order. Keep your work in
   [`student-workspace/`](student-workspace/README.md).
4. Tick topics off in [`CHECKLIST.md`](CHECKLIST.md), or rate yourself in
   [`progress-tracker.csv`](progress-tracker.csv).

## Use it as a teacher
- Each lesson `README.md` is a requirements list with spec references, Performance Outcomes, prior
  Year 1 knowledge, suggested activities and resources.
- Write teaching notes in each lesson folder as `notes.md`, starting from
  [`templates/lesson-template.md`](templates/lesson-template.md).
- Part B of `CHECKLIST.md` tracks which lessons have notes, examples, activities, quizzes and resources.

## Add or change a lesson
The lesson list lives in **[`tools/curriculum_data.py`](tools/curriculum_data.py)**, the single source
of truth.

```bash
# 1. edit tools/curriculum_data.py
# 2. rebuild
python3 tools/build_curriculum.py
```

- New lesson folders and READMEs are created. **Existing READMEs are not overwritten** (use `--force`
  to regenerate them).
- `CHECKLIST.md` and `curriculum/README.md` are always rebuilt. Ticked checkboxes are kept, matched by ID.
- The script lists any resource files a lesson links to that don't exist yet.
- Topic status codes: `K` known from Year 1, `P` partially known, `N` new.

> Topic IDs (`SS.LL.TT`) come from the order of subjects, lessons and topics. Inserting a topic in the
> middle renumbers the ones after it, so add new topics at the end of a lesson where you can.

## Before sharing your copy
- [ ] Empty `student-workspace/` (keep the `.gitkeep` files and READMEs)
- [ ] Untick `CHECKLIST.md` (delete it and re-run the build script) and reset `progress-tracker.csv` (`--force`)
- [ ] Check [`docs/research/sources.md`](docs/research/sources.md) and update it if Pearson has released a newer specification

## Ground rules
- Don't commit Pearson copyrighted papers or mark schemes. Link to them instead.
- Mock briefs and sample data must be original and fictional.
- Keep spec references accurate (`OS x.y` = Occupational Specialism content area x.y; `Core x.y` = Year 1 Core).
