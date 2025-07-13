"""user story : taking grades as inputs from the student
   A(90-100) ,B(80-89),C(70-79),D(60-69),E(50-59),F(>50)
   """
name=str(input("Enter student name:"))
rollnumber=int(input("Enter roll number :"))
subject1=int(input("Enter subject1 Marks :"))
subject2=int(input("Enter subject2 Marks :"))
subject3=int(input("Enter subject3 Marks :"))
subject4=int(input("Enter subject4 Marks :"))
subject5=int(input("Enter subject5 Marksa :"))
#marks to grade
def marks_to_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <90:
        return "B"
    elif 70 <= mark <80:
        return "C"
    elif 60 <= mark <70:
        return "D"
    elif 50 <= mark <60:
        return "E"
    else:
        return "F"
marks=[subject1,subject2,subject3,subject4,subject5]
grades=list(map(marks_to_grade,marks))
#enumerate() gives both index and grade
for i,grade in enumerate(grades , start=1):
    print(f" subject {i} Grade : {grade}")
#function to calculate total
def total(*args):
    return subject1+subject2+subject3+subject4+subject5
totalMarks=total(subject1,subject2,subject3,subject4,subject5)
print("Total marks obtained : ",totalMarks)
#function to calculate average marks
def average(totalMarks):
    return totalMarks/5
Average =average(totalMarks)
print("Percentage obtained {} %".format(Average))
#if else for grades
if (Average>=90 and Average<=100):
    grade="A"
elif(Average>=80 and Average<90):
    grade="B"
elif(Average>=70 and Average<80):
    grade="C"
elif(Average>=60 and Average<70):
    grade="D"
elif(Average>=50 and Average<60):
    grade="E"
else:
    grade="F"
#match case for giving grade
match grade:
    case "A"|"B"|"C"|"D"|"E"|"F":
        print("Total Grade obtained : {} ".format(grade))
   
    case _:
        print("***********************************")
    

