"""
实验 2：课程类 Course。

包含：课程名、课程编号、任课老师、上课地点。
其中 location 为私有属性。
运行：python EXAM_PREP/lab_oop_report/course_demo.py
"""


class Course:
    def __init__(self, name: str, number: str, teacher: str, location: str) -> None:
        self.name = name
        self.number = number
        self.teacher = teacher
        self.__location = location

    def get_location(self) -> str:
        return self.__location

    def set_location(self, location: str) -> None:
        self.__location = location

    def show_info(self) -> None:
        print(f"课程名：{self.name}")
        print(f"课程编号：{self.number}")
        print(f"任课老师：{self.teacher}")
        print(f"上课地点：{self.__location}")


if __name__ == "__main__":
    course = Course("Python 程序设计", "PY001", "王老师", "教学楼 A101")
    course.show_info()

    print("修改上课地点后：")
    course.set_location("实验楼 B203")
    course.show_info()

