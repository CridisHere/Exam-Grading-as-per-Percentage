#Write a program to accept the marks of a student in five subjects. Display total marks, percentage and grade as follow:
#≥85 : A
#≥75 : B
#≥50 : C
#≥30 : D
#<30 : Reappear

#Answer :

#Input maximum marks of all exams from the user
max_marks=int(input("What is the Total Marks of All Subjects : "))

#Input Marks for each subjects from the user
sub1=int(input("Marks of Subject 1 : "))
sub2=int(input("Marks of Subject 2 : "))
sub3=int(input("Marks of Subject 3 : "))
sub4=int(input("Marks of Subject 4 : "))
sub5=int(input("Marks of Subject 5 : "))

#Sum and Print the Total Marks Scored by User
total=sub1+sub2+sub3+sub4+sub5
print("You scored ", total,"marks out of", max_marks,"marks")

#Calculate and Print Total Percentage Scored by User
percentage=(total/max_marks)*100
print("You scored ", percentage,"%")

#Grade as per given in Question in beggining of the code
if percentage>=85:
    print("Grade : A")
elif percentage>=75:
    print("Grade : B")
elif percentage>=50:
    print("Grade : C")
elif percentage>=30:
    print("Grade : D")
elif percentage<30:
    print("Grade : Reappear")
else :
    print("Error") #Fallback code incase any error occurs

