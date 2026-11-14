import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent


def build(d):
    r = subprocess.run(
        [sys.executable, "-W", "ignore", str(d / "algo.py")],
        capture_output=True,
        text=True,
        check=True,
    )
    out_dir = d / "output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "result.txt").write_text(r.stdout, encoding="utf-8")

    definition = (d / "definition.md").read_text(encoding="utf-8").strip()
    code = (d / "algo.py").read_text(encoding="utf-8").strip()
    output = r.stdout.strip()

    imgs = sorted(out_dir.glob("*.png"))
    img_block = "\n\n".join(f"![{img.stem}](output/{img.name})" for img in imgs)

    readme = f"""{definition}

---

<details>
<summary><strong>Click to view Qiskit Implementation</strong></summary>

```python
{code}
```

</details>

<details>
<summary><strong>Click to view Verified Simulator Output & Plots</strong></summary>

```text
{output}
```

{img_block}

</details>
"""
    (d / "README.md").write_text(readme, encoding="utf-8")
    print("built", d.name)


if __name__ == "__main__":
    for d in sorted((root / "algorithms").iterdir()):
        if d.is_dir():
            build(d)

