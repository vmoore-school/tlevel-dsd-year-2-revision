// Front end for the starter project: talks to the Flask JSON API with fetch().
"use strict";

const API_BASE = "/api";

const sessionList = document.getElementById("session-list");
const sessionSelect = document.getElementById("session-id");
const form = document.getElementById("booking-form");
const message = document.getElementById("message");

function formatDate(isoString) {
  return new Date(isoString.replace(" ", "T")).toLocaleString("en-GB", {
    weekday: "short", day: "numeric", month: "short", hour: "2-digit", minute: "2-digit",
  });
}

function formatPrice(gbp) {
  return new Intl.NumberFormat("en-GB", { style: "currency", currency: "GBP" }).format(gbp);
}

function showMessage(text, type) {
  message.textContent = text;
  message.className = `message ${type}`;
}

// Build the DOM with textContent (not innerHTML) so data from the API can't inject HTML (XSS).
function renderSession(session) {
  const item = document.createElement("li");
  item.className = session.spaces_left === 0 ? "session-card full" : "session-card";

  const title = document.createElement("h3");
  title.textContent = session.name;

  const details = document.createElement("p");
  details.textContent = `${formatDate(session.start)} · ${session.duration_minutes} mins · ` +
    `${formatPrice(session.price_gbp)} · Coach: ${session.coach}`;

  const spaces = document.createElement("p");
  spaces.textContent = session.spaces_left === 0 ? "Full" : `${session.spaces_left} spaces left`;

  item.append(title, details, spaces);
  return item;
}

async function loadSessions() {
  try {
    const response = await fetch(`${API_BASE}/sessions`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();

    sessionList.replaceChildren(...data.sessions.map(renderSession));
    sessionSelect.replaceChildren(...data.sessions.map((s) => {
      const option = document.createElement("option");
      option.value = s.session_id;
      option.textContent = `${s.name} (${formatDate(s.start)})`;
      option.disabled = s.spaces_left === 0;
      return option;
    }));
  } catch (error) {
    showMessage("Sorry, sessions could not be loaded. Please try again later.", "error");
    console.error(error);
  }
}

// Client-side validation gives quick feedback; the server validates again because clients can't be trusted.
function validate(memberId) {
  if (!/^\d+$/.test(memberId) || Number(memberId) < 1) {
    return "Enter your member number (a whole number, 1 or more).";
  }
  return null;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const memberId = form.member_id.value.trim();
  const problem = validate(memberId);
  if (problem) {
    showMessage(problem, "error");
    form.member_id.focus();
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/bookings`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ member_id: Number(memberId), session_id: Number(form.session_id.value) }),
    });
    const data = await response.json();
    if (response.ok) {
      showMessage(`Booked! Your booking number is ${data.booking_id}.`, "success");
      form.reset();
      loadSessions();
    } else {
      showMessage(data.error, "error");
    }
  } catch (error) {
    showMessage("Something went wrong. Please try again.", "error");
    console.error(error);
  }
});

loadSessions();
