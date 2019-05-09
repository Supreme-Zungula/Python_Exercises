#lists Divisors of a given number.

num = int(input("Enter a number: "))
divisors = []
count = 1
while count <= num / 2:
    if num % count == 0:
        divisors.append(count)
    count += 1
print(divisors)