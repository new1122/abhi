import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*+-"

all = lower + upper + numbers + symbols
length = 6
password = "".join(random.sample(all, length))

print("Your Random Password is :" + password)