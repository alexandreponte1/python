class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")


student = ClassTest()

print(student.self)