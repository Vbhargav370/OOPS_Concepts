class Student:
    def __init__(self, name, grade, skill, location):
        self.name = name
        self.grade = grade
        self.skill = skill
        self.location = location

    def student_data(self):
        print(f'Hello, {self.name}')
        print(f'Your grade is {self.grade}')
        print(f'Your skill is {self.skill}')
        print(f'You are from {self.location}\n')

t = int(input("Enter the number of students: "))
for i in range(t):
    name = input("Enter the name of the student: ")
    grade = float(input("Enter the grade of the student: "))
    skill = input("Enter the skill of the student: ")
    location = input("Enter the location of the student: ")
    std = Student(name, grade, skill, location)
    std.student_data()
