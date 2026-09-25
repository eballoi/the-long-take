# The Long Take

A pixel-art scroll-film of my career. Scroll, and a jetpack version of me flies through seven worlds, levelling up from software testing and data warehouses to full-stack engineering, solo consulting and AI.

**Live:** https://eballoi.github.io/the-long-take/

## The seven worlds

1. **It started with a test** · Soundtracker, 2013–2014
2. **A warehouse from zero** · Payleven → SumUp, 2015
3. **Going live** · Tiscali / Streamago, 2015–2017
4. **Inside the giant** · Docler Holding, 2017–2019
5. **Building our own** · Longwave Studio, founded 2019
6. **Solo mode** · independent consultant, startups to enterprises
7. **The AI turn** · today

## How it's built

- One static `index.html`: no build step, no framework, no dependencies to install.
- **Three.js** (r128, loaded from cdnjs) renders the 3D worlds at low resolution and upscales them with `image-rendering: pixelated`, so the whole scene reads as pixel art.
- Scroll position drives a single continuous camera move (the "long take"), the story cards, the year counter and an RPG layer: level, XP, world unlocks and achievements.
- The character and every prop are hand-authored pixel maps drawn on a 2D canvas.
- Falls back to a plain, readable page when WebGL is unavailable or reduced motion is enabled.

## Run it locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Security & privacy

- No backend, forms, cookies, tracking or analytics.
- Three.js is pinned with Subresource Integrity, so an altered copy on the CDN would be refused.
- A strict Content-Security-Policy only allows the page's own inline script (pinned by hash), that exact Three.js file and Google Fonts, and blocks every network request after load.
- The contact email is assembled at runtime, so it never appears as plain text in the HTML.

After editing the inline script, refresh its CSP hash:

```bash
python3 tools/update-csp.py
```

## Contact

Edoardo Balloi · Italy · remote · edoardo.balloi [at] gmail [dot] com · [LinkedIn](https://www.linkedin.com/in/edoardo-balloi/)
