# LAUNCH.md: going live with Kits by Iqbal

Everything is built and tested locally. Nothing has been published, pushed or uploaded. Follow these steps in order. Total time: about 90 minutes.

## What is where

| Path | What it is | Public? |
|---|---|---|
| `index.html`, `css/`, `js/`, `img/`, `preview/`, `sitemap.xml`, `robots.txt` | The storefront for GitHub Pages | Yes |
| `js/store.js` | **The one place for Gumroad links and prices** (`PRODUCTS` at the top) | Yes |
| `dist/local-business-templates-v1.zip` | Product 1, upload to Gumroad | **No, never commit or share** |
| `dist/ai-prompt-pack-india-v1.zip` | Product 2, upload to Gumroad | **No** |
| `dist/website-launch-checklist.pdf` | Free lead magnet, upload to Gumroad | Upload to Gumroad only |
| `products/` | Source files of the paid products (its own private git repo) | **No** |
| `tools/` | Build, screenshot and QA scripts | Yes (harmless) |

`dist/` and `products/` are in `.gitignore`, so pushing this repo does not leak the paid files. To rebuild the zips after editing a product: `python tools/build.py` (add `--shots` to refresh screenshots).

## Step 1: Gumroad account and payouts (15 min)

1. Sign up at gumroad.com with the username **snpwave6**, so your store lives at `https://snpwave6.gumroad.com`.
2. Settings > Payments: connect **PayPal** for payouts. Fill in the tax details Gumroad asks for.
3. Settings > Profile: name "Sheik Iqbal Meera John", short bio, link to https://iqbalmeerajohn.github.io/portfolio/ .
4. Check the current fee on Gumroad's pricing page before setting prices, so you know your take-home per sale.
5. Currency: if Gumroad lets you price in INR, use the rupee prices below. If not, use the dollar prices and change `price` / `priceNote` in `js/store.js` to match exactly what Gumroad charges.

## Step 2: Create the three products

For each product: Gumroad dashboard > Products > New product > Digital product. Set the **URL slug exactly as written** so the links already in `js/store.js` work without edits.

---

### Product 1: Local Business Website Template Pack

- **Name:** Local Business Website Template Pack
- **URL slug:** `local-biz-templates` → `https://snpwave6.gumroad.com/l/local-biz-templates`
- **Price:** ₹499 (or $9)
- **File to upload (Content tab):** `dist/local-business-templates-v1.zip`
- **Cover images:** `img/tpl-dental-clinic-1440.webp`, `img/tpl-beauty-salon-1440.webp`, `img/tpl-hair-studio-1440.webp`, `img/tpl-fitness-studio-1440.webp`, `img/tpl-strength-gym-1440.webp` (convert to PNG/JPG first if Gumroad rejects WebP; any free image converter works). Thumbnail: `img/og.jpg`.
- **Summary line (the short "You'll get" text):** 5 one-page website templates, a step-by-step README and a licence for unlimited client sites.
- **Description (paste as is):**

```
Five complete, mobile-first websites for local businesses. Change your name, phone, WhatsApp, address, opening hours and brand colours in ONE clearly marked block at the top of the file, and the whole page updates.

Try every template live before you buy: https://iqbalmeerajohn.github.io/kits/#templates

WHAT'S INSIDE
- Dental clinic: treatment cards and a WhatsApp appointment form
- Beauty parlour: tap services, pick a time, WhatsApp opens with the booking message
- Hair studio: price menu with stylist levels, team section, light and dark mode
- Fitness studio: weekly timetable drawn from your hours, membership plans
- Strength gym: bold dark design with a live clock of today's sessions

EVERY TEMPLATE INCLUDES
- A live "Open now · until 9 PM" badge that reads your hours in your time zone
- An automatic weekly hours table with today highlighted
- Tap-to-call, WhatsApp and Google Maps buttons wired to your details
- A demo switch so test clicks never reach a real number until you go live
- Smooth scroll animations that switch off for visitors who prefer reduced motion
- No frameworks or build tools: one HTML file plus a photos folder

ALSO INCLUDED
- README with field-by-field instructions and free hosting guides (Netlify Drop and GitHub Pages)
- LICENCE: use for your own business or unlimited client websites, including paid work. Reselling the templates themselves is not allowed.
- All photos are CC0 from StockSnap.io, free for commercial use

The sample businesses, reviews and contact details in the demos are fictional. Replace them with real details before publishing.

7-day refund: if it isn't right for you, email me within 7 days for a full refund.

Need it set up or customised? I build full websites from ₹8,000: https://iqbalmeerajohn.github.io/portfolio/
```

