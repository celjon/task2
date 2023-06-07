class Student:
    def __init__(self, name, age, group_number, average_grade):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def get_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)

    def get_scholarship(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5 and self.average_grade > 3:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        self_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()

        if self_scholarship > other_scholarship:
            return f"{self.name} получает большую стипендию, чем {other.name}"
        elif self_scholarship < other_scholarship:
            return f"{self.name} получает меньшую стипендию, чем {other.name}"
        else:
            return "Оба студента получают одинаковую стипендию"


class GraduateStudent(Student):
    def __init__(self, name, age, group_number, average_grade):
        super().__init__(name, age, group_number, average_grade)

    def get_info(self):
        super().get_info()

    def get_scholarship(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5 and self.average_grade > 3:
            return 6000
        else:
            return 0

student1 = Student("Иван Иванов", 20, "Группа 1", 4.8)
student2 = Student("Анна Смирнова", 19, "Группа 2", 5.0)

graduate_student1 = GraduateStudent("Петр Петров", 25, "Группа 3", 4.9)
graduate_student2 = GraduateStudent("Мария Козлова", 24, "Группа 4", 5.0)

# Вывод информации о студентах и аспирантах
student1.get_info()
print("Стипендия студента:", student1.get_scholarship())
print()

student2.get_info()
print("Стипендия студента:", student2.get_scholarship())
print()

graduate_student1.get_info()
print("Стипендия аспиранта:", graduate_student1.get_scholarship())
print()

graduate_student2.get_info()
print("Стипендия аспиранта:", graduate_student2.get_scholarship())
print()

# Сравнение размера стипендии
print(student1.compare_scholarship(student2))
print(graduate_student1.compare_scholarship(graduate_student2))



