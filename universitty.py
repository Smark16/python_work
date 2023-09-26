class University():
    course = '',
    student = '',
    lecturer = ''

    def Student(self):
        print(f"My name is {self.student}")

    def Course(self):
        print(f"My course is {self.course}")

    def Lecturer(self):
        print(f"My lecturer is {self.lecturer}")

obj_1 = University()
obj_1.course = 'BSIT'
obj_1.student = 'SENGENDO MARK'
obj_1.lecturer = 'MR.KASOZI BRIAN'

#calling functions
obj_1.Student()
obj_1.Course()
obj_1.Lecturer()
