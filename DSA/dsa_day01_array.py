numbers = [12, 7, 25, 3, 18, 9]

print(numbers)

print(numbers[2])

print(numbers[5])

if 18 in numbers:
    print("18 exists")
else:
    print("18 does not exist")
    
if 30 in numbers:
    print("30 exists")
else:
    print("30 does not exist")
    
numbers.remove(7)
    
numbers.append(50)
print(numbers)