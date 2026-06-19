"""
34 - 文件拷贝与 CSV 实验
实验八：文件数据存储练习

功能：
1. 图片拷贝（二进制文件复制）
2. 文件备份（shutil）
3. 文件内容大小写互换（swapcase）
4. CSV 学生成绩录入、求总分、按姓名查找
"""

import csv
import shutil
from pathlib import Path


# ─── 目录设置 ─────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
WORK_DIR = BASE_DIR / "work"
WORK_DIR.mkdir(exist_ok=True)

# 文件路径常量
TEXT_SOURCE = WORK_DIR / "source.txt"
TEXT_COPY = WORK_DIR / "source_copy.txt"

IMAGE_SOURCE = WORK_DIR / "demo_image.bin"
IMAGE_COPY = WORK_DIR / "demo_image_copy.bin"

BACKUP_SOURCE = WORK_DIR / "need_backup.txt"
BACKUP_TARGET = WORK_DIR / "need_backup_backup.txt"

CASE_SOURCE = WORK_DIR / "case_source.txt"
CASE_TARGET = WORK_DIR / "case_result.txt"

CSV_FILE = WORK_DIR / "students.csv"
CSV_RESULT_FILE = WORK_DIR / "students_with_total.csv"


# ─── 1. 图片拷贝 ──────────────────────────────────────────
def copy_image():
    """以二进制模式复制图片/文件。"""
    with open(IMAGE_SOURCE, "rb") as f:
        data = f.read()

    with open(IMAGE_COPY, "wb") as f:
        f.write(data)

    print(f"[OK] 图片拷贝完成：{IMAGE_COPY.name}")


# ─── 2. 文件备份 ──────────────────────────────────────────
def backup_file():
    """使用 shutil.copy2 备份文件。"""
    shutil.copy2(BACKUP_SOURCE, BACKUP_TARGET)
    print(f"[OK] 文件备份完成：{BACKUP_TARGET.name}")


# ─── 3. 大小写互换 ────────────────────────────────────────
def swap_case():
    """读取文件内容，大写转小写、小写转大写后写入新文件。"""
    with open(CASE_SOURCE, "r", encoding="utf-8") as f:
        text = f.read()

    result = text.swapcase()

    with open(CASE_TARGET, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"[OK] 大小写互换完成：{CASE_TARGET.name}")


# ─── 4. CSV 操作 ──────────────────────────────────────────

def input_scores_to_csv():
    """（1）录入班级学生成绩并保存到 CSV 文件。"""
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["姓名", "语文", "数学", "英语", "理综"])
        writer.writerow(["tom", 124, 137, 145, 260])
        writer.writerow(["jack", 116, 143, 139, 263])

    print(f"[OK] 学生成绩已录入：{CSV_FILE.name}")


def calculate_total():
    """（2）读取 CSV 成绩，计算每个学生的总分，保存到新文件。"""
    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    new_header = header + ["总分"]
    new_rows = []

    for row in rows:
        scores = [int(row[1]), int(row[2]), int(row[3]), int(row[4])]
        total = sum(scores)
        new_rows.append(row + [total])

    with open(CSV_RESULT_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_header)
        writer.writerows(new_rows)

    print(f"[OK] 总分计算完成：{CSV_RESULT_FILE.name}")
    print("班级总成绩如下：")
    print(f"  {'姓名':<6} {'语文':<4} {'数学':<4} {'英语':<4} {'理综':<4} {'总分':<4}")
    print(f"  {'-' * 30}")
    for row in new_rows:
        print(f"  {row[0]:<6} {row[1]:<4} {row[2]:<4} {row[3]:<4} {row[4]:<4} {row[5]:<4}")


def find_student():
    """（3）输入姓名，在 CSV 中查找并显示学生信息。"""
    name = input("请输入姓名：").strip()

    with open(CSV_RESULT_FILE, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if row[0] == name:
                print(f"\n找到学生「{name}」的信息：")
                for key, value in zip(header, row):
                    print(f"  {key}: {value}")
                return

    print(f"\n未找到学生「{name}」")


# ─── 准备素材 ─────────────────────────────────────────────
def prepare_materials():
    """创建实验所需的素材文件。"""
    # 文本素材
    TEXT_SOURCE.write_text("第一行：hello file\n第二行：Python 文件复制练习\n", encoding="utf-8")
    CASE_SOURCE.write_text("Hello Python!\nTom and JACK are Students.\n", encoding="utf-8")
    BACKUP_SOURCE.write_text("这是需要备份的文件。\n", encoding="utf-8")

    # 用二进制文件模拟图片
    IMAGE_SOURCE.write_bytes(b"\x89PNG\r\n\x1a\nfake-image-bytes-for-practice")


# ─── 主程序 ───────────────────────────────────────────────
def main():
    print("=" * 40)
    print("文件数据存储练习 - 实验结果")
    print("=" * 40)

    prepare_materials()

    print("\n--- 1. 图片拷贝 ---")
    copy_image()

    print("\n--- 2. 文件备份 ---")
    backup_file()

    print("\n--- 3. 大小写互换 ---")
    swap_case()

    print("\n--- 4. CSV 操作 ---")
    print("\n[4.1] 录入学生成绩")
    input_scores_to_csv()

    print("\n[4.2] 计算总成绩")
    calculate_total()

    print("\n[4.3] 按姓名查找学生")
    find_student()

    print("\n" + "=" * 40)
    print("所有实验完成！")


if __name__ == "__main__":
    main()
