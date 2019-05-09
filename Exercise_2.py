number = int(input("Enter an integer: "))
if number % 2 == 0 and number % 4 != 0:
    print("Normal")
elif number % 4 == 0:
    print("Weird but normal")
else:
    print("Thats weird")