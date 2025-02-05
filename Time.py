# Write a program to get a hour, minute and second of a time. Then convert it to seconds and print it.

hours = int(input("Please enter a number for the hour: "))
while hours < 0:
    hours = int(input("Negative numbers are not accepted, please enter a positive integer: "))

minutes = int(input("Please enter a number for the minute: "))
while minutes < 0:
    minutes = int(input("Negative numbers are not accepted, please enter a positive integer: "))

seconds = int(input("Please enter a number for the second: "))
while seconds < 0:
    seconds = int(input("Negative numbers are not accepted, please enter a positive integer: "))

seconds = hours * 3600 + minutes * 60 + seconds

print("Total seconds:",seconds)