- **Tags:** website template, html template, small business, local business, india, salon, gym, dental, whatsapp

---

### Product 2: Small Business AI Marketing Prompt Pack: India Edition

- **Name:** Small Business AI Marketing Prompt Pack: India Edition
- **URL slug:** `ai-prompt-pack-india` → `https://snpwave6.gumroad.com/l/ai-prompt-pack-india`
- **Price:** ₹199 (or $5)
- **File to upload:** `dist/ai-prompt-pack-india-v1.zip` (31-page PDF + plain-text .md copy + read-me)
- **Cover image:** take a screenshot of the PDF cover page (open the PDF inside the zip), or use `img/og.jpg`.
- **Summary line:** 126 copy-and-paste AI prompts for Indian small businesses, PDF plus plain text.
- **Description (paste as is):**

```
126 ready-to-use prompts for ChatGPT, Gemini, Claude or any AI chat tool, written for Indian shops, clinics, salons, gyms, restaurants, tutors and service businesses. Copy a prompt, fill in the [BRACKETS] with your details, paste, and get a post you can actually use.

WHAT'S COVERED
- Google Business Profile posts, offers, Q&A and descriptions (12 prompts)
- WhatsApp broadcasts, auto-replies, reminders and quick replies (14)
- Instagram and Facebook captions, reel scripts and content plans (14)
- Festival and seasonal offers: Diwali, Sankranti, Ugadi, Ramzan and Eid, Christmas, Navratri, Onam, wedding season and more (16)
- Review requests and replies, including negative and fake reviews (12)
- Menus, service lists and product descriptions (10)
- Website and directory listing copy (8)
- Flyers, banners, ads and SMS (8)
- Customer service and daily operations (8)
- Telugu and Hindi: translations, Tenglish and Hinglish captions, pamphlets (10)
- Quick packs for restaurants, salons, clinics, gyms, kirana stores, tutors, boutiques and pharmacies (14)

ALSO INSIDE
- A "business profile" starter prompt that makes every other prompt more accurate
- Example outputs for 8 prompts, including Telugu and Hindi
- A pre-posting checklist so you never publish a wrong price or a claim you can't back up

Formats: a clean 31-page PDF to read or print, plus a plain-text copy for fast copy and paste.

Licence: use in your own business and for clients you serve. Please don't resell or share the files.

7-day refund: if it isn't useful, email me within 7 days for a full refund.
```

- **Tags:** ai prompts, chatgpt prompts, small business marketing, india, whatsapp marketing, instagram, google business profile

---

### Product 3 (free): Website Launch Checklist for Small Businesses

- **Name:** Website Launch Checklist for Small Businesses
- **URL slug:** `website-launch-checklist` → `https://snpwave6.gumroad.com/l/website-launch-checklist`
- **Price:** ₹0+ / $0+ with "Let customers pay what they want" switched on (suggested price 0). Buyers enter their email to get it, which builds your Gumroad audience list.
- **File to upload:** `dist/website-launch-checklist.pdf`
- **Cover image:** `img/checklist.webp` (convert to PNG if needed).
- **Description (paste as is):**

```
A one-page, printable checklist with 40 checks to run before you share your website link. Works for any shop, clinic, salon, gym, restaurant or service business, whoever built the site.

Five sections: your details are correct, content that earns trust, works on every phone, found on Google, and launch and keep it alive.

Free. Pay what you want if you find it useful.

Want a website that passes every check? Templates: https://iqbalmeerajohn.github.io/kits/  Custom builds from ₹8,000: https://iqbalmeerajohn.github.io/portfolio/
```

- After publishing, turn on Gumroad's "Send a receipt / follow-up" email in the product's Workflow or Emails area (if available on your plan) with a short thank-you and links to the two paid kits.

