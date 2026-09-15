# The SOC Home Lab Handbook — STYLE-GUIDE.md

**Status:** Final, adopted before any unit is authored or reviewed.
**Applies to:** every part, appendix, checklist, and diagram in this book.
**Audience:** every writer, technical reviewer, and editor working on this book.

## Why this document exists

This guide adapts the contract proven by *The Detection Engineering Handbook V2*'s `STYLE-GUIDE.md` for a different audience and a different risk profile. That guide was written to fix drift across 55 independently-authored units with no shared contract; this book starts from that lesson rather than re-learning it, and reuses what transfers directly (voice discipline, the eight-slot callout structure, the four-class evidence system, the Mermaid-rendering requirement) while changing what genuinely needs to change for a hands-on build audience: the six content tags (organized by build phase, not professional role — see `BOOK-INDEX.md` provenance item 1), the eight callout names and bodies (re-purposed for build content — provenance item 2), and one new mandatory rule this book's companions don't have: **every part carries an explicit, specific network-isolation and ownership statement.** This is not a style preference. A book that teaches a reader to stand up honeypots, run attack-simulation tooling, and build intentionally vulnerable services carries real risk of misuse or accidental harm if a part ships without stating, concretely, what must be isolated before its content is followed. **"Must"** means a PR gets rejected if it doesn't comply. **"Should"** means deviate only with a reason recorded in the PR description. **"Avoid"** is a strong default a reviewer can override with justification, recorded as a documented guide change, not silent drift.

This guide governs prose voice, Markdown conventions, the eight recurring callout boxes, content-level tags, the evidence-classification system for figures, and the safety-framing mandate. It does not cover technical review standards for whether a build step is actually correct on the tool version it claims to target — that is a separate concern for a separate reviewer, per the production model in `BOOK-INDEX.md`, because voice/format consistency and technical/build correctness are different failure modes.

---

## 1. Voice and Tone

### 1.1 The core rule

Write like a competent lab operator walking a friend through a build over their shoulder — not like a vendor quick-start guide trying to make an install look effortless, and not like a security-marketing post trying to make a honeypot sound edgy. The reader already knows why detection telemetry matters; they came here to build the thing that produces it. Every sentence should survive the question: **what does this actually tell me to install, configure, check, or avoid?** If it doesn't, cut it.

Concretely:

- **State the step, then the reason.** Don't build up to an instruction with scene-setting about how important logging is.
- **Name the failure mode; don't gesture at it.** "This breaks if the vSwitch isn't in promiscuous mode" beats "network visibility can be affected by switch configuration."
- **Prefer the concrete number over the vague qualifier.** "Wazuh's indexer alone wants 4GB of heap; budget 8GB total for the VM before adding endpoints" beats "the SIEM requires a significant amount of memory."
- **Name the tool, the file, the setting, the command** — not the adjective. Say what to do, not that it matters.
- **Prefer active voice with a named actor** ("the hypervisor," "Sysmon," "the reader," "pfSense") over passive constructions that hide who does what. Passive is acceptable only when the actor genuinely doesn't matter ("the packet is dropped at the firewall").
- **Commit to a claim.** If something is untested by the author, say so explicitly ("this Suricata rule set is the vendor default, not validated against this book's own lab traffic — expect to tune it") rather than hedging with vague qualifiers.
- Second person ("you") is fine for procedural instructions; first person plural ("we") is fine for the book's own reasoning. Neither should be used to manufacture urgency or as a substitute for a real subject in an explanatory sentence.
- It is okay to say a step is tedious, fiddly, or genuinely not worth doing by hand. Not every tool needs to sound like the right choice for every reader.

### 1.2 Banned filler — and the actual rule behind the ban

The patterns below are banned **only in their AI-marketing-filler usage** — as a load-bearing transition, hedge, or intensifier that could be deleted with no loss of meaning. Mechanically grepping-and-blocking normal English is explicitly wrong: several of these words have legitimate, specific uses that are fine to keep. **The reviewer's test: does this phrase carry information, or does it just sound like it does?** If a reviewer can delete the phrase and the sentence loses nothing, it's filler — cut it. Do not add a global regex ban to a CI check for this reason: it will both miss the actual pattern and false-positive on legitimate uses.

