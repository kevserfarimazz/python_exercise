sayi=float(input('sayiyi giriniz:'))
result=(sayi > 0) and (sayi >= 100)
print=(f'sayi 0-100 arasında mı : {result}')





sayi=int(input('sayı:'))
(sayi>0) and (sayi%2==0)
print(f'çift mi {sayi:}')





vize1=float(input('vize 1:  '))
vize2=float(input('vize2:   '))
final=float(input('final:   '))
ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
result=(ortalama>=50) and final>=50
print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu {result}')







vize1=float(input('vize 1:  '))
vize2=float(input('vize2:   '))
final=float(input('final:   '))

ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
result=(ortalama>=50) or final>=70

print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu {result}')






kisiad=input('kullanıcınıın adı=')
kilosu=float(input('kullanıcınınkilosu='))
boyu=float(input('kullanıcının boyu='))
formül=(kilosu)/(boyu**2)

index=(kilosu)/(boyu**2)
zayif=(index>0)and (index<18.4)
normal=(index>18.4) and (index<=24.9)
kilolu=(index>=29.9) and (index<=34.9)
obez=(index<=29.9) and (index<=34.9)
print(f' {kisiad} kilo indeksin: {index} ve kilo değerlendirme: {zayif}')
print(f' {kisiad} kilo indeksin: {index} ve kilo değerlendirme: {normal}')
print(f' {kisiad} kilo indeksin: {index} ve kilo değerlendirme: {kilolu}')
print(f' {kisiad} kilo indeksin: {index} ve kilo değerlendirme: {obez}')


