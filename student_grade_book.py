student_name=["Jhon","Ana","David","Ema"]
student_score=[68,73,83,92]
sum=(68+73+83+92)
average=sum/4
minimum=min(student_score)
maximum=max(student_score)
student_grade_book=dict(zip(student_name,student_score))
input("Enter the name of the student to get their score:")
search_student_name=input()
if student_name=="Jhon":
    print("student name:")