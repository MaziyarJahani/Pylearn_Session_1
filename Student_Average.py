# Write a program to get a firstname, lastname and three course grade of a student. Then calculate the average of grades and print the student's academic status.

first_name = input ("Please enter your first name: ")
last_name = input ("Please enter your last name: ")

first_lesson = float(input("Please enter your first lesson grade: "))
while first_lesson < 0 or first_lesson > 20:
    first_lesson = float(input("Only numbers between 0 and 20 are accepted, please enter your first lesson grade: "))

second_lesson = float(input("Please enter your second lesson grade: "))
while second_lesson < 0 or second_lesson > 20:
    second_lesson = float(input("Only numbers between 0 and 20 are accepted, please enter your second lesson grade: "))

third_lesson = float(input("Please enter your Third lesson grade: "))
while third_lesson < 0 or third_lesson > 20:
    third_lesson = float(input("Only numbers between 0 and 20 are accepted, please enter your Third lesson grade: "))

average = (first_lesson + second_lesson + third_lesson) / 3

if average >= 17:
    status = "Honor Student"
    print("Congratulations", first_name, last_name, "\nYou are an excellent student")
elif average >= 12:
    status = "Regular Student"
else:
    status = "Probation Student"

print("Your status is:", status)
