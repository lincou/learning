class Chinese:
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

class Teacher(Chinese):
    ...

Teacher1 = Teacher("Lihua",24,"tennis")
print(Teacher1.name)