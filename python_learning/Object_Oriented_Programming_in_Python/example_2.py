# Object Oriented Programming in Python
# Пример использования классов

class Student:
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name
        self.age = age
        self.grade = grade  # 1 - 100

    def get_grade(self) -> int:
        return self.grade


class Course:
    def __init__(self, name: str, max_sutudents: int) -> None:
        self.name = name
        self.max_students = max_sutudents
        self.students: list[Student] = []

    def add_student(self, student: str) -> bool:
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        n = (sum([el.get_grade() for el in self.students])
             / len(self.students))
        # Or
        value = 0
        for student in self.students:
            value += student.get_grade()
        n = value / len(self.students)

        return n if round(n, 0) != n else int(n)


s1 = Student('Tim', 17, 95)
s2 = Student('Bill', 15, 75)
s3 = Student('Jill', 16, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
