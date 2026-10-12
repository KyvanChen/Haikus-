# Haikus 🌱

A tiny daily dose of motivation: a haiku or a confidence-boosting message,
picked at random every day and posted right here by a GitHub Action.

<!-- MESSAGE:START -->
**Haiku of the day**

> Storm clouds pass and fade
> the sun was always still there
> so is your own strength
<!-- MESSAGE:END -->

---

## How it works

- All the messages live in [`messages.json`](messages.json) — each one is
  either a `haiku` or a `confidence` message.
- Every day, [`.github/workflows/daily-message.yml`](.github/workflows/daily-message.yml)
  runs [`scripts/daily_message.py`](scripts/daily_message.py), which picks one
  at random and rewrites the block above.
- Want to add more? Open `messages.json` and append a new
  `{"type": "haiku" | "confidence", "text": "..."}` entry, then open a PR.

## One-time setup

For the daily commit to work, this repo's Actions need write permission:

**Settings → Actions → General → Workflow permissions → "Read and write permissions"**, then save.

You can also trigger it manually any time from the **Actions** tab by running
the "Daily Motivation" workflow with "Run workflow."
