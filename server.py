import random
fd = open("test.txt", "r")
lines = fd.readlines()
print(random.choice(lines))
fd.close()
