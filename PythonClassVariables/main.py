# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allows you to share data among all objects created from that class

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Kunal", 26)
student2 = Student("Haley", 26)
student3 = Student("Lexi", 22)
student4 = Student("Javi", 22)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

#print(student1.num_students)

#print(student1.name)
#print(student1.age)
#print(student1.class_year)
#print(Student.class_year) ## access via the class name for better readability
