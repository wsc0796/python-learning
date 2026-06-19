"""
34 - 文件拷贝与 CSV 实验参考答案

先自己写 practice_34_file_csv.py。
卡住 10 分钟以后，再看这个文件对答案。
"""

from pathlib import Path
import csv
import shutil


BASE_DIR = Path(__file__).parent
WORK_DIR = BASE_DIR / "work"

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


def prepare_demo_files() -> None:
    WORK_DIR.mkdir(exist_ok=True)

    for output_file in [
        TEXT_COPY,
        IMAGE_COPY,
        BACKUP_TARGET,
        CASE_TARGET,
        CSV_FILE,
        CSV_RESULT_FILE,
    ]:
        if output_file.exists():
            output_file.unlink()

    TEXT_SOURCE.write_text(
        "第一行：hello file\n第二行：Python 文件复制练习\n",
        encoding="utf-8",
    )
    IMAGE_SOURCE.write_bytes(b"\x89PNG\r\n\x1a\nfake-image-bytes-for-practice")
    BACKUP_SOURCE.write_text("这是需要备份的文件。\n", encoding="utf-8")
    CASE_SOURCE.write_text(
        "Hello Python!\nTom and JACK are Students.\n",
        encoding="utf-8",
    )


def copy_text_file() -> None:
    with open(TEXT_SOURCE, "r", encoding="utf-8") as f:
        content = f.read()

    with open(TEXT_COPY, "w", encoding="utf-8") as f:
        f.write(content)


def copy_image_file() -> None:
    with open(IMAGE_SOURCE, "rb") as f:
        data = f.read()

    with open(IMAGE_COPY, "wb") as f:
        f.write(data)


def backup_file() -> None:
    shutil.copy2(BACKUP_SOURCE, BACKUP_TARGET)


def swap_file_case() -> None:
    with open(CASE_SOURCE, "r", encoding="utf-8") as f:
        text = f.read()

    result = text.swapcase()

    with open(CASE_TARGET, "w", encoding="utf-8") as f:
        f.write(result)


def input_students_to_csv() -> None:
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["姓名", "语文", "数学", "英语", "理综"])
        writer.writerow(["tom", 124, 137, 145, 260])
        writer.writerow(["jack", 116, 143, 139, 263])


def calculate_total_score() -> None:
    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    new_header = header + ["总分"]
    new_rows = []

    for row in rows:
        chinese = int(row[1])
        math = int(row[2])
        english = int(row[3])
        science = int(row[4])
        total = chinese + math + english + science
        new_rows.append(row + [total])

    with open(CSV_RESULT_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_header)
        writer.writerows(new_rows)


def find_student_by_name(name: str) -> None:
    with open(CSV_RESULT_FILE, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if row[0] == name:
                print("找到学生：")
                for key, value in zip(header, row):
                    print(f"{key}: {value}")
                return

    print("未找到")


def main() -> None:
    prepare_demo_files()
    copy_text_file()
    copy_image_file()
    backup_file()
    swap_file_case()
    input_students_to_csv()
    calculate_total_score()
    find_student_by_name("tom")
    print("全部完成")


if __name__ == "__main__":
    main()
