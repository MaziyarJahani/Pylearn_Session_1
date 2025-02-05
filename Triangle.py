# Write a program to get the size of three sides of a triangle and determines whether it is possible to draw such a triangle or not?
# Hint: The rule of the sides of a triangle is that the sum of the lengths of any two sides of a triangle is always greater than the length of the third side. This rule is also known as the triangle inequality theorem.

a = float(input("Please enter the desired value for the first side of the triangle: "))
while a <=0:
    a = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))


b = float(input("Please enter the desired value for the second side of the triangle: "))
while b <=0:
    b = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))


c = float(input("Please enter the desired value for the third side of the triangle: "))
while c <=0:
    c = float(input("Negative numbers and zero are not accepted, please enter a positive number: "))

if a + b > c and a + c > b and b + c > a:
    print("Yes, the triangle you are looking for can be drawn.")
else:
    print("No, the triangle you are looking for cannot be drawn.")
        
