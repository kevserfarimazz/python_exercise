musteri=["0",0,0,0,0,0]
musteri[0]= input("müşterinin adını giriniz")
musteri[1]=int(input("müşterinin yaşını giriniz"))
musteri[2]=int(input("müşterinin borcunu giriniz"))
musteri[3]=int(input("indirim miktarını giriniz"))
musteri[4]=int(input("vergi oranını giriniz"))
musteri[5]=(musteri[2]-musteri[3])+((musteri[2]-musteri[3])*0.2)
print(musteri)