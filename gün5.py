sayilar=[81,2,3,4,5,6,7,8,913,15,21]

toplam=0
for i in sayilar:
    toplam+=i

sayilar=[81,2,3,4,5,6,7,8,913,15,21]

for i in sayilar:
    if (i%2==1):
        print(i**2)

sehirler=['izmit','sivas','samsun','amkara','trabzon']

for i in sehirler:
    if (len(i)<=6):
        print(i)