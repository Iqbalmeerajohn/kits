/* =====================================================================
   PRODUCTS: the ONLY place to edit Gumroad links and prices.
   After you create each product on Gumroad, paste its URL here.
   Every buy button and price on the page updates automatically.
   ===================================================================== */
const PRODUCTS = {
  templates: {
    url: "https://snpwave6.gumroad.com/l/local-biz-templates",
    price: "₹499",
    priceNote: "one-time · about $9"
  },
  prompts: {
    url: "https://snpwave6.gumroad.com/l/ai-prompt-pack-india",
    price: "₹199",
    priceNote: "one-time · about $5"
  },
  checklist: {
    url: "https://snpwave6.gumroad.com/l/website-launch-checklist",
    price: "Free",
    priceNote: "pay what you want"
  }
};

/* ---------- page behaviour (no need to edit below) ---------- */
document.documentElement.classList.add("js");

document.querySelectorAll("[data-buy]").forEach(a => {
  const p = PRODUCTS[a.dataset.buy]; if (!p) return;
  a.href = p.url;
});
document.querySelectorAll("[data-price]").forEach(el => {
  const p = PRODUCTS[el.dataset.price]; if (p) el.textContent = p.price;
});
document.querySelectorAll("[data-price-note]").forEach(el => {
  const p = PRODUCTS[el.dataset.priceNote]; if (p) el.textContent = p.priceNote;
});

/* template viewer tabs (arrow keys supported) */
const tabs = [...document.querySelectorAll(".tab")];
function select(tab, focus) {
  tabs.forEach(t => {
    const on = t === tab;
    t.setAttribute("aria-selected", String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute("aria-controls")).classList.toggle("on", on);
  });
  if (focus) tab.focus();
}
tabs.forEach((t, i) => {
  t.addEventListener("click", () => select(t));
  t.addEventListener("keydown", e => {
    const d = e.key === "ArrowDown" || e.key === "ArrowRight" ? 1 : e.key === "ArrowUp" || e.key === "ArrowLeft" ? -1 : 0;
    if (d) { e.preventDefault(); select(tabs[(i + d + tabs.length) % tabs.length], true); }
  });
});

/* reveal on scroll */
const io = "IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches
  ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -8% 0px" })
  : null;
document.querySelectorAll(".rv").forEach(el => io ? io.observe(el) : el.classList.add("in"));

document.querySelectorAll("[data-year]").forEach(el => el.textContent = new Date().getFullYear());
