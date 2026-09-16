# The SOC Home Lab Handbook

**Building a Personally-Operated, Isolated Practice Lab — SIEM, Endpoints, Network Monitoring, Honeypots, and Safe Attack Simulation**

📄 **[Download the full PDF](./SOC_Home_Lab_Handbook.pdf)** — 249 pages, ~95,800 words across 22 parts.

Part of the **NESHBOY SOC Professional Library**, alongside [SIGNAL TO ACTION: The Complete SOC Playbook Handbook](https://github.com/neshboy/soc-playbook-handbook), [The Detection Engineering Handbook V2](https://github.com/neshboy/detection-engineering-handbook), and [The SOC Manager's Operating Handbook](https://github.com/neshboy/soc-manager-handbook).

## Safety first — read this before anything else in the book

This is a book about standing up a SIEM, monitored endpoints, network sensors, honeypots, and attack-simulation tooling — several of the components it teaches you to build are, by design, meant to be attacked or to run offensive tooling. The book's one non-negotiable rule, stated in Part 1 and never relaxed afterward:

> You build this lab to attack and defend systems **you own**, on a network segment that cannot reach — and cannot be reached by — anything you don't own. Never point a scanner, an exploit, or an "attack simulation" tool at a system you don't own or don't have explicit authority to test. Intentionally vulnerable practice services (honeypots, deliberately unpatched targets, Atomic Red Team runs) stay on a dedicated, isolated lab network — never bridged to your home production network or the open internet.

Every one of the 22 parts carries a mandatory **Safety Gate** callout — the one recurring feature in this book that is not opportunistic — stating the specific, checkable isolation or ownership control that part's content depends on. Part 4 (network isolation and segmentation architecture) and Appendix A4 (the safety/isolation pre-flight checklist, not yet drafted — see "What's not in this release" below) are where the full mechanics live; every later Safety Gate box points back to a control defined there rather than re-deriving it. If you take one thing from this book before touching a keyboard, it's this: verify isolation before anything intentionally vulnerable goes live, every time, not just the first time.

## What this book is

A practical, hands-on guide to building a personally-operated, safely isolated environment for practicing the skills the other three NESHBOY volumes teach. Those volumes assume telemetry, alerts, and a running SOC already exist; this book is where a reader who has none of that starts — a SIEM to search, Windows and Linux endpoints producing real logs (Sysmon, auditd), a firewall and network segmentation, Zeek and Suricata watching the wire, honeypots generating unsolicited attacker traffic, threat-intelligence feeds enriching what comes in, dashboards worth looking at, and safe, reversible attack-simulation tooling (Atomic Red Team–style) to generate known-cause telemetry on demand. It's a construction manual, not a detection-logic book, a playbook, or a management text — those are the other three volumes' jobs, cross-referenced by name and part number every time a topic brushes up against one.

Content is marked with one of six **content tags**, organized by build phase rather than professional role: `[CONCEPT]`, `[SETUP]`, `[HANDS-ON LAB]`, `[TROUBLESHOOTING]`, `[SAFETY]`, `[COST/RESOURCE]`. A hobbyist and a working SOC analyst building the identical Wazuh install need the same information at the same points — what varies is which build phase a given paragraph belongs to, not who the reader is professionally.

## Part 11: an honest build autopsy, not a fabricated walkthrough

Part 11, "The Windows Domain Lab Problem," exists specifically to hold a gap honestly rather than paper over it. The author attempted a persistent, multi-DC Active Directory forest lab for domain-authentication and Kerberos telemetry practice — and abandoned it: domain controller promotion, GPO-driven Sysmon/audit-policy rollout, and keeping eval licenses alive on a rotating basis demanded more ongoing maintenance than the rest of the author's lab needed, and the build stalled at a half-configured single DC. Part 11 documents that Build Autopsy as a real case study in what a domain lab actually costs, instead of presenting a walkthrough of a lab that was never finished. It closes with a realistic scoped-down alternative (one or two standalone Windows hosts, or a short-lived eval-image domain for a single exercise) rather than a persistent multi-DC forest as a hobbyist default.

## What's real vs. conceptual

This book reuses *The Detection Engineering Handbook V2*'s four-class figure-evidence system verbatim (`STYLE-GUIDE.md` §9) rather than inventing its own — the two books frequently cite the same physical lab and the same evidence files, and a reader flipping between them should see one consistent classification:

- **REAL LAB EXAMPLE** — captured from the author's own real, continuously-operated Proxmox lab (a Pi-hole resolver, a honeynet, and several monitored Linux containers), scrubbed of secrets/PII. This evidence is concentrated where the real lab actually is: mainly the Linux endpoint (Part 9), internal DNS (Part 7), and honeynet (Parts 15, 19) content.
- **CONTROLLED LAB EXAMPLE** — captured in a lab built specifically to generate that evidence.
- **OFFICIAL REFERENCE** — sourced from vendor documentation or another authoritative published source, cited in full.
- **CONCEPTUAL** — an illustrative diagram or architecture sketch with no claim of being captured from a running system. This is the default for anything the author's own lab hasn't built end to end — including every mermaid architecture diagram in the book and most of the SIEM/NSM/threat-intel content, since the author's real lab currently runs no commercial SIEM/EDR product and no live Zeek/Suricata/feed-enrichment pipeline.

The author's real lab is real, running, and Linux/network-only: no Windows host, no Active Directory domain, no cloud tenant. This book says so plainly rather than fabricating REAL LAB EXAMPLE evidence for components that were never built.

## Reading the book

- **[SOC_Home_Lab_Handbook.pdf](./SOC_Home_Lab_Handbook.pdf)** — the assembled, print-ready book (22 parts). Start here.
- **[BOOK-INDEX.md](./BOOK-INDEX.md)** — the full part table with per-unit scope, plus a "Key structural decisions and provenance" section recording which scope/format calls against the sibling volumes were deliberate.
- **[STYLE-GUIDE.md](./STYLE-GUIDE.md)** — the voice, formatting, safety-framing, and figure-evidence contract every part follows: six content tags, eight recurring callouts (Build Autopsy, Lab Note, Engineering Reality, Safety Gate, Resource Reality, Validation Test, Blind Spot, What Would Change My Mind), and the mandatory per-part isolation statement.

## What's not in this release

BOOK-INDEX.md specifies five appendices (A1–A5: network topology templates, hardware cost worksheets, build checklists, the safety/isolation pre-flight checklist, and the cross-series quick reference) as part of this book's full scope. They have not been authored yet — `appendices/` is currently empty — so this release is the 22-part book body only. The build script (`build/build_book.js`) stops at the Part Table for exactly this reason: emitting placeholder pages for content that doesn't exist would misrepresent what's actually in this PDF. Every in-text reference to an appendix (there are several, particularly to Appendix A4 from Safety Gate boxes) is a forward pointer to future work, not a broken link inside this build.

## How it was built

- `build/build_book.js` — parses `BOOK-INDEX.md`'s Part Table, assembles all 22 chapter files into one HTML document (colorizing the six content tags), and prints it to PDF via headless Chrome.
- `build/render_mermaid.py` — renders each chapter's Mermaid diagram source to SVG via `@mermaid-js/mermaid-cli`, inserting the rendered-image reference directly after the source fence without touching figures already linked.
- `build/add_watermark.py` — applies the diagonal `neshboy` watermark to every page.

## Rebuilding it yourself

```
cd build
npm install
node build_book.js
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer ^
  --print-to-pdf="..\_build\SOC_Home_Lab_Handbook.pdf" "..\_build\book.html"
python add_watermark.py
```

## Repository layout

- `chapters/` — the 22 parts, Markdown source of record, each with YAML front matter (`author`, `reviewer`, `status`, `last_validated`, `tested_on`, `depends_on`).
- `appendices/` — reserved for the five appendices specified in `BOOK-INDEX.md`; not yet authored (see "What's not in this release").
- `assets/diagrams/` — rendered Mermaid SVGs (and their `.mmd` sources) for every diagram in the book.
- `build/` — the build/render/watermark tooling above.
- `BOOK-INDEX.md`, `STYLE-GUIDE.md` — cross-cutting project documentation: the canonical part list and the voice/format/safety contract every part follows.
- `REFERENCES.md` — full citations for every `OFFICIAL REFERENCE`-tagged claim or figure, keyed by the bracket ID (e.g. `[COWRIE-REPO]`) named in the citing part's text.
