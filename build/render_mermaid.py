import os
import re
import subprocess
import glob

ROOT = r"C:\Users\User\projects\soc-home-lab-handbook"
CHAPTER_GLOBS = [
    os.path.join(ROOT, "chapters", "*.md"),
    os.path.join(ROOT, "appendices", "*.md"),
]
DIAGRAM_DIR = os.path.join(ROOT, "assets", "diagrams")
os.makedirs(DIAGRAM_DIR, exist_ok=True)

MERMAID_RE = re.compile(r"```mermaid\r?\n(.*?)```\r?\n", re.DOTALL)
CAPTION_RE = re.compile(r"\*\*Figure (\d+)\.(\d+) — (.*?)\.\*\*")
MMDC_CMD = ["npx", "-y", "@mermaid-js/mermaid-cli"]

STOPWORDS = {"the", "a", "an", "and", "of", "in", "on", "to", "into", "across",
             "inside", "versus", "vs", "where", "it", "actually", "this", "for",
             "with", "at", "by", "from", "over", "its", "that", "not"}


def slugify(title, max_words=6):
    words = re.sub(r"[^a-zA-Z0-9\s-]", "", title).lower().split()
    kept = [w for w in words if w not in STOPWORDS]
    if len(kept) < 3:
        kept = words
    kept = kept[:max_words]
    slug = "-".join(kept)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:60].rstrip("-")


def existing_svg_for(part_num, fig_num):
    pattern = os.path.join(DIAGRAM_DIR, f"fig-{part_num:02d}-{fig_num:02d}-*.svg")
    matches = glob.glob(pattern)
    return matches[0] if matches else None


def render_one(mmd_text, out_svg):
    tmp_mmd = out_svg + ".mmd"
    with open(tmp_mmd, "w", encoding="utf-8") as f:
        f.write(mmd_text)
    cmd = MMDC_CMD + ["-i", tmp_mmd, "-o", out_svg, "-b", "white"]
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=90)
    ok = os.path.exists(out_svg) and os.path.getsize(out_svg) > 0
    try:
        os.remove(tmp_mmd)
    except OSError:
        pass
    return ok, result.stdout, result.stderr


def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    matches = list(MERMAID_RE.finditer(content))
    if not matches:
        return 0, 0, 0

    rendered = 0
    skipped = 0
    failed = 0
    new_content = content
    offset = 0

    for m in matches:
        mmd_text = m.group(1)
        insert_at = m.end() + offset

        # Already linked? Skip blank lines and check for an image tag immediately after.
        tail = new_content[insert_at:insert_at + 400]
        stripped_tail = tail.lstrip("\r\n")
        if stripped_tail.startswith("!["):
            skipped += 1
            continue

        # Find the figure caption within the next ~600 chars to get N.M and title.
        window = new_content[insert_at:insert_at + 600]
        cap = CAPTION_RE.search(window)
        if not cap:
            print(f"  WARNING: no Figure caption found after a mermaid fence in {os.path.basename(path)}; skipping.")
            failed += 1
            continue

        part_num, fig_num, title = int(cap.group(1)), int(cap.group(2)), cap.group(3)
        label = f"Figure {part_num}.{fig_num} — {title}"

        existing = existing_svg_for(part_num, fig_num)
        if existing:
            fig_filename = os.path.basename(existing)
            ok = True
        else:
            slug = slugify(title)
            fig_filename = f"fig-{part_num:02d}-{fig_num:02d}-{slug}.svg"
            out_svg = os.path.join(DIAGRAM_DIR, fig_filename)
            ok, out, err = render_one(mmd_text, out_svg)
            if not ok:
                failed += 1
                print(f"  RENDER FAILED for {fig_filename}: {err.strip()[:300]}")
                continue

        rel_path = f"../assets/diagrams/{fig_filename}"
        img_line = f"\n![{label}]({rel_path})\n"
        new_content = new_content[:insert_at] + img_line + new_content[insert_at:]
        offset += len(img_line)
        rendered += 1
        print(f"  {os.path.basename(path)}: Figure {part_num}.{fig_num} -> {fig_filename} ({'reused' if existing else 'rendered'})")

    if rendered:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return rendered, skipped, failed


def main():
    files = []
    for g in CHAPTER_GLOBS:
        files.extend(sorted(glob.glob(g)))

    total_rendered = 0
    total_skipped = 0
    total_failed = 0
    for path in files:
        rendered, skipped, failed = process_file(path)
        total_rendered += rendered
        total_skipped += skipped
        total_failed += failed

    print(f"\n=== TOTAL: rendered/linked={total_rendered} already-linked-skipped={total_skipped} failed={total_failed} ===")


if __name__ == "__main__":
    main()
