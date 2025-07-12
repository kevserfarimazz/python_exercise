class ucgen:
    def __init__(self,acibir,aciiki,aciuc):
        self.acibir=acibir
        self.aciiki=aciiki
        self.aciuc=aciuc
    def kontrol(self):
        self.toplam=self.acibir+self.aciiki+self.aciuc
        if self.toplam==180:
            print("bu bir üçgendir. Açıların toplamı=",self.toplam)
        else:
            print("bu bir üçgen değildir. Açıların toplamı=", self.toplam)
            
ilk=ucgen(45,45,90)
ilk.kontrol()