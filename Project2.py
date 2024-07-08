# print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

#step 1-obtaining the marks
name=input("Enter your name: ")
english=float(input("Enter your english mark: "))
science=float(input("Enter your science mark: "))
math=float(input("Enter your math mark: "))
L2=float(input("Enter your Language 2 mark: "))
Social_Science=float(input("Enter your social science mark: "))

#step 2-printing the name and total
print(name,"has obtained the following results,")
total=english+science+math+L2+Social_Science
print("Your total marks are",total)

#step 3-calculating the average
avg=(english+science+math+L2+Social_Science)/5

#step 4-printing the results
if avg>90 and avg<=100:
    print("You've gotten A grade")
elif avg > 80 and avg <= 90:
    print("You've gotten B grade")
elif avg > 70 and avg <= 80:
    print("You've gotten C grade")
elif avg > 60 and avg <= 70:
    print("You've gotten D grade")
elif avg < 60:
    print("You've gotten E grade")