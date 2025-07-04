name = input("Enter student name: ")
s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))
s4 = int(input("Enter marks for Subject 4: "))
s5 = int(input("Enter marks for Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print("\n🎓 Report Card")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")


name="ganesh"
maths=98
english=97
tamil=99
science=92
ip=100

subjects=maths+english+tamil+science+ip
total_percentage=subjects/500 *(100)
print("\n report card")
print("student name:",name)
print("total marks:",subjects,"/500")
print("total_percentage:",total_percentage,"%")