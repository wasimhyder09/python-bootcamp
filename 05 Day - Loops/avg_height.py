student_heights = input("Input a list of student heights ").split()

total_height = 0
counter = 0
for height in student_heights:
  total_height += int(height)
  counter += 1
average_height = total_height / counter
print(f"Average height: {round(average_height)}")