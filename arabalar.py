
#  # arabalar=['BMW','OPEL','MERCEDES','MAZDA']
# # # result=len(arabalar)
# # # result=arabalar[0]
# # # arabalar[-1]='toyota'
# # # result=arabalar
# # # result='MERCEDES' in arabalar
# # # result='mercedes' in arabalar
# # # result=arabalar[-2]
# # # result=arabalar [0:3]
# # # arabalar[-2:]=['TOYOTA','RENAULT']
# # # result=arabalar
# # # result=arabalar+['audi','nissan']
# # del arabalar[-1]
# # result=arabalar
# # # print(result)
 

# # numbers=[1,10,5,16,4,9,10]
# # letters=[a,b,d,k,fr,g,j]

# # # val=min(numbers)
# # # val=max(numbers)
# # # val=numbers[3:6]
# # # numbers[4]=40
# # # numbers.append('49')
# # # numbers.insert(3,78)
# # # numbers.pop(0) --en sondaki eleman siliniyor
# # # letters.sort()kk
# # print(len(numbers))


# names=['Ali','Yağmur','Hakan','Deren']
# years=[1998,2000,1998,1987]
# # names.append('Cenk')  --Cenk ismini en sona allır append metodu
# # names.insert(0,'Sena')  -iinsert Sena ismini en başa aldı
# # names.remove('Deren')
# result='Aleyna' in names
# # print(names)

# sehırler=['Sivas','Kayseri']
# plakalar=[58,48]

# print(plakalar[sehırler.index('Sivas')])


# users={
#     'KevserFarımaz':{
#         'age':20,
#         'email':'Kevser@gmail.com',
#         'adress':'Sivas',
#         'phone':'123121123'
#     }
# }

# fruits={'orange','apple','banana'}
# # print(fruits)
# for x in fruits:
#     print(x)
# fruits.add('cherry')
# print(fruits)
# fruits.update(['mango','grape'])
# print(fruits)
# fruits.remove('mango')
# print(fruits)
# fruits.discard('apple')
# print(fruits)


# a=int(input('a: '))
# b=int(input('b:  '))
# result=(a > b)
# print(f'a: {a}b: {b} den büyüktür:{result}')

# vize1=float(input('1.vize: '))
# vize2=float(input('2.vize: '))
# final=float(input('final: '))
# ortalama=((vize1+vize2)*0.6)+(final*0.4)
# print(f'NOT ORTALAMANIZ:  {ortalama} VE DERTSN GEÇME DURUMUNUZ:{ortalama>=50}')
    

# email='email@kevserfarimaz.com' and password='abc1w23'
# girilenmail=input('email:')
# girilenpasssword=input('parola:')


# isim=input('isminiz: ')
# yas=int(input('yaşınız: '))        
# egitim=input('egitim: ')

# if (yas>=18):
#     if(egitim=='lise' or egitim=='üniversite'):
#         print(f'{isim} ehliyet alabilirsiniz')
#     else:
#         print(f'{isim} EHLİYET ALAMAZSINIZ,EĞİTİM DURUMUNUZ YETERSİZ')
# else:
#     print(f'{isim} ehliyet alamazsınız ,yaşını,yaşınız tutmuyor')


yazili1=float(input('1.yazılı: '))
yazili2=float(input('2.yazılı: '))
ortalama=(yazili1+yazili2)/2