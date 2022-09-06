x = 0
array = [1, 2 ,3]

while x < 1 or x > 10:
    x = int(input("give a number between 1 - 10: "))

print(x)
array.append(x)
print(array[1])