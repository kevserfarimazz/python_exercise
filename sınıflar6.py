class sinif:
    def __init__(self,arasinav,odev,final):
        self.arasinav=arasinav
        self.odev=odev
        self.final=final
    ortalama=0
    def hesapla(self):
        self.ortalama=((self.arasinav)*30/100)+((self.odev)*20/100)+((self.final)50*/100)
        print("öğrencinin ortalaması", self.ortalama)
        if self.ortalama>=5 and self.ortalama<=70:
            print("harf notunuz BB ")
        elif self.ortalama<=101 and self.ortalam>=70:
            print("harf notunuz= AA")
        elif self.ortalama<=45:
            print("harf notunuz DD")

Kevser = sinif(56,78,100)

Kevser.hesapla()