list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)


list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)