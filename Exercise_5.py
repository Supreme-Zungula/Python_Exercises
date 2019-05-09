a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commons = []

for n in a:
    if n in b:
        if n in commons:
                continue
        else:
                commons.append(n)

print(commons)