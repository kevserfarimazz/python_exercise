liste = ['a','b','c']
hedef_harf='k'
if hedef_harf in liste:
    print('buldum')
else:
    liste.append(hedef_harf)
    print('lsteye ekledim')
    print('güncel liste {}'.format(liste))


