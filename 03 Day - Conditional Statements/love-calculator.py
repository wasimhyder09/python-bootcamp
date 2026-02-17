print("Welcome to love calculator!")
name1 = input("What is your name \n").lower()
name2 = input("What is their name \n").lower()

count1 = 0
count2 = 0
combine_name = name1 + name2

# Count occurance of True
if(combine_name.count("t") > 0):
  count1 += combine_name.count("t")
if(combine_name.count("r") > 0):
  count1 += combine_name.count("r")
if(combine_name.count("u") > 0):
  count1 += combine_name.count("u")
if(combine_name.count("e") > 0):
  count1 += combine_name.count("e")


# Now count occurance of Love
if(combine_name.count("l") > 0):
  count2 += combine_name.count("l")
if(combine_name.count("o") > 0):
  count2 += combine_name.count("o")
if(combine_name.count("v") > 0):
  count2 += combine_name.count("v")
if(combine_name.count("e") > 0):
  count2 += combine_name.count("e")

final_count = int(str(count1) + str(count2))

if(final_count < 10 or final_count > 90):
  print(f"Your score is {final_count}% , you go together like coke and mentos")
elif(final_count >= 40 and final_count <= 50):
  print(f"Your score is {final_count}%, you are alright together.")
else:
  print(f"Your score is {final_count}%")