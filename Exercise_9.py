import random

condition = ""
while condition != 'exit':
    num = random.randint(1, 10)
    while True:
        guess = input("Guess a number from 1 to 9 or enter exit to quit: ")
        if guess == 'exit':
            condition = guess
            break
        elif int(guess) < num:
            print("Too low")
        elif int(guess) > num:
            print("Too high")
        else:
            print("Exactly right")
            break