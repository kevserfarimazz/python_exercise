results=[x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)

#iç içe iki dögü varsa böyleee
result =[]

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)


numbers=[(x,y)for x in range(3) for x in range(3) ]
print(numbers)