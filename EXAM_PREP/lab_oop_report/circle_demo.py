"""
实验 1：圆类 Circle。

包含：圆心位置、半径、颜色、构造函数、周长和面积方法。
运行：python EXAM_PREP/lab_oop_report/circle_demo.py
"""

import math


class Circle:
    def __init__(self, x: float, y: float, radius: float, color: str) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def show_info(self) -> None:
        print(f"圆心位置：({self.x}, {self.y})")
        print(f"半径：{self.radius}")
        print(f"颜色：{self.color}")
        print(f"周长：{self.circumference():.2f}")
        print(f"面积：{self.area():.2f}")


if __name__ == "__main__":
    circle = Circle(0, 0, 5, "红色")
    circle.show_info()

