havadurumu = "karli"
if havadurumu == 'yagisli':
    print("şemsiyeni al")
elif havadurumu == 'karli':
    print("atkını al")
else:
    print("sorun yok")

yas = 19
if yas >18:
   print("selam")
else:
    print("gre")

liste = ['a', 'b', 'c']


hedef_harf='d'
if hedef_harf in liste:
    print('buldum')
else:
    liste.append(hedef_harf)
    
    print('liste ekl')
    print('güncel list{}'.format(liste))



if (hedef_harf in liste) and (hedef_harf==liste[0]):
     print('buldum ve ilk harf konumunda')
elif hedef_harf in liste:
    print('buldum ve il konumda değil')
else:
    liste.append(hedef_harf)
    
    print('liste ekl')
    print('güncel list{}'.format(liste))

