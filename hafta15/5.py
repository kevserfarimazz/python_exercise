# Bir otoparkta kullanıcının giriş saati, çıkış saati
# ve araç türüne göre saat ücretini belirten bir
#fonksiyon yazınız. taksi=1 ücreti 40 tl
# kamyonet=2, ücreti 60 tl, minibüs=3, 100

def borc(gs,cs,at):
    borc=0
    if at==1:
        borc=(cs-gs)*40
    elif at==2:
        borc=(cs-gs)*60
    elif at==3:
        borc=(cs-gs)*100
    print(borc)

borc(8,12,1)
borc(8,12,2)
borc(8,12,3)
