# REFERENCES.md — Full Citations for OFFICIAL REFERENCE Claims

**Status:** First pass. `STYLE-GUIDE.md` §9 and several parts (11, 15, 18) point here for the full citation behind an `OFFICIAL REFERENCE`-tagged claim or figure, keyed by a bracket ID named in the citing text (e.g. `[COWRIE-REPO]`). This file currently covers the entries added during the 2026-09-16 citation pass, concentrated in Part 15 (honeypots/honeynet) and the install/repository steps in Parts 5, 8, 13, and 17. It does not yet carry entries for every pre-existing `OFFICIAL REFERENCE` tag in the book (for example, several of Part 11's Microsoft-documentation citations and Part 18's Red Canary/Atomic Red Team citations predate this file and still need their own entries added in a future pass) — that gap is stated here rather than papered over with a placeholder.

Every entry below was independently fetched and read, in full, on the retrieval date shown, before being added — none are reconstructed from memory or pattern-matched from a URL convention.

---

## Honeypot and honeynet research (Part 15)

**[SPITZNER-HONEYPOTS-2002]**
Lance Spitzner, *Honeypots: Tracking Hackers*, Addison-Wesley, 2002. ISBN 0-321-10895-7. The practitioner book that put the low-interaction/high-interaction honeypot vocabulary Part 15 §1 uses into general circulation.
Retrieved 2026-09-16: https://openlibrary.org/isbn/0321108957

**[HONEYNET-PROJECT]**
The Honeynet Project, official website and About page. Volunteer, international 501(c)(3) non-profit security research organization, operating since 1999, dedicated to investigating attacks and developing open-source security tools; cited in Part 15 §1 as one of the sources of the low/medium- vs. high-interaction honeypot vocabulary this part uses. (Note: the official site and About page describe the organization itself but do not spell out a specific "honeynet vs. honeypot" definition, so this entry is not used to support any claim about how the Honeynet Project itself distinguishes the two terms.)
Retrieved 2026-09-16: https://www.honeynet.org/ and https://www.honeynet.org/about/

**[PANG-BACKRAD-2004]**
R. Pang, V. Yegneswaran, P. Barford, V. Paxson, and L. Peterson, "Characteristics of Internet Background Radiation," *Proceedings of the ACM Internet Measurement Conference (IMC)*, October 2004 (ACM SIGCOMM IMC "Test of Time" award). Foundational network-telescope study of unsolicited internet traffic hitting unused address space — the academic counterpart to what Part 15 §1's honeynet observes at hobbyist scale.
Retrieved 2026-09-16 (via author's own publication list at icir.org/vern): https://www.icir.org/vern/papers/radiation-imc04.pdf

**[COWRIE-REPO]**
Michel Oosterhof et al., Cowrie SSH/Telnet honeypot, official GitHub repository. Confirmed current install methods (pip, Docker, git checkout) and the project's own "medium to high interaction" description, cited in Part 15 §2, Table 15.1, and §4 step 2.
Retrieved 2026-09-16: https://github.com/cowrie/cowrie

**[DIONAEA-REPO]**
DinoTools, Dionaea honeypot, official GitHub repository. Confirmed current protocol coverage (SMB, FTP, HTTP, MSSQL, MySQL, SIP, TFTP, MQTT, and others), cited in Part 15 §2 and Table 15.1.
Retrieved 2026-09-16: https://github.com/DinoTools/dionaea

**[TPOT-REPO]**
Deutsche Telekom Security, T-Pot ("the all in one, optionally distributed, multiarch honeypot platform"), official GitHub repository. Confirmed current bundled honeypot count (20+), Suricata/Elastic Stack components, and active maintainer, cited in Part 15 §2 and Table 15.1.
Retrieved 2026-09-16: https://github.com/telekom-security/tpotce

**[CVE-2018-10561]**
MITRE/NIST, "CVE-2018-10561" — Dasan GPON home router authentication bypass via a `?images` URI suffix (CVSS 3.1: 9.8, Critical). Cited in Part 15 Figure 15.4 against the real `/GponForm/diag_Form` decoy hit shown there.
Retrieved 2026-09-16 (via NVD's own CVE API): https://nvd.nist.gov/vuln/detail/CVE-2018-10561

**[CVE-2018-10562]**
MITRE/NIST, "CVE-2018-10562" — Dasan GPON home router command injection via the `dest_host` parameter of a `diag_action=ping` request (CVSS 3.1: 9.8, Critical); commonly chained with CVE-2018-10561's auth bypass. Cited in Part 15 Figure 15.4 alongside CVE-2018-10561.
Retrieved 2026-09-16 (via NVD's own CVE API): https://nvd.nist.gov/vuln/detail/CVE-2018-10562

## Install/repository currency checks (Parts 5, 8, 13, 17)

**[PROXMOX-REPOS]**
Proxmox Server Solutions GmbH, "Package Repositories," official Proxmox VE documentation wiki. Confirmed the no-subscription repository's current recommended format has moved to deb822 (`/etc/apt/sources.list.d/proxmox.sources`) and that trixie's `apt` warns on the legacy single-line `.list` syntax Part 5 §6.1 still uses. Cited in Part 5 §6.1.
Retrieved 2026-09-16: https://pve.proxmox.com/wiki/Package_Repositories

**[WAZUH-QUICKSTART]**
Wazuh Inc., "Quickstart installation guide," official Wazuh documentation. Confirmed the all-in-one installer pattern (`wazuh-install.sh -a`) and that the docs' own current example has moved past the 4.7 path Part 8 §3.2 pins to. Cited in Part 8 §3.2.
Retrieved 2026-09-16: https://documentation.wazuh.com/current/quickstart.html

**[ZEEK-INSTALL-DOCS]**
The Zeek Project, "Installing Zeek Packages," official Zeek documentation. Confirmed the openSUSE Build Service `security:zeek` repository pattern Part 13 §3.1 uses is still current and live, now also serving Zeek 7.x/8.x builds well past the 6.0/6.1 line that part targets (Zeek 9.0 shipped separately just days before this retrieval). Cited in Part 13 §3.1.
Retrieved 2026-09-16: https://docs.zeek.org/en/master/install.html

**[GRAFANA-INSTALL-DOCS]**
Grafana Labs, "Install Grafana on Debian or Ubuntu," official Grafana documentation. Confirmed the apt repository URL Part 17 §3.1 uses is current, and that Grafana's own docs have since renamed the recommended GPG key file (`gpg-full.key`, stored as `.asc`) with an explicit permissions step not shown in that section. Cited in Part 17 §3.1.
Retrieved 2026-09-16: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