| Banned pattern (as filler) | Why it's banned | Legitimate exception |
|---|---|---|
| "in today's rapidly evolving threat landscape" | Says nothing; not this book's register at all | None — always cut |
| "it is crucial / critical / important that you..." | Asserts importance instead of demonstrating the concrete consequence | Rewrite as the concrete failure if the step is skipped ("skip this and Sysmon silently fails to load its config, producing zero events with no error") |
| "robust" (attached to abstract nouns: "robust setup," "robust posture") | Vague virtue word | Fine describing a specific measurable property: "robust to a host reboot — the service is enabled, not just started" |
| "leveraging" | Nearly always means "using" | Keep only if something is literally used as leverage in a specific mechanical sense (rare) |
| "seamlessly" | Unfalsifiable marketing adjective, especially common in vendor install docs this book must not imitate | Cut; if setup friction matters (it usually does), describe the actual friction |
| "holistic" | Vague scope-inflation word | Cut; say what specific components are actually being combined |
| "delve into" | AI-pattern verb-of-choice for "discuss/examine" | Use "look at," "cover," "walk through," "install" |
| "in conclusion" / "to summarize" as a section opener | Signposting the reader doesn't need | None in body prose |
| "it is important to note that..." | Hedge that adds no information | Cut the phrase, keep the note only if something remains |
| "unlock / empower / elevate / supercharge" as verbs for a tool enabling a capability | Marketing verbs, not build-manual verbs | Use the literal verb: "lets you query," "forwards events to," "reduces the disk this eats by..." |
| "at the end of the day" | Filler transition | Cut |
| "game-changer / game-changing / cutting-edge / best-in-class / enterprise-grade" | Unfalsifiable superlative, especially tempting when describing a free tool doing something a paid product also does | Cut, or state the measurable difference |
| "just" / "simply" before an instruction ("simply configure the VLAN...") | Minimizes real setup friction and reads as condescending when the step in fact isn't simple | Cut; if a step genuinely is one line, show the line and let its brevity speak for itself |

A phrase is **not** banned just because it contains one of these words. Two tests:

- "Verifying the vSwitch is genuinely isolated is important because a single bridged NIC silently defeats every other control in this chapter" — `important` is load-bearing and explained. Keep it.
- "This Zeek deployment is robust to the sensor host rebooting mid-capture — the service restarts and resumes writing new log rotations without operator intervention" — a specific, falsifiable claim, not the stock phrase. Keep it.

### 1.3 Worked GOOD vs. BAD examples

**Example 1 — opening a setup section**

> BAD: "In order to build a robust, enterprise-grade SOC home lab, it is crucial to seamlessly integrate a SIEM platform into your environment."

> GOOD: "Wazuh's indexer component alone wants 4GB of heap at idle. On an 8GB VM with two Windows endpoints forwarding Sysmon, expect the box to be fully committed with no headroom for anything else — this is the point where Part 3's resource tiers stop being a suggestion and start being a hard constraint."

**Example 2 — describing a limitation**

> BAD: "It is important to note that honeypot deployments may present certain security challenges when leveraging network segmentation."

> GOOD: "A honeypot that shares a switch with anything you care about is not a honeypot — it's an open door with a webcam pointed at it. If the VLAN plan from Part 4 isn't verified (Appendix A4), don't power this on."

**Example 3 — closing a section**

> BAD: "In conclusion, a holistic, seamless approach to lab network isolation will empower you to elevate your security practice."

> GOOD: "None of the honeypot correlation logic in this part matters if the isolation upstream of it fails. Run the pre-flight checklist in Appendix A4 every time you add a new decoy service, not just the first time you build the segment."

**Example 4 — a hedge that should just be a claim**

> BAD: "It is crucial to note that Sysmon configuration is paramount to the quality of the telemetry your lab produces."

> GOOD: "A default Sysmon install with no config file logs almost nothing useful — process creation with a thin field set, no filtering logic. Deploy a real config (Appendix A3's baseline) before you generate a single test event, or your first three exercises will teach you the tool is disappointing when the actual problem is you never configured it."

**Example 5 — false confidence vs. honest uncertainty**

> BAD: "This chapter provides a complete, production-grade walkthrough of building a Windows Active Directory lab."

> GOOD: "This chapter does not walk through building a persistent multi-DC Active Directory forest, because the author tried and abandoned that build — see the Build Autopsy in §3. What follows is a standalone, non-domain-joined Windows host, which covers Sysmon and Windows Event Log telemetry but not domain-authentication or GPO-driven detection content."

### 1.4 Sentence and paragraph mechanics

