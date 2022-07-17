# a=input("attendance")
# b=imput("hommework")
# c=input("exams")

# Answer=int((attandance+homework+Exam)/3)

# Textbox4.Tex ="The Answer=" & Answer & "The grade ia A "

# Textbox4.Text ="The Answer=" & Answer & "The grade ia B "

# Textbox4.Text="The Answer=" & Answer & "The grade ia c "


stu1=int(input("attandance:"))
stu2=int(input("homework:"))
stu3=int(input("exam:"))

sum=stu1+stu2+stu3
totalMarks=300
percentage=(sum/totalMarks) * 100
Avg=(sum/3)
print("percentage is ",percentage)
print("Average is ",Avg)