import os

root = "docs/chapitres"
index_file = "docs/index.md"

entries = []

for rootdir, dirs, files in os.walk(root):
    files = [f for f in files if f.endswith(".md")]
    for f in files:
        full = os.path.join(rootdir, f)
        rel = os.path.relpath(full, "docs")
        rel = rel.replace(".md", "")
        entries.append(rel)

entries.sort()

with open(index_file, "w", encoding="utf-8") as f:
    f.write("# Documentation\n\n")
    f.write("```{toctree}\n:maxdepth: 2\n\n")
    for e in entries:
        f.write(f"{e}\n")
    f.write("```\n")