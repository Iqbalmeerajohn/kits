/* SITEKIT:BEGIN  Template engine. You do not need to edit anything in this block. */
(function () {
  var S = window.SITE || {};
  var DAYS = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
  var NAMES = { sun: "Sunday", mon: "Monday", tue: "Tuesday", wed: "Wednesday", thu: "Thursday", fri: "Friday", sat: "Saturday" };
  var ORDER = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function toMin(t) { var p = String(t).split(":"); return (+p[0]) * 60 + (+(p[1] || 0)); }
  function fmt(m) { m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mm = m % 60; return ((h + 11) % 12 + 1) + (mm ? ":" + String(mm).padStart(2, "0") : "") + " " + (h >= 12 ? "PM" : "AM"); }
  function slots(d) { return ((S.hours || {})[d] || []).map(function (s) { return [toMin(s[0]), toMin(s[1])]; }); }
  function now() {
    var p = new Intl.DateTimeFormat("en-US", { timeZone: S.timezone || "Asia/Kolkata", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
    var g = function (t) { return p.find(function (x) { return x.type === t; }).value; };
    var key = g("weekday").slice(0, 3).toLowerCase();
    return { day: DAYS.indexOf(key), key: key, min: (+g("hour") % 24) * 60 + (+g("minute")) };
  }
  function status() {
    var n = now(), t = slots(n.key);
    var cur = t.find(function (s) { return n.min >= s[0] && n.min < s[1]; });
    if (cur) return { open: true, until: cur[1], text: "Open now · until " + fmt(cur[1]) };
    var later = t.find(function (s) { return n.min < s[0]; });
    if (later) return { open: false, next: later[0], text: "Closed now · opens " + fmt(later[0]) + " today" };
    for (var k = 1; k <= 7; k++) {
      var d = DAYS[(n.day + k) % 7], ts = slots(d);
      if (ts.length) return { open: false, next: ts[0][0], text: "Closed now · opens " + (k === 1 ? "tomorrow" : NAMES[d]) + " " + fmt(ts[0][0]) };
    }
    return { open: false, text: "Closed" };
  }
  function dayLabel(d, sep) { var t = slots(d); return t.length ? t.map(function (s) { return fmt(s[0]) + " - " + fmt(s[1]); }).join(sep || ", ") : "Closed"; }

  /* Small toast used in demo mode and for form messages */
  var toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.setAttribute("role", "status");
      toastEl.style.cssText = "position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:9999;max-width:min(560px,calc(100% - 32px));width:max-content;background:#161616;color:#f5f5f3;font:500 14px/1.5 system-ui,sans-serif;padding:12px 16px;border-radius:12px;box-shadow:0 18px 40px -16px rgba(0,0,0,.5);opacity:0;transition:opacity .2s ease;pointer-events:none;text-align:center";
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg; toastEl.style.opacity = "1";
    clearTimeout(toastTimer); toastTimer = setTimeout(function () { toastEl.style.opacity = "0"; }, 5200);
  }
  function waLink(msg) { return "https://wa.me/" + String(S.whatsapp || "").replace(/\D/g, "") + "?text=" + encodeURIComponent(msg || S.whatsappMessage || ""); }
  function openWhatsApp(msg) {
    if (S.demoMode) { toast("Demo mode: on the live site this opens WhatsApp to " + S.phoneDisplay + " with: “" + (msg || S.whatsappMessage) + "”"); return; }
    window.open(waLink(msg), "_blank", "noopener");
  }

  /* Fill in text and links from SITE */
  document.querySelectorAll("[data-site]").forEach(function (el) {
    var v = S[el.getAttribute("data-site")]; if (v == null) return;
    el.innerHTML = Array.isArray(v) ? v.map(esc).join(el.getAttribute("data-join") || "<br>") : esc(v);
  });
  document.querySelectorAll("[data-tel]").forEach(function (el) {
    el.href = "tel:" + S.phone;
    el.addEventListener("click", function (e) { if (S.demoMode) { e.preventDefault(); toast("Demo mode: on the live site this calls " + S.phoneDisplay + "."); } });
  });
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var msg = el.getAttribute("data-wa") || S.whatsappMessage;
    if (el.tagName === "A") { el.href = waLink(msg); el.target = "_blank"; el.rel = "noopener"; }
    el.addEventListener("click", function (e) { e.preventDefault(); openWhatsApp(msg); });
  });
  document.querySelectorAll("[data-maps]").forEach(function (el) { el.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(S.mapsQuery || S.name); el.target = "_blank"; el.rel = "noopener"; });
  document.querySelectorAll("[data-email]").forEach(function (el) { el.href = "mailto:" + S.email + (el.getAttribute("data-email") ? "?subject=" + encodeURIComponent(el.getAttribute("data-email")) : ""); });
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  window.SiteKit = { S: S, DAYS: DAYS, NAMES: NAMES, ORDER: ORDER, fmt: fmt, toMin: toMin, slots: slots, now: now, status: status, dayLabel: dayLabel, toast: toast, waLink: waLink, openWhatsApp: openWhatsApp, esc: esc };
})();
/* SITEKIT:END */
