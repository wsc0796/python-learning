# -*- coding: utf-8 -*-
"""
期末复习笔记 -- MD -> PDF 批量转换脚本
纯 Windows 方案: markdown 转 HTML, Edge 无头模式转 PDF (无需安装GTK3)
用法: python convert_to_pdf.py
"""

import os
import subprocess
import sys

ROOT = r"C:\Users\50469\python-learning"
OUT = os.path.join(ROOT, "期末复习笔记")

DAY_MAP = {
    "day02": {
        "dirs": [
            ("01-fstring", ["theory_01_fstring.md"]),
            ("24-string-methods", ["theory_24_string_methods.md"]),
            ("02-slice", ["theory_02_slice.md"]),
            ("04-listcomp-class", ["theory_04_listcomp_lambda_class.md"]),
            ("06-dict", ["theory_06_dict.md"]),
            ("17-tuple-set", ["theory_17_tuple_set.md"]),
            ("21-list-deep", ["theory_21_list_deep.md"]),
        ],
        "files": [
            "references/python-strings.md",
        ],
    },
    "day03": {
        "dirs": [
            ("25-function-basics", [
                "theory_25_function_basics.md",
                "theory_25_recursion.md",
                "笔记_内置函数速查.md",
            ]),
            ("11-closure-decorator", ["theory_11_closure_decorator.md"]),
        ],
        "files": [
            "16-python-gaps/笔记_高阶函数.md",
            "00-学习路线/课堂老师程序-函数专题对照.md",
        ],
    },
}

CSS = """
body {
    font-family: "Microsoft YaHei", "SimSun", sans-serif;
    max-width: 800px;
    margin: 40px auto;
    line-height: 1.8;
    color: #333;
}
h1 { border-bottom: 2px solid #4A90D9; padding-bottom: 6px; }
h2 { color: #4A90D9; margin-top: 28px; }
h3 { color: #555; }
code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
pre { background: #f4f4f4; padding: 16px; border-radius: 6px; overflow-x: auto; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
th { background: #4A90D9; color: white; }
blockquote { border-left: 4px solid #4A90D9; padding-left: 16px; color: #666; margin: 12px 0; }
img { max-width: 100%; }
"""


def copy_md_files():
    for day, spec in DAY_MAP.items():
        day_dir = os.path.join(OUT, day)
        os.makedirs(day_dir, exist_ok=True)

        for subdir, filenames in spec["dirs"]:
            for fname in filenames:
                src = os.path.join(ROOT, subdir, fname)
                dst = os.path.join(day_dir, fname)
                if os.path.exists(src):
                    with open(src, encoding="utf-8") as f:
                        content = f.read()
                    with open(dst, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  [OK] copy: {subdir}/{fname}")
                else:
                    print(f"  [MISS] not found: {subdir}/{fname}")

        for rel_path in spec["files"]:
            fname = os.path.basename(rel_path)
            src = os.path.join(ROOT, rel_path)
            dst = os.path.join(day_dir, fname)
            if os.path.exists(src):
                with open(src, encoding="utf-8") as f:
                    content = f.read()
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [OK] copy: {rel_path}")
            else:
                print(f"  [MISS] not found: {rel_path}")


def md_to_html(md_path):
    import markdown
    with open(md_path, encoding="utf-8") as f:
        md_content = f.read()
    html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])
    fname = os.path.basename(md_path)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>{fname}</title><style>{CSS}</style></head>
<body>{html_body}</body>
</html>"""


def find_edge():
    """Find Microsoft Edge executable path."""
    paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None


def convert_to_pdf():
    edge = find_edge()
    if not edge:
        print("\n[X] Microsoft Edge not found. Trying Chrome fallback...")
        edge = "chrome"  # try Chrome as fallback

    for day in DAY_MAP:
        day_dir = os.path.join(OUT, day)
        if not os.path.isdir(day_dir):
            continue
        for fname in os.listdir(day_dir):
            if not fname.endswith(".md"):
                continue
            md_path = os.path.join(day_dir, fname)
            html_path = md_path.replace(".md", ".html")
            pdf_path = md_path.replace(".md", ".pdf")

            # Step 1: MD -> HTML
            print(f"  MD -> HTML: {day}/{fname}")
            full_html = md_to_html(md_path)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(full_html)

            # Step 2: HTML -> PDF via Edge headless
            print(f"  HTML -> PDF: {day}/{fname}")
            abs_html = os.path.abspath(html_path)
            abs_pdf = os.path.abspath(pdf_path)

            result = subprocess.run(
                [edge, "--headless", "--disable-gpu",
                 f"--print-to-pdf={abs_pdf}", abs_html],
                capture_output=True, text=True, timeout=30
            )

            if os.path.exists(pdf_path):
                print(f"  [OK] PDF: {day}/{fname} ({os.path.getsize(pdf_path)} bytes)")
            else:
                print(f"  [FAIL] PDF generation failed for {fname}")
                print(f"    Edge stderr: {result.stderr[:200]}")


if __name__ == "__main__":
    print("=" * 50)
    print("[Step 1] Copy MD notes")
    print("=" * 50)
    copy_md_files()

    print("\n" + "=" * 50)
    print("[Step 2] MD -> HTML -> PDF (via Edge)")
    print("=" * 50)
    convert_to_pdf()

    print("\n[DONE] Check 期末复习笔记/day02/ and day03/")
