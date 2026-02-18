student_scores = input("Input a list of student scores ").split()

heighest_score = 0

for score in student_scores:
  if int(score) > int(heighest_score):
    heighest_score = score

print(f"Heighest score: {heighest_score}")