numbers=[x for x in range(10)]
print(numbers)

for i in range(10):
    print(i**2)
numbers=[i**2 for i in range(10) if i%3==0]
print(numbers)