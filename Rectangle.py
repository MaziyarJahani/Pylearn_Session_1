# Write a program to get width and height of a rectangle. Then calculate and print the Area and the Perimeter of the rectangle.

width = float(input("Please enter a number for the width of the rectangle: "))
while width <=0:
    width = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))

height = float(input("Please enter a number for the height of the rectangle: "))
while height <=0:
    height = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))

perimeter = (width + height) * 2
area = width * height

print ( "The perimeter of the rectangle is equal to: ", perimeter)
print ("The area of the rectangle is equal to: ", area)