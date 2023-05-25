from abc import ABC, abstractmethod


class Course:
    def __init__(self, name, instructor, content):
        self._name = name
        self._instructor = instructor
        self._content = content

    def display_info(self):
        print(f"Course's name: {self._name}")
        print(f"Instructor: {self._instructor}")
        print(f"Content: {self._content}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_instructor(self):
        return self._instructor

    def set_instructor(self, instructor):
        self._instructor = instructor

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content


class UnderGraduate(Course):
    def __init__(self, name, instructor, content, level):
        super().__init__(name, instructor, content)
        self.level = level

    def display_info(self):
        super().display_info()
        print(f"Level: {self.level}")


class Graduate(Course):
    def __init__(self, name, instructor, content, level):
        super().__init__(name, instructor, content)
        self.level = level

    def display_info(self):
        super().display_info()
        print(f"Level: {self.level}")


class CourseAssignment(ABC):
    @abstractmethod
    def submit_assignment(self):
        pass


class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")


class Student(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.courses = []
        self.progress = {}

    def enroll_course(self, course):
        self.courses.append(course)
        self.progress[course] = 0

    def submit_assignment(self, course):
        self.progress[course] += 1
        print(f"{self.name} has submitted the assignment for {course.name}")

    def view_progress(self):
        print(f"{self.name}'s Progress:")
        for course, progress in self.progress.items():
            print(f"{course._name}: {progress}")


class Professor(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.courses = []

    def create_course(self, name, instructor, content, level):
        if level == "undergraduate":
            course = UnderGraduate(name, instructor, content, level)
        elif level == "graduate":
            course = Graduate(name, instructor, content, level)
        else:
            raise ValueError("Invalid course level")

        self.courses.append(course)
        print(f"{self.name} has created the course {course._name}")

    def assign_assignment(self, course, student):
        student.submit_assignment(course)
        print(f"{self.name} has assigned the assignment for {course.name} to {student.name}")


professor = Professor("John Smith", "jsmith@university.edu")
student1 = Student("Alice Brown", "abrown@university.edu")
student2 = Student("Bob Green", "bgreen@university.edu")

professor.create_course("Calculus", "Dr. Johnson", "Limits, derivatives, and integrals", "undergraduate")
professor.create_course("Computer Science", "Dr. Smith", "Data structures and algorithms", "graduate")

student1.enroll_course(professor.courses[0])
student2.enroll_course(professor.courses[1])

student1.view_progress()
student2.view_progress()