### Refund policy text (Gumroad > Settings > Refund policy)

```
7-day refund policy. If a product isn't right for you, email iqbalmeerajohn1@gmail.com or reply to your receipt within 7 days of purchase and you'll get a full refund.
```

## Step 3: Check the links in the storefront (2 min)

Open `js/store.js`. The `PRODUCTS` block at the top already contains:

```js
templates: { url: "https://snpwave6.gumroad.com/l/local-biz-templates", price: "₹499", ... }
prompts:   { url: "https://snpwave6.gumroad.com/l/ai-prompt-pack-india", price: "₹199", ... }
checklist: { url: "https://snpwave6.gumroad.com/l/website-launch-checklist", price: "Free", ... }
```

If your Gumroad product URLs or prices differ, edit them here and nowhere else. Every buy button and price on the page updates from this block.

## Step 4: Publish the storefront on GitHub Pages (10 min)

1. On github.com (account Iqbalmeerajohn) create a new **public** repository named exactly `kits`. Do not add a README.
2. In this folder run:
   ```
   git remote add origin https://github.com/Iqbalmeerajohn/kits.git
   git push -u origin main
   ```
   Before pushing, run `git status` and confirm `dist/` and `products/` are NOT listed (they are ignored).
3. Repository Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`. Save.
4. After a minute the store is live at https://iqbalmeerajohn.github.io/kits/ . Open it on your phone, click every buy button and one live demo.
5. Optional: add the store to Google Search Console and submit `https://iqbalmeerajohn.github.io/kits/sitemap.xml`.
6. Add the store link to your portfolio, GitHub profile README, LinkedIn "Featured" section and Gumroad profile.

The product sources in `products/` are a separate local git repo. If you want an off-machine backup, push it to a **private** GitHub repository only.

## Step 5: Promote it (free channels, post manually)

House rules for every post: no fake testimonials, no invented sales numbers, no countdowns or "only today" pressure. Say plainly that it is a paid product you made. Reply to every comment within a day.

### 1. Reddit: r/webdev (Showoff Saturday)

r/webdev only allows showing off your own projects on **Saturdays**, using the "Showoff Saturday" flair. Read the sidebar rules on the day you post in case they have changed. Lead with what is interesting technically; the store link goes last. Do not cross-post the same text to many subreddits.

**Title:** `[Showoff Saturday] 5 single-file local business templates with a live "open now" badge driven by one config object`

**Body:**
```
I build websites for small businesses in Visakhapatnam, India, and kept rewriting the same things: opening hours, "open now", WhatsApp booking, tap-to-call. So I turned five of my designs into templates where everything business-specific lives in one window.SITE object at the top of the file.

Some details that might interest this sub:
- Hours are an array of sessions per day (["09:00","13:00"], ["15:30","21:00"]). The "Open now · until 9 PM / Closed · opens 10 AM tomorrow" text, the weekly table and a 24h clock on one template are all derived from it using Intl.DateTimeFormat with the configured time zone, so it is correct for visitors in other time zones.
- A demoMode flag intercepts tel: and wa.me clicks and shows what would happen, so demo clicks never reach a real phone.
- No build step: one HTML file + an img folder each. GSAP for motion, fully disabled under prefers-reduced-motion.
- Tested headless at 1440 and 390 for zero console errors and no horizontal scroll.

Live demos (fictional businesses): https://iqbalmeerajohn.github.io/kits/#templates

The pack is paid (₹499 / about $9) because I'm trying to fund my freelancing, but I'm happy to answer questions about any of the implementation, and feedback on the designs is very welcome.
```

### 2. LinkedIn post

```
I just launched my first digital products.

Over the past months I've been designing websites for local businesses in Vizag: clinics, salons, gyms. The same requests came up every time: show if we're open right now, let customers book on WhatsApp, make calling one tap.

So I packaged five of those designs as rebrandable templates. You change the name, phone, WhatsApp, address, hours and colours in one block at the top of the file and the whole site updates, including a live "Open now" badge.

Alongside it:
→ 126 AI marketing prompts for Indian small businesses (Google Business posts, WhatsApp broadcasts, festival offers, review replies, Telugu and Hindi versions)
→ A free one-page Website Launch Checklist

Live demos and details: https://iqbalmeerajohn.github.io/kits/

If you run a small business, or you're a freelancer who builds sites for them, I'd love your honest feedback. And if you'd rather have it done for you, I build full websites from ₹8,000.

#webdevelopment #smallbusiness #india #freelancing #ai
```

