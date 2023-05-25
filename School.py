from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class Courses:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = 0

    def set_grade(self, student, grade):
        self.students[student.name] = grade

    def get_grade(self, student):
        return self.students.get(student.name, "N/A")


class MathCourse(Courses):
    def __init__(self, teacher):
        super().__init__("Math", teacher)


class EnglishCourse(Courses):
    def __init__(self, teacher):
        super().__init__("English", teacher)


class SchoolOperations(ABC):
    @abstractmethod
    def view_progress(self, student):
        pass


class Student(Person, SchoolOperations):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def view_progress(self, course):
        grade = course.get_grade(self)
        if grade == "N/A":
            print(f"{self.name} is not enrolled in {course.name}.")
        else:
            print(f"{self.name}'s grade in {course.name} is {grade}.")


class Teacher(Person, SchoolOperations):
    def __init__(self, name, contact, subject):
        super().__init__(name, contact)
        self.subject = subject

    def assign_teacher(self, course):
        course.teacher = self

    def view_progress(self, student):
        for course in student.courses:
            grade = course.get_grade(student)
            if grade == "N/A":
                print(f"{student.name} is not enrolled in {course.name}.")
            else:
                print(f"{student.name}'s grade in {course.name} is {grade}.")


# Client code
math_teacher = Teacher("Mr. Smith", "555-1234", "Math")
english_teacher = Teacher("Ms. Jones", "555-5678", "English")

math_course = MathCourse(math_teacher)
english_course = EnglishCourse(english_teacher)

alice = Student("Alice", "555-1111")
bob = Student("Bob", "555-2222")

alice.enroll(math_course)
alice.enroll(english_course)
bob.enroll(math_course)

math_course.set_grade(alice, 90)
math_course.set_grade(bob, 85)
english_course.set_grade(alice, 95)

alice.view_progress(math_course)
alice.view_progress(english_course)

bob.view_progress(math_course)
