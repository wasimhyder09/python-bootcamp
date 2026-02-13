print("Welcome to tip calculator")
bill = float(input("What is your total bill? $"))
tip = int(input("What percent tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

final_bill = round((bill + (bill * tip/100)) / people, 2)
final_amount = "{:.2f}".format(final_bill)

print(f"Each person should pay: ${final_amount}")