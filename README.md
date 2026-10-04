<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/header-light.svg">
  <img alt="RWX — open-source contributor: Python, mobile, embedded" src="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/header-dark.svg" width="100%">
</picture>

<kbd>Python</kbd> <kbd>FastAPI</kbd> <kbd>Flutter</kbd> <kbd>Kotlin</kbd> <kbd>C · Zephyr</kbd> <kbd>Linux</kbd> <kbd>pytest</kbd>

</div>

I fix bugs and ship features in open-source projects, mostly across the stack of
[**BasedHardware/omi**](https://github.com/BasedHardware/omi): Python backend services, the
Flutter app, Android, and the wearable's firmware. I like small, well-tested changes that are easy
for maintainers to review.

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/activity-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/activity-light.svg">
  <img alt="Upstream activity: merged and open pull requests by project" src="https://raw.githubusercontent.com/TheRWX/TheRWX/main/assets/activity-dark.svg" width="100%">
</picture>

<sub>Refreshed daily from the GitHub API by <a href=".github/workflows/activity.yml">a workflow in this repo</a> ·
<a href="https://github.com/pulls?q=is%3Apr+author%3ATheRWX+repo%3ABasedHardware%2Fomi+repo%3ABerriAI%2Flitellm">see every PR</a></sub>

</div>

## Selected work

| | Contribution | What it involved |
|:-:|:--|:--|
| 🔐 | **GitHub app security** · [#15012](https://github.com/BasedHardware/omi/pull/15012), [#13912](https://github.com/BasedHardware/omi/pull/13912) | Shared-secret auth on chat-tool routes; stable client errors and escaped OAuth HTML |
| 🧩 | **Integration hardening** · [Slack](https://github.com/BasedHardware/omi/pull/14693), [Microsoft 365](https://github.com/BasedHardware/omi/pull/14250), [Notion](https://github.com/BasedHardware/omi/pull/14258), [Zapier](https://github.com/BasedHardware/omi/pull/14256), [ClickUp](https://github.com/BasedHardware/omi/pull/14268), [notifications](https://github.com/BasedHardware/omi/pull/14260) | Timeouts, null guards, safe error handling, and a cooldown memory leak fix |
| ⏱️ | **Conversation duration fix** · [#18619](https://github.com/BasedHardware/omi/pull/18619) | Durations computed from the transcript's speech span instead of the session offset |
| 🌍 | **11 CLI quickstart translations** | Bulgarian, Estonian, Irish, Basque, Galician, Maltese, Welsh, Bosnian, Mongolian, Belarusian, Tajik |

<details>
<summary><b>In review</b> — open pull requests</summary>
<br>

| PR | Area | Summary |
|:--|:--|:--|
| [#17854](https://github.com/BasedHardware/omi/pull/17854) | Backend + app | Import audio files to create conversations |
| [#17825](https://github.com/BasedHardware/omi/pull/17825) | App (Android) | Sync health watchdog with stall alerts |
| [#17656](https://github.com/BasedHardware/omi/pull/17656) | App | Automatic offline batch uploads when the network returns |
| [#17544](https://github.com/BasedHardware/omi/pull/17544) | Android (Kotlin) | Home-screen widget for device battery and mic state |
| [#19327](https://github.com/BasedHardware/omi/pull/19327) | Firmware (C) | Keep the SD read cursor safe across BLE disconnects |

</details>

<details>
<summary><b>All merged pull requests</b> (20)</summary>
<br>

**Fixes** —
[#13912](https://github.com/BasedHardware/omi/pull/13912) ·
[#14250](https://github.com/BasedHardware/omi/pull/14250) ·
[#14256](https://github.com/BasedHardware/omi/pull/14256) ·
[#14258](https://github.com/BasedHardware/omi/pull/14258) ·
[#14260](https://github.com/BasedHardware/omi/pull/14260) ·
[#14268](https://github.com/BasedHardware/omi/pull/14268) ·
[#14693](https://github.com/BasedHardware/omi/pull/14693) ·
[#15012](https://github.com/BasedHardware/omi/pull/15012) ·
[#18619](https://github.com/BasedHardware/omi/pull/18619)

**Docs** —
[#13717](https://github.com/BasedHardware/omi/pull/13717) ·
[#13729](https://github.com/BasedHardware/omi/pull/13729) ·
[#13740](https://github.com/BasedHardware/omi/pull/13740) ·
[#13742](https://github.com/BasedHardware/omi/pull/13742) ·
[#13752](https://github.com/BasedHardware/omi/pull/13752) ·
[#13754](https://github.com/BasedHardware/omi/pull/13754) ·
[#13756](https://github.com/BasedHardware/omi/pull/13756) ·
[#13758](https://github.com/BasedHardware/omi/pull/13758) ·
[#13773](https://github.com/BasedHardware/omi/pull/13773) ·
[#14236](https://github.com/BasedHardware/omi/pull/14236) ·
[#14238](https://github.com/BasedHardware/omi/pull/14238)

</details>

## Toolbox

| Area | Tools |
|:--|:--|
| **Backend** | Python · FastAPI · Pydantic · SQLite · REST & webhooks · OAuth |
| **Mobile & embedded** | Flutter / Dart · Kotlin (Android) · C on Zephyr (nRF) · BLE |
| **Ops & testing** | Linux · systemd · Docker · Google Cloud · pytest · hermetic tests |

## How I work

- **Reproduce first.** Every fix starts with a failing test on the unpatched code.
- **Small diffs.** Change only what the issue needs, so reviews stay quick.
- **Leave it verifiable.** Tests, notes, and evidence a maintainer can check in minutes.

<details>
<summary><b>Side projects</b></summary>
<br>

- **Discord community bot** — music player with live audio telemetry, DJ leaderboard and title roles, running 24/7 on a small cloud VM.
- **Self-hosted review app** — FastAPI app that helps local businesses invite customer reviews, with owner login and a fair (no-gating) review flow.
- **YouTube voice control** — hands-free browser extension to seek, skip and rewind videos.
- **HSA calculator** — tracks health savings account contribution limits.

</details>

<div align="center">
<br>

[![GitHub](https://img.shields.io/badge/GitHub-@TheRWX-111?style=flat-square&logo=github)](https://github.com/TheRWX)
![Timezone](https://img.shields.io/badge/US-Mountain_Time-b3122e?style=flat-square)

<sub>Open to open-source collaboration — reach me through issues or pull requests.</sub>

</div>
