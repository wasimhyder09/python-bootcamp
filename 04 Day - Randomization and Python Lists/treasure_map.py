row1=["☐", "☐", "☐"]
row2=["☐", "☐", "☐"]
row3=["☐", "☐", "☐"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
col_row = input("Where do you want to put the treasure? ")
col = int(col_row[0])
row = int(col_row[1])

selected_row = map[row - 1]
selected_row[col - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")