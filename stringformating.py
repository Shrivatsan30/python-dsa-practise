def student_name(name,class_name,**marks):
    print("Student Name:", name)
    print("Class Name:", class_name)
    print("Marks:", marks)
    for x,y in marks.items():
        print(x,":",y)

student_name("John", 321, math=85, science=90, english=78, history= 92)

