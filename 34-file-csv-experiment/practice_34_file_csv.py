"""
34 - 文件拷贝与 CSV 实验练习

运行：
    python practice_34_file_csv.py

规则：
1. 先按 TODO 顺序手敲，不要复制粘贴。
2. 每完成一关就运行一次。
3. 不会时先看 theory_34_file_csv_experiment.md。
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
    """创建练习素材。你不用手动准备 txt、图片、csv。"""
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

    # 这里用二进制文件模拟图片。真正图片复制时，代码完全一样，只是文件名换成 .jpg/.png。
    IMAGE_SOURCE.write_bytes(b"\x89PNG\r\n\x1a\nfake-image-bytes-for-practice")

    BACKUP_SOURCE.write_text("这是需要备份的文件。\n", encoding="utf-8")

    CASE_SOURCE.write_text(
        "Hello Python!\nTom and JACK are Students.\n",
        encoding="utf-8",
    )


def copy_text_file() -> None:
    """第一关：复制 txt 文件。"""
    # TODO 1：复制 txt 文件
    #
    # 你要做的事：
    # 把 TEXT_SOURCE 这个文件里的文字，复制到 TEXT_COPY 这个新文件里。
    #
    # 第一步：读源文件
    # 写法提示：
    # with open(TEXT_SOURCE, "r", encoding="utf-8") as f:
    #     content = f.read()
    #
    # 解释：
    # "r" = read，读取文本
    # content = 文件里的全部文字
    #
    # 第二步：写目标文件
    # 写法提示：
    # with open(TEXT_COPY, "w", encoding="utf-8") as f:
    #     f.write(content)
    #
    # 解释：
    # "w" = write，写入文本
    # f.write(content) = 把刚才读到的文字写进去
    #
    # 注意：这一关不要用 shutil，因为这一关练的是 open/read/write。
    with open(TEXT_SOURCE, "r", encoding="utf-8") as f:
        content = f.read()

    with open(TEXT_COPY, "w", encoding="utf-8") as f:
        f.write(content)


def copy_image_file() -> None:
    """第二关：复制图片/二进制文件。"""
    # TODO 2：复制图片/二进制文件
    #
    # 你要做的事：
    # 把 IMAGE_SOURCE 复制成 IMAGE_COPY。
    #
    # 这关和 txt 拷贝很像，但是模式不同：
    # txt 用 "r" / "w"
    # 图片用 "rb" / "wb"
    #
    # 第一步：
    # with open(IMAGE_SOURCE, "rb") as f:
    #     data = f.read()
    #
    # 第二步：
    # with open(IMAGE_COPY, "wb") as f:
    #     f.write(data)
    #
    # 注意：
    # 图片/视频/压缩包这种二进制文件，不写 encoding。
    with open(IMAGE_SOURCE, "rb") as f:
        data = f.read()

    with open(IMAGE_COPY, "wb") as f:
        f.write(data)


def backup_file() -> None:
    """第三关：文件备份。"""
    # TODO 3：文件备份
    #
    # 你要做的事：
    # 把 BACKUP_SOURCE 备份成 BACKUP_TARGET。
    #
    # 这次不用自己 read/write，直接用工具：
    #
    # shutil.copy2(BACKUP_SOURCE, BACKUP_TARGET)
    #
    # 解释：
    # shutil 是 Python 自带的文件工具箱。
    # copy2(原文件, 备份文件) = 复制并尽量保留文件信息。
    shutil.copy2(BACKUP_SOURCE, BACKUP_TARGET)


def swap_file_case() -> None:
    """第四关：文件内容大小写互换。"""
    # TODO 4：文件内容大小写互换
    #
    # 你要做的事：
    # 读取 CASE_SOURCE 里的文字。
    # 把大写变小写，小写变大写。
    # 写入 CASE_TARGET。
    #
    # 第一步：读取文本
    # with open(CASE_SOURCE, "r", encoding="utf-8") as f:
    #     text = f.read()
    #
    # 第二步：大小写互换
    # result = text.swapcase()
    #
    # 第三步：写入新文件
    # with open(CASE_TARGET, "w", encoding="utf-8") as f:
    #     f.write(result)
    with open(CASE_SOURCE, "r", encoding="utf-8") as f:
        text = f.read()

    result = text.swapcase()

    with open(CASE_TARGET, "w", encoding="utf-8") as f:
        f.write(result)


def input_students_to_csv() -> None:
    """第五关 A：录入学生成绩并保存到 CSV。"""
    # TODO 5：录入学生成绩并保存到 CSV
    #
    # 先不要做 input 输入，先写死老师给的两行数据。
    # 这样你先把 CSV 写入流程跑通。
    #
    # 目标文件内容：
    # 姓名,语文,数学,英语,理综
    # tom,124,137,145,260
    # jack,116,143,139,263
    #
    # 写法骨架：
    # with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["姓名", "语文", "数学", "英语", "理综"])
    #     writer.writerow(["tom", 124, 137, 145, 260])
    #     writer.writerow(["jack", 116, 143, 139, 263])
    #
    # 解释：
    # writerow = write row，写一行。
    # 列表里每个元素就是 CSV 的一列。
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["姓名", "语文", "数学", "英语", "理综"])
        writer.writerow(["tom", 124, 137, 145, 260])
        writer.writerow(["jack", 116, 143, 139, 263])


def calculate_total_score() -> None:
    """第五关 B：读取 CSV，计算每个学生总成绩，保存到新文件。"""
    # TODO 6：读取 CSV，计算总分，保存到新文件
    #
    # 你要做的事：
    # 读取 students.csv。
    # 给每个学生算总分。
    # 写入 students_with_total.csv。
    #
    # 一行学生数据长这样：
    # ["tom", "124", "137", "145", "260"]
    #
    # 每个位置的含义：
    # row[0] = 姓名
    # row[1] = 语文
    # row[2] = 数学
    # row[3] = 英语
    # row[4] = 理综
    #
    # 注意：
    # CSV 读出来的 "124" 是字符串。
    # 要计算必须 int(row[1])。
    #
    # 新文件格式：
    # 姓名,语文,数学,英语,理综,总分
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
    """第五关 C：输入姓名，查找学生信息。"""
    # TODO 7：按姓名查找学生
    #
    # 你要做的事：
    # 打开 CSV_RESULT_FILE。
    # 一行一行找。
    # 如果某一行 row[0] 等于 name，就打印这个学生的信息。
    #
    # 关键判断：
    # if row[0] == name:
    #
    # row[0] 是 CSV 里第一列，也就是姓名。
    #
    # 如果找到了，可以这样打印：
    # print(row)
    #
    # 更好一点：
    # for key, value in zip(header, row):
    #     print(f"{key}: {value}")
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


def check_file_exists(path: Path, label: str) -> None:
    if path.exists():
        print(f"OK: {label} -> {path.name}")
    else:
        print(f"未完成: {label} -> {path.name}")


def main() -> None:
    prepare_demo_files()

    print("\n=== 第一关：txt 文件拷贝 ===")
    copy_text_file()
    check_file_exists(TEXT_COPY, "txt 拷贝")

    print("\n=== 第二关：图片/二进制文件拷贝 ===")
    copy_image_file()
    check_file_exists(IMAGE_COPY, "图片拷贝")

    print("\n=== 第三关：文件备份 ===")
    backup_file()
    check_file_exists(BACKUP_TARGET, "文件备份")

    print("\n=== 第四关：大小写互换 ===")
    swap_file_case()
    check_file_exists(CASE_TARGET, "大小写转换结果")

    print("\n=== 第五关：CSV 学生成绩 ===")
    input_students_to_csv()
    check_file_exists(CSV_FILE, "学生成绩 CSV")

    calculate_total_score()
    check_file_exists(CSV_RESULT_FILE, "带总分的新 CSV")

    name = input("请输入姓名：").strip()
    find_student_by_name(name)


if __name__ == "__main__":
    main()
