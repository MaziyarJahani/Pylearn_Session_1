# Add the following features to the calculator program: sqrt ( √ ), sin, cos, tan, cot, factorial
# Note: some functions such as `sin` or `tan` in Python receive the angle in radians. You must write a code to convert degrees to radians for these functions.
import math

while True:
    operator = int(input("Please enter the number of the mathematical operation you want. \nSquare Root (enter 1) \nSine (enter 2) \nCosine (enter 3) \nTangent (enter 4) \nCotangent (enter 5) \nFactorial (enter 6) \nExit (enter 7) \nYour operation: "))
    if operator == 1 :
        number = float(input("Enter a number for square root: "))
        if number < 0:
                print("Error: Negative input for square root")
        else:
                print("Result:", math.sqrt(number))
    
    elif operator == 2 :
        degrees = float(input("Enter an angle in degrees for sine: "))
        radians = math.radians(degrees)
        print("Result:", math.sin(radians))
    
    elif operator == 3 :
        degrees = float(input("Enter an angle in degrees for cosine: "))
        radians = math.radians(degrees)
        print("Result:", math.cos(radians))
    
    elif operator == 4 :
        degrees = float(input("Enter an angle in degrees for tangent: "))
        if degrees == 90 or degrees == 270:
            print("Error: Tangent is undefined at 90° and 270°")
        else:
            radians = math.radians(degrees)
            print("Result:", math.tan(radians))
    
    elif operator == 5 :
        degrees = float(input("Enter an angle in degrees for cotangent: "))
        if degrees == 0 or degrees == 180:
            print("Error: Cotangent is undefined at 0° and 180°")
        else:
            radians = math.radians(degrees)
            tan_value = math.tan(radians)
            print("Result:", 1 / tan_value)

    
    elif operator == 6 :
        number = int(input("Enter a number for factorial: "))
        if number < 0:
            print("Error: Factorial is not defined for negative numbers")
        else:
            print("Result:", math.factorial(number))

    elif operator == 7:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")        