class student:
    def __init__(self, name, class_name, **marks):
        self.name = name
        self.class_name = class_name
        self.marks = marks

    def display_info(self):
        print("Student Name:", self.name)
        print("Class Name:", self.class_name)
        print("Marks:", self.marks)

s1 = student("Alice", "10A", Math=90, Science=85, English=88)
s1.display_info()