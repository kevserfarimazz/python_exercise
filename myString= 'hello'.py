myString= 'hello'
myList=[]


for letter in myString:
    myList.append(letter)
print(myList)

myList=[letter for letter in myString]
print(myList)





years=[1999,1987,2988,1289,2617]
ages=[2019-year for year in years]
print(ages)