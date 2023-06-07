import math


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Используем формулу Герона для вычисления площади треугольника
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


square_side = float(input("Введите длину стороны квадрата: "))
square = Square(square_side)

rectangle_side1 = float(input("Введите длину прямоугольника: "))
rectangle_side2 = float(input("Введите ширину прямоугольника: "))
rectangle = Rectangle(rectangle_side1, rectangle_side2)

triangle_side1 = float(input("Введите длину первой стороны треугольника: "))
triangle_side2 = float(input("Введите длину второй стороны треугольника: "))
triangle_side3 = float(input("Введите длину третьей стороны треугольника: "))
triangle = Triangle(triangle_side1, triangle_side2, triangle_side3)

circle_radius = float(input("Введите радиус круга: "))
circle = Circle(circle_radius)

figures = [("Квадрат", square), ("Прямоугольник", rectangle), ("Треугольник", triangle), ("Круг", circle)]

# Сортировка фигур по убыванию площади
sorted_figures_by_area = sorted(figures, key=lambda x: x[1].calculate_area(), reverse=True)

# Сортировка фигур по убыванию периметра
sorted_figures_by_perimeter = sorted(figures, key=lambda x: x[1].calculate_perimeter(), reverse=True)

print("Фигуры в порядке убывания площади:")
for figure in sorted_figures_by_area:
    print("Название фигуры:", figure[0])
    print("Площадь фигуры:", figure[1].calculate_area())
    print()

print("Фигуры в порядке убывания периметра:")
for figure in sorted_figures_by_perimeter:
    print("Название фигуры:", figure[0])
    print("Периметр фигуры:", figure[1].calculate_perimeter())
    print()
