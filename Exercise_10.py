# List overlap comprehensions
import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
print([elem for elem in a if elem in b])