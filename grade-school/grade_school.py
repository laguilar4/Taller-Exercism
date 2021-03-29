class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append((name,grade))

    def roster(self):
        self.students.sort(key=lambda x: (x[1], x[0]))
        return [name for name, _ in self.students]

    def grade(self, grade_number):
        self.students.sort(key=lambda x: (x[1], x[0]))
        return [name for name, grade in self.students if grade == grade_number]
