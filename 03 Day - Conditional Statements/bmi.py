height = input("Enter your height (m): ")
weight = input("Enter your weight (kg): ")

bmi = int(weight) / float(height)**2
print(f"Your BMI is {round(bmi)}")
if(bmi <= 18.5):
  print("You are underweight")
elif(bmi > 18.5 and bmi < 25):
  print("You have normal weight")
elif(bmi >=25 and bmi < 30):
  print("You are overweight")
elif(bmi >= 30 and bmi < 35):
  print("You are obese")
else:
  print("You are clinically obese")