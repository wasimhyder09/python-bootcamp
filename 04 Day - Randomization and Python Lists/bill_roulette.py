import random

names = input("Give me list of names separated by comma: ")
people = names.split(", ")
length = len(people - 1)
print(length)
random_num = random.randint(0, length)

print(f"Today's bill will be paid by {people[random_num]}")