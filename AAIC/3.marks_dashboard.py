# consider the marks list of class students given two lists 
# Students = ['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] 
# Marks = [45, 78, 12, 14, 48, 43, 45, 98, 35, 80] 
# from the above two lists the Student[0] got Marks[0],  Student[1] got Marks[1] and so on 
# your task is to print the name of students
# a. Who got top 5 ranks, in the descending order of marks
# b. Who got least 5 ranks, in the increasing order of marks
# d. Who got marks between  &gt;25th percentile &lt;75th percentile, in the increasing order of marks</strong>

def display_dash_board(students, marks):
    # write code for computing top top 5 students
    top_5_students = [j  for i,j in sorted(zip(marks,students),reverse=True)][:5]
    # write code for computing top least 5 students
    least_5_students = [j for i,j in sorted(zip(marks,students))][:5]
    # write code for computing top least 5 students
    sorted_list = sorted(zip(marks,students))
    N = len(students)
    students_within_25_and_75 = [sorted_list[i][1] for i in range(len(marks)) if i+1>(25/100)*N and i+1<(75/100)*N]
    
    return top_5_students, least_5_students, students_within_25_and_75

students = ['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10']
marks = [45, 78, 12, 14, 48, 43, 45, 98, 35, 80]

top_5_students, least_5_students, students_within_25_and_75 = display_dash_board(students, marks)
print(top_5_students,'\n',least_5_students,'\n',students_within_25_and_75)