- Default to active voice; passive only when the actor genuinely doesn't matter.
- One instruction per sentence in `[SETUP]` and `[HANDS-ON LAB]` content. A sentence combining "install the package, then edit the config, then restart the service" should be three sentences or a numbered list, not one comma-chained one.
- One idea per paragraph. A paragraph introducing a tool, then its resource cost, then a troubleshooting note, then a safety caveat should be four short paragraphs or callouts, not one block.
- Numbers: use digits for port numbers, Event IDs, MITRE IDs, version numbers, and any count ≥ 10; spell out one through nine in prose ("three VLANs," not "3 VLANs") — except in tables, where digits are always used for scanability, and except for counts paired with a unit or identifier (8GB of RAM, a 5-minute timeout, VLAN 30), which always use digits regardless of size.
- Contractions ("doesn't," "isn't," "won't") are fine and preferred — this book has a spoken-voice register, not a legal-document register.
- Every numbered install/config procedure that has more than three steps must be a numbered Markdown list, not prose — a reader following along at a keyboard should never have to re-read a paragraph to find step 4.

---

## 2. Heading Level Conventions

| Level | Use for | Example |
|---|---|---|
| `#` (H1) | Part title only. One per file, first line of the file. | `# Part 9 — Linux Endpoints and auditd Deployment` |
| `##` (H2) | Major numbered sections within a part (the part's own table-of-contents entries). Number sequentially: `## 1. Title`, `## 2. Title`. | `## 3. Writing an auditd rule set` |
| `###` (H3) | Subsections within a major section — a specific install step, a specific config file, a specific exercise. Number as `### 3.2 Title` under `## 3`, never restarted as an independent `### 1`. | `### 3.2 Watching /etc/shadow and /etc/passwd` |
| `####` (H4) | Rare; only for structured sub-breakdowns inside a long H3 that need their own anchor ("Prerequisites," "Verification," "Common errors" inside one build walkthrough, when those aren't rendered as callout boxes). Do not nest deeper than H4. | `#### Verification` |

Rules:

- **Callout boxes are never headings** (see §6) — they are blockquotes opened with a bold label, at the same nesting level as the paragraph they annotate.
- Never skip a level (no H2 directly to H4).
- Every part must open with an unnumbered `## Why this part exists` section before numbering starts at `## 1.` — mandatory for all 22 parts.
- Immediately after `## Why this part exists`, every part must carry its mandatory Safety Gate box (see §6.4) before any `## 1.` setup content begins — a reader must see the isolation requirement before the first instruction that needs it.
- Every H2 and H3 must be unique within its file — needed for stable anchor links from the index and cross-references.
- Section titles are sentence case, not Title Case ("Writing an auditd rule set," not "Writing An Auditd Rule Set"). Part titles use title case with an em dash, matching the convention already baked into the part list (`# Part 9 — Linux Endpoints and auditd Deployment`).

---

## 3. Code Block Conventions

Every fenced code block **must** carry an explicit language tag — an untagged fence, or a tag for a language that isn't the one actually shown, is a lint failure.

| Content | Fence tag | Notes |
|---|---|---|
| Bash / shell commands (install steps, `auditctl` invocations, `systemctl` commands) | `` ```bash `` | Pick the tag matching the actual shell — never a generic `shell`. |
| PowerShell | `` ```powershell `` | Never `ps1` as the fence tag. |
| Windows `cmd`/batch | `` ```cmd `` | Only when a command genuinely requires `cmd` and doesn't work in PowerShell. |
| Sysmon configuration XML | `` ```xml `` | Sysmon config is XML, not YAML — do not mistag it. |
| Wazuh/OSSEC `ossec.conf` | `` ```xml `` | Also XML. |
| YAML configs (Filebeat, Elasticsearch, Suricata `suricata.yaml`, Graylog inputs) | `` ```yaml `` | |
| auditd `.rules` file contents (as a static file, not a live command) | `` ```text `` | The syntax is simple enough that no renderer's highlighting adds value, and a truncated/annotated excerpt should never be mistaken for something meant to be parsed as another language. |
| Suricata/Snort rules | `` ```suricata `` (fall back to `` ```text `` if the renderer lacks a Suricata mode) | |
| Zeek scripts (`.zeek` files) | `` ```zeek `` if the renderer supports it, otherwise `` ```text `` | Never mislabel as `bro` (deprecated project name) or a generic scripting-language tag. |
| Firewall rule syntax (pfSense/OPNsense CLI, `nft`/`iptables`) | `` ```bash `` | Pick the tag matching how the rule is actually entered; GUI-driven pfSense rules are shown as a table (§8), not a code block, since there's no literal syntax to paste. |
| Raw log excerpts, event XML/JSON not meant to be executed | `` ```json ``, `` ```xml ``, or `` ```text `` | Use `json`/`xml` only if it's actually valid; a truncated/annotated excerpt with ellipses or inline comments should be `text`. |
| Mermaid diagram source | `` ```mermaid `` | See §9 — the fenced source stays in the file as the editable source of truth alongside its rendered image reference, never deleted once rendered. |
| Conceptual/illustrative content (invented hostnames, teaching-only config not meant to be copy-pasted as-is) | Same tag as normal, **plus** a one-line label immediately above the fence: `CONCEPTUAL SAMPLE — <one clause on what's illustrative about it>` | Reserve for teaching snippets embedded in prose; never label a real, build-tested config this way. |

Additional rules:

- Every code block that is a real installation or configuration step must be preceded by one sentence stating what OS/tool version it targets and followed by one sentence stating what to check to confirm it worked, or a pointer to the Validation Test box that does — a bare wall of config with no framing is grounds for reviewer rejection.
- Inline code (single backtick) is for filenames, single settings, command names, and field names used mid-sentence — e.g., `` `/etc/audit/rules.d/audit.rules` ``, `` `EnableScriptBlockLogging` `` — never a substitute for a fenced block when showing more than one line.
- Comments inside config/code blocks explain *why*, not restate the syntax: `# excluded — this path is rewritten on every package update and floods the log`, not `# this is a watch rule`.

---

## 4. Windows Event ID and Telemetry Identifier Notation

This book reuses Detection Engineering Handbook V2's Event ID rule exactly, and extends it to the other identifier systems a lab-building book actually needs (auditd keys, Zeek notice types, Suricata SIDs) so a reader verifying a build step knows precisely what to look for.

- **Windows/Sysmon Event IDs:** "Event ID 4624 (An account was successfully logged on)" on true first use in the chapter, bare `4624` after. Sysmon IDs always disambiguate on first use per chapter: "Sysmon Event ID 1 (Process Create)," never bare "Event ID 1." Never "Event 4624" (drop "ID"), never "EID 4624."
- **auditd keys and record types:** introduce a key on first use with its purpose stated inline — "the `identity` key (`-k identity`), tagging any write to `/etc/passwd` or `/etc/shadow`" — then bare `` `identity` `` after. Record types (`SYSCALL`, `EXECVE`, `PATH`) are always inline-coded, never bare prose words, since they are literal field values a reader will grep for.
- **Zeek log fields and notice types:** first use states the log file and field together — "`conn.log`'s `duration` field" — then bare field name after within the same section. `Notice::Type` values (e.g., `` `SSL::Invalid_Server_Cert` ``) are always inline-coded.
- **Suricata rule identifiers:** a rule's `sid` is always inline-coded and always paired with its rule message on first reference: "`sid:2100498`, 'GPL ATTACK_RESPONSE id check returned root'."
- **MITRE ATT&CK IDs:** identical rule to Detection Engineering Handbook V2 (see §5) — used in this book only where a part cites what technique a piece of attack-simulation content or honeypot capture maps to, never invented.
- Tables use the bare identifier only, in every system above — no exceptions.
- Ranges follow the same convention throughout: "Event IDs 4624 and 4625" for a pair, "Event IDs 4728–4733" for a true contiguous range (en dash).

---

## 5. MITRE ATT&CK ID Formatting

Reused verbatim from Detection Engineering Handbook V2 for series consistency — this book uses MITRE IDs sparingly (mainly in Parts 15, 18, and 19, where a honeypot capture or a simulated technique needs a precise tag) but when it does, the format must match the rest of the series exactly.

- **First reference in a section:** technique ID + name — `T1595 (Active Scanning)`.
- **Subsequent references in the same section:** bare ID is fine — `T1595`.
- Always uppercase `T`, no space between `T` and the digits, sub-technique separated by a period: `T1550.002`, never `T1550-002` or `T1550.2`.
- Tactic references use the `TA` prefix the same way: `TA0043 (Reconnaissance)` on first use.
- Never invent or guess an ID. If a honeypot capture or simulated action doesn't map cleanly to a technique, say so in prose rather than forcing a tenuous tag — this book is teaching a reader to build evidence, and false MITRE coverage on that evidence is worse than an honest gap.

---

## 6. Callout Boxes — Exact Templates

All eight use the same base shape as the rest of the series: a **blockquote** (`>`) opened with a bold label line, visually and structurally consistent with each other and distinguished only by label text and internal sub-structure. They sit inline in the flow of a section — never a separate jump-target, never nested one inside another.

**General template:**

```
> **[Label — optional short qualifier]**
> Body text, 1–5 sentences. Can include inline code and a short code block if needed.
```

If a box needs more than ~5 sentences, it isn't a callout — promote it to a real `###`/`####` subsection with prose.

### 6.1 Build Autopsy

Dissects a real or realistic lab build that shipped broken: the plan, why it seemed reasonable, how it failed, what replaced it. Adapted from Detection Engineering Handbook V2's Detection Autopsy — same shape, applied to infrastructure instead of a detection rule.

```
> **Build Autopsy — "<the build in one clause>"**
>
> **The plan:** <what was actually attempted, plain description>.
>
> **Why it seemed reasonable:** <the logic that made this look like the right approach>.
>
> **How it failed:** <the specific mechanism, with a concrete trigger or symptom>.
>
> **The fix:** <what the corrected approach adds or changes — or, honestly, that no fix was completed and the build was abandoned>.
```

Worked example:

```
> **Build Autopsy — the abandoned Windows/AD forensics lab**
>
> **The plan:** Stand up a persistent two-DC Active Directory forest with several domain-joined
> Windows endpoints, generating realistic AD authentication and Kerberos telemetry for detection
> practice.
>
> **Why it seemed reasonable:** A domain lab is the natural next step after standalone Windows
> hosts, and eval-licensed Server ISOs make the software cost zero.
>
> **How it failed:** DC promotion, GPO-driven Sysmon/audit-policy rollout, and keeping two eval
> licenses alive on a rotating basis turned out to demand a level of ongoing maintenance the
> author's other running lab components (honeynet, vulnerability scanner) didn't need — the build
> stalled at a half-configured single DC and was never finished.
>
> **The fix:** No fix was completed. This book teaches standalone, non-domain-joined Windows
> hosts (Part 10) and documents the domain build's real cost honestly (Part 11) instead of
> presenting a walkthrough of a lab that doesn't exist.
```

### 6.2 Lab Note

A tactical, practitioner-voice aside — a tip, a shortcut, or a "this is what actually gets you unstuck" observation. Shorter and more informal than the other boxes, but still no filler.

```
> **Lab Note**
> The tip or shortcut, stated as something you'd actually say out loud to someone building this
> next to you.
```

Worked example:

```
> **Lab Note**
> Snapshot the VM immediately after a clean install and before touching any config file. Every
> Sysmon/auditd config mistake in this book is a five-minute revert from that snapshot instead of
> a twenty-minute reinstall — take the snapshot before you're tempted to skip it "just this once."
```

### 6.3 Engineering Reality

A grounded statement about what actually happens when you run the tool, as opposed to what the documentation implies.

```
> **Engineering Reality**
> The gap between documented/expected behavior and what you'll actually hit running this on real
> hardware, stated as a fact, plus the practical consequence.
```

Worked example:

```
> **Engineering Reality**
> Zeek's documentation describes `conn.log` as capturing every connection; in practice, a sensor
> placed on a mirrored port that drops packets under load (common on consumer-grade switches)
> silently produces `conn.log` entries with `missed_bytes` populated and no error anywhere else.
> If your lab's Zeek logs look thin, check `missed_bytes` before assuming the attack simply
> didn't generate traffic.
```

### 6.4 Safety Gate

**Mandatory in every part — the one callout in this book that is not opportunistic.** States the specific network-isolation, containment, or ownership boundary this part's content depends on, and what to verify before proceeding. Never a generic "be careful" — it must name the actual control.

```
> **Safety Gate**
> The specific isolation/ownership control this part's content depends on, stated as a concrete,
> checkable condition — not a general caution. What to verify before proceeding, and where the
> full procedure lives if it's not repeated here (usually Part 4 or Appendix A4).
```

Worked example:

```
> **Safety Gate**
> Everything in this part assumes the honeynet segment built in Part 4 has zero route back to
> your home network or any host holding real credentials, and that its only internet-facing path
> is inbound-only on the specific ports the decoy services listen on. Before deploying a single
> decoy, run the Appendix A4 pre-flight checklist and confirm it end to end — a honeypot is built
> to be attacked; if isolation fails here, it will be attacked successfully and the blast radius
> is whatever that segment can reach.
```

A part's Safety Gate may be short (one control, already fully specified in an earlier part, with a pointer) or expanded (Parts 15 and 18 carry an expanded version with a repeated pre-flight step, per `BOOK-INDEX.md` provenance items 3 and 9) — but it may never be absent, and it may never be reduced to a single sentence with no checkable condition in it.

### 6.5 Resource Reality

Names the specific CPU/RAM/disk/cost this component actually consumes, and what breaks below that.

```
> **Resource Reality**
> The concrete resource or dollar cost, stated as a number. What happens specifically when the
> reader is below it — not just "performance may suffer."
```

Worked example:

```
> **Resource Reality**
> Wazuh's indexer wants 4GB of JVM heap at idle, and the manager process itself adds another
> 1–2GB under load. On a 4GB VM, the indexer either fails to start or gets OOM-killed within
> minutes of the first real ingest burst — this isn't a "runs slowly" failure, it's a "doesn't run
> at all" failure. Budget 8GB minimum for the SIEM VM alone, before adding endpoints.
```

### 6.6 Validation Test

A concrete, reproducible step confirming a build step actually worked, plus the expected observable result.

```
> **Validation Test**
> **Setup:** lab prerequisites, one line.
> **Action:** `the exact command or action to take`
> **Expected result:** what should appear, specifically — a log entry, a dashboard panel, a
> field value.
```

Worked example:

```
> **Validation Test**
> **Setup:** Sysmon installed with the Appendix A3 baseline config, forwarding to the Part 8
> SIEM.
> **Action:** `powershell -Command "Start-Process notepad.exe"` on the Windows endpoint.
> **Expected result:** A Sysmon Event ID 1 (Process Create) entry in the SIEM within seconds,
> with `Image` = `C:\Windows\System32\notepad.exe` and a populated `ParentImage` field pointing to
> the PowerShell process that launched it.
```

### 6.7 Blind Spot

A specific, named gap in what a built component can see or teach — never a vague disclaimer.

```
> **Blind Spot**
> What this component cannot see or cannot teach, stated specifically — the traffic type, the
> host state, or the condition that defeats it.
```

Worked example:

```
> **Blind Spot**
> A honeypot only ever sees traffic addressed to it. An attacker who compromises a real
> production-shaped host elsewhere on your lab network and pivots internally without ever
> touching the decoy IPs generates nothing in the honeynet's logs at all — this part's honeynet
> teaches you to build a magnet for opportunistic scanning, not a comprehensive internal
> intrusion-detection layer.
```

### 6.8 What Would Change My Mind

An explicit falsifiability statement — what evidence, if observed, would change the stated conclusion or recommendation.

```
> **What Would Change My Mind**
> The specific observation, test result, or resource number that would overturn or materially
> revise the claim just made — a concrete, checkable condition, not a vague "results may vary."
```

Worked example:

```
> **What Would Change My Mind**
> Part 11 recommends against a persistent multi-DC AD forest for a single-operator hobbyist lab
> on the grounds of ongoing maintenance cost. If a reader reports running one comfortably on
> commodity hardware for six-plus months with under an hour a month of upkeep, that specific claim
> — not the general "AD labs are hard" framing — would need revision, and this part would need a
> documented update rather than silent removal of the caveat.
```

### 6.9 Callout usage density

A typical build-focused section carries one Safety Gate (mandatory) and one Validation Test; the other six are used opportunistically. A section stacking all eight callouts is over-boxed — if every paragraph needs an annotation, the prose isn't doing its job. Safety Gate is the one exception to "opportunistic" — see §6.4.

---

## 7. Content-Level Tags

Format locked to `**[TAG]**` — bold, brackets, all caps, placed at the start of the paragraph or subsection it governs. Never a heading, never a footer note, never two tags on one paragraph.

| Tag | Use for | Do not use for |
|---|---|---|
| `[CONCEPT]` | Foundational "what and why" behind a component or architecture choice, with no assumption the reader is building it this minute. | Anything that gives a specific install command or config value — that's a lower tag even if conceptually simple. |
| `[SETUP]` | Concrete installation/configuration steps: what to click, install, edit, or run, in order. | Open-ended exploration with no defined end state — that's `[HANDS-ON LAB]`. |
| `[HANDS-ON LAB]` | A self-contained exercise with a stated goal, steps, and an expected observable result. | A single one-line command embedded in a `[SETUP]` walkthrough — promote it to `[HANDS-ON LAB]` only when it has its own goal and result to check. |
| `[TROUBLESHOOTING]` | A named, specific failure mode of a build step and its fix. | A general "make sure everything is configured correctly" — if it isn't specific and diagnosable, it doesn't belong under this tag. |
| `[SAFETY]` | Isolation, containment, and ownership-boundary content — what must be true about the network or the target before proceeding. | Generic caution language with no checkable condition — that's filler, not `[SAFETY]` content (see §1.2 and the Safety Gate callout, §6.4, which is the preferred home for this content when it needs its own box). |
| `[COST/RESOURCE]` | CPU/RAM/disk/power/dollar cost of a component, and what happens when the reader's hardware is undersized. | Any content with a specific install step embedded — if a cost-tagged paragraph starts giving a command, split it. |

Tagging guidance:

- Most `##` sections carry more than one tag across their subsections — a single section on deploying Zeek plausibly has a `[CONCEPT]` opening, `[COST/RESOURCE]` sizing, `[SETUP]` install steps, a `[HANDS-ON LAB]` verification exercise, and `[TROUBLESHOOTING]` for the two most common install failures. That's expected and good.
- `[CONCEPT]` is the only tag allowed to open a section before any other tag appears — every section needs grounding before it gets into build-phase-specific content.
- The two pairs authors most often confuse: `[SETUP]` (a defined sequence with no exploratory goal beyond "get the thing installed") vs. `[HANDS-ON LAB]` (a bounded exercise with its own stated goal and expected result, even if it reuses steps from a `[SETUP]` section); `[SAFETY]` (isolation/ownership boundary — what must be true about the network) vs. `[TROUBLESHOOTING]` (a build step that's broken — what's wrong with the config). When in doubt, ask "is this about what must be true before I proceed, what to click, what to verify, what broke, what it costs, or why it matters at all" and match to the tag whose question that is.

---

## 8. Table Conventions

- Every data table gets a one-line lead-in sentence stating what decision it supports — e.g., "The table below maps hardware tier to what it can and can't run without swapping."
- Header row uses short noun phrases, capitalized like a title ("Minimum RAM," not "minimum ram" or a full sentence).
- Left-align text columns; skip explicit `:---:` alignment markers unless a column is genuinely numeric and benefits from right-alignment.
- Cell content: fragments, not full sentences with terminal periods, unless a cell genuinely needs more than one sentence (rare — if so, reconsider whether it belongs in a table at all).
- Bare identifiers in the first column. Field names, event IDs used as literal values, and command names inside cells use inline code ticks, same as in prose: `` `LogonType` ``, `` `auditctl` ``.
- Firewall/VLAN rule tables (pfSense/OPNsense-style) use one row per rule with columns for source, destination, port/protocol, and action — this is the preferred format for segmentation rules over a code block, since these rules are usually GUI-configured and have no literal syntax to paste.
- Never leave a cell blank — use an em dash "—" for "not applicable" so the omission is visibly deliberate.
- MITRE IDs and Event IDs get their own greppable column and must follow §4/§5 formatting inside the cell too — a table is not an exemption.
- Tables built from invented/illustrative data are marked `(CONCEPTUAL SAMPLE)` in the caption, same standard as code blocks in §3.

---

## 9. Figures, Diagrams, and Screenshots: Evidence Classification

Reused verbatim from Detection Engineering Handbook V2 §9, deliberately not reinvented (see `BOOK-INDEX.md` provenance item 4) — the two books frequently cite the same physical lab and the same underlying capture files.

### 9.1 Evidence classes (exactly four, always tagged)

| Tag | Meaning | Allowed for |
|---|---|---|
| `CONTROLLED LAB EXAMPLE` | Captured in a lab built specifically to generate this evidence (a build step run, telemetry captured, screenshot/log taken from that run). | Screenshots, exported log excerpts, packet captures. |
| `REAL LAB EXAMPLE` | Captured from a real, pre-existing environment the author actually operates and runs continuously (the Proxmox host, its honeynet, Pi-hole, and monitored Linux containers). Must be scrubbed of real secrets/PII before inclusion. | Screenshots, exported log excerpts. |
| `OFFICIAL REFERENCE` | Sourced from vendor documentation, a public standard, or another authoritative published source, reproduced or closely adapted with attribution. | Vendor console screenshots, official schema diagrams — must cite the source in `REFERENCES.md`. |
| `CONCEPTUAL` | An illustrative diagram with no claim of being captured from a real system — a topology sketch, a data-flow diagram, a sequence diagram of expected behavior. | Mermaid diagrams, hand-drawn architecture figures. |

A figure with no real captured evidence behind it yet is `CONCEPTUAL` if it's a diagram, or an explicit **pending placeholder** (§9.3) if it's meant to eventually be a screenshot. **Never label an uncaptured, aspirational screenshot `CONTROLLED LAB EXAMPLE` "because it will be captured later"** — the tag describes what evidence backs the figure *right now*. This rule has particular teeth in this book: Part 11 exists precisely because the honest answer for a persistent AD-domain screenshot is "this was never built," not a placeholder waiting on a future capture that was already tried and abandoned. Screenshot filenames must additionally carry a `REAL-LAB-` or `SYNTH-UI-` prefix at the filesystem level; `SYNTH-UI-` (a clearly labeled synthetic mockup) is permitted only when a real capture is genuinely infeasible and must be logged in `VISUAL-INVENTORY.md` with a reason.

### 9.2 Caption format — rendered figure (diagram or captured screenshot)

```
**Figure N.M — [Short descriptive title].** *[Evidence class tag].* One to two sentences: what
the figure shows and what it's evidence of, or — for CONCEPTUAL diagrams — what it illustrates
rather than proves. If OFFICIAL REFERENCE: source citation. If CONTROLLED/REAL LAB EXAMPLE: lab
context — host OS/version, tool used, capture date if relevant to tool-version drift.
```

Worked examples:

```
**Figure 4.1 — Isolated lab VLAN topology.** *CONCEPTUAL.* Illustrates the target segmentation
described in Part 4 — management, endpoint, NSM, and honeynet VLANs with default-deny
inter-segment rules. This is an architecture sketch, not a capture from a running build; see
Figure 6.2 for the same topology after a real pfSense build.
```

```
**Figure 15.2 — Honeynet correlated attack session, MITRE-tagged.** *REAL LAB EXAMPLE.* Output
of the honeynet platform's own session-correlation logic, captured from the author's running
CT103 honeynet container, showing a `possible_success`-status session tagged with T1595, T1046,
T1083, and T1190. Captured 2026-09-15; source IPs and internal decoy addresses shown are real but
represent no risk to disclose, since the targets are sacrificial decoy hosts by design.
```

```
**Figure 8.1 — Wazuh manager and indexer resource usage at idle.** *OFFICIAL REFERENCE.*
Reproduced from Wazuh's official sizing-guide documentation. See `REFERENCES.md` entry
[WAZUH-SIZING] for the full citation and retrieval date.
```

### 9.3 Pending placeholder format (only for figures not yet captured/rendered)

```
> **[FIGURE PENDING — target evidence class: <CONTROLLED LAB EXAMPLE | REAL LAB EXAMPLE |
> OFFICIAL REFERENCE | CONCEPTUAL>]** What the figure will show, one sentence. Why it isn't
> captured/rendered yet, one sentence. What claim in the surrounding text it would support.
```

A reviewer finding this block logs it in the tracked-placeholder list; it must be resolved before the unit ships. The one figure in this book that must **never** use this format is any hypothetical AD-domain screenshot in Part 11 — that gap is a documented, permanent non-goal (§9.1), not a pending capture.

---

## 10. Diagram Rendering Requirement

Same rule as the rest of the series, because "diagrams were never rendered" is a named defect the whole NESHBOY series was built to avoid repeating:

- Every `` ```mermaid `` block must be rendered to a static image (SVG preferred, PNG acceptable) and committed alongside the source, referenced via the §9.2 caption format with a real evidence-class tag (almost always `CONCEPTUAL` for a diagram).
- The Mermaid source stays in the file, directly above or below the rendered image reference — it is the editable source of truth, not dead weight to delete once rendered.
- A unit is not review-complete if it contains a `mermaid` fence with no paired rendered figure reference.

---

## 11. Review Checklist (for the independent reviewer, per unit)

Every unit gets an author and a separate reviewer; voice review and technical/build review are separate passes. Work from this list, not from vibes:

1. **Voice:** any banned filler pattern present without being rewritten? Any sentence that doesn't survive the "what does this tell me to install/check/expect" test?
2. **Headings:** correct level nesting, `## Why this part exists` present, and the mandatory Safety Gate box present immediately after it?
3. **Safety:** does the Safety Gate box state a specific, checkable isolation/ownership condition — not a generic caution? Does anything in the part instruct or imply attacking, scanning, or targeting a system the reader doesn't own? (Any "yes" to the second question is an automatic rejection, not a tuning note.)
4. **Code blocks:** every fence tagged, every tag correct for the actual content shown (Sysmon/`ossec.conf` as `xml`, not `yaml`), framing sentences present for real install/config steps?
5. **Identifiers:** Event IDs, auditd keys, Zeek fields, Suricata SIDs, and MITRE IDs formatted per §4–5, first-use expansion present?
6. **Callouts:** correct label string, correct blockquote structure, body length in range, Safety Gate present in every part with no exceptions, density not otherwise excessive (§6.9)?
7. **Tags:** every `##`/`###` subsection carries at least one `[TAG]`, no paragraph carries two?
8. **Tables:** lead-in sentence present, no blank cells, code-tick usage consistent with prose, identifier formatting followed inside cells?
9. **Figures:** every figure has a caption with an evidence-class tag; every pending figure uses the `[FIGURE PENDING]` blockquote and is logged in `VISUAL-INVENTORY.md`; no figure claims `CONTROLLED`/`REAL LAB EXAMPLE` for content that wasn't actually built and run; every Mermaid block has (or is tracked toward) a paired rendered image?
10. **Honesty check (this book's specific defect to avoid):** does any section imply a build was completed, tested, or run end-to-end when it wasn't? Cross-check against `LAB-EVIDENCE-MANIFEST.md` and `BUILD-INVENTORY.md` — an unbuilt component described as if it were build-tested is a rejection, not a wording fix.
11. **Depth check:** does this unit's technical depth match sibling units covering comparable scope? Flag thin sections rather than silently accepting breadth-only coverage.

Any deviation a reviewer approves gets recorded as a documented change to this file, not silent local drift.