### 3. Twitter / X thread

```
1/ I turned 5 of my local business website designs into templates you can rebrand in one sitting. Live demos 👇
https://iqbalmeerajohn.github.io/kits/

2/ Everything business-specific sits in one config block: name, phone, WhatsApp, address, hours, colours. Change it, refresh, done.

3/ The hours drive a live "Open now · until 9 PM" badge, the weekly table and (on the gym one) a 24-hour clock. Time zone aware via Intl.DateTimeFormat.

4/ The salon template has a WhatsApp booking picker: tap services, pick a time, WhatsApp opens with the message written for you.

5/ No frameworks, no build step. One HTML file + photos. Host free on Netlify or GitHub Pages; the README walks through it.

6/ Also made: 126 AI marketing prompts for Indian small businesses (festival offers, review replies, Telugu + Hindi), and a free website launch checklist.

7/ Templates ₹499, prompts ₹199, checklist free. Built in Vizag. Feedback very welcome, replies are open.
```

### 4. Indie Hackers (post in the main feed or "Show IH")

**Title:** `Launched my first products: website templates + AI prompts for Indian local businesses`

```
Hi IH, I'm Iqbal, a web and AI developer in Visakhapatnam, India.

What I made:
- Local Business Website Template Pack (₹499 / ~$9): 5 single-file templates for clinics, salons and gyms with live opening hours and WhatsApp booking
- AI Marketing Prompt Pack, India Edition (₹199 / ~$5): 126 prompts for Google Business posts, WhatsApp broadcasts, festival offers and Telugu/Hindi copy
- A free one-page launch checklist as a lead magnet

Why: local businesses here mostly run on WhatsApp and Google Maps. They need a fast, simple site that answers "are you open?" and "how do I book?", not a 10-page CMS. The templates came from real pitch work.

Stack and costs: static HTML on GitHub Pages, Gumroad for checkout. Total spend so far: ₹0.

What I'd love feedback on:
1. Is the pricing right for an Indian audience vs. global?
2. Which channel would you test first for selling to freelancers who build sites for small businesses?

Store with live demos: https://iqbalmeerajohn.github.io/kits/

I'll share honest numbers here after the first month, whatever they are.
```

### 5. Product Hunt-style listing (Product Hunt, or similar directories such as Peerlist, Uneed or Microlaunch)

- **Name:** Kits by Iqbal
- **Tagline (max 60 chars):** `Rebrandable websites + AI prompts for local businesses`
- **Topics:** Website Builder, Templates, Marketing, Artificial Intelligence
- **Description (max 260 chars):**
```
Five single-file website templates for clinics, salons and gyms with a live "Open now" badge, WhatsApp booking and one config block for all your details. Plus 126 AI marketing prompts for Indian small businesses and a free launch checklist.
```
- **Gallery:** `img/og.jpg`, then the five `img/tpl-*-1440.webp` screenshots (convert to PNG) and two `img/tpl-*-390.webp` phone shots.
- **Maker's first comment:**
```
Hi everyone! I design websites for local businesses in Visakhapatnam, India. Every client asked for the same three things: show whether we're open right now, let people book on WhatsApp, and make calling one tap. These templates do all three, driven by a single settings block, with no frameworks or build step.

The demos use fictional businesses so you can click around freely (calls and WhatsApp are in demo mode). I'd really value feedback on which business type I should add next.
```

## After launch: first 30 days

- Week 1: post channels 2, 3 and 5. Saturday: Reddit. Share the free checklist in local business WhatsApp groups only where you are a member and it is allowed.
- Reply to every comment and Gumroad message within 24 hours. Note every question; the answers become FAQ entries and new prompts.
- Day 30: write the honest Indie Hackers follow-up with real numbers.
- Never add testimonials until real buyers give permission to quote them.
