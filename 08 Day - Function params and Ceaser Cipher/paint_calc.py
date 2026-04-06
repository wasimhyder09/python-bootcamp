import math

def paint_calc(height, width):
  total_paint = (wall_height * wall_width) / 5;
  print(f"Total paint cans required are {math.ceil(total_paint)}")

wall_height = int(input("Enter height of wall: "))
wall_width = int(input("Enter width of wall: "))
paint_calc(wall_height, wall_width)