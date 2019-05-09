import datetime

curr_year = datetime.datetime.now().year
name = input("Enter your name: ")
age = input("Enter your age: ")
number = int(input("Enter a number: "))

year100 = curr_year + (100 - int(age))

while number > 0:
    print("Hi {0}, You will turn 100 in {1}.".format(name, year100))
    number -= 1