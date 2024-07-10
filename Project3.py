# Underweight:BMI less than 18.5
# Normal weight:BMI between 18.5 and 24.9
# Overweight:BMI between 25 and 29.9
# Obesity:
# Class I (Moderate obesity): BMI between 30 and 34.9
# Class II (Severe obesity): BMI between 35 and 39.9
# Class III (Very severe or morbid obesity): BMI of 40 and above

#step 1-obtaining information
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height(m): "))
weight=float(input("Enter your weight(kg): "))

#step 2-calculating and printing basic information
bmi=weight/(height**2)
bmi=round(bmi, 2)
print(name,"of age",age,"has a bmi of",bmi)

#step 3-calculating and printing data about bmi
if bmi >= 18.5 and bmi <= 24.9:
    print("Your bmi is normal")
elif bmi < 18.5:
    print("You are underweight")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight")
elif bmi >= 30:
    if bmi >= 30 and bmi <= 34.9:
        print("You have moderate obesity")
    elif bmi >= 35 and bmi <= 39.9:
        print("You have severe obesity")
    elif bmi >= 40:
        print("You have very severe or morbid obesity")