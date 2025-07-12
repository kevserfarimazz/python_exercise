yorum = ['lara deniz','samet eke','dilan koç','faysal öz','rasim öztekin']

for kullanici in yorum:
    print("kullanici")

kullanicisayisi=0
for kullanici in yorum:    
    kullanicisayisi=kullanicisayisi + 1
    print(kullanicisayisi, kullanici)

yorum[1].split()

kullanicisayisi=0
for kullanici in yorum:    
    kullanicisayisi=kullanicisayisi + 1
    ad, soyad= yorum[0].split()[0], yorum[0].split()[1]
    print(kullanicisayisi,kullanici)