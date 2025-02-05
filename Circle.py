# Write a program to get radius of a circle. Then calculate and print the Area and the Perimeter of the circle.

import math

r = float(input("Please enter a number for the radius of the circle: "))
while r <=0:
    r = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))

perimeter = r * 2 * math.pi
area = r ** 2 * math.pi

print ("The perimeter of ​the circle is equal to: ", perimeter)
print ("The area of ​​the circle is equal to:", area)
