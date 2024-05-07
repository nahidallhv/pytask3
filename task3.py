##print("Hello world")



class qus():
   
    sinif = "qus"
    
    def __init__(self, ad, yas, reng):
        self.ad = ad
        self.yas = yas
        self.reng = reng
        
    def ucabilme(self):
        return f"{self.ad} ucabiler"
    
    def yeriyebiler(self, yeriyebiler=False):
        if yeriyebiler:
            return f"{self.ad} yeriyebiler"
        else:
            return f"{self.ad} yeriyebilmez"


class surunen():
    
    sinif = "surunen"
    
    def __init__(self, ad, yas, reng):
        self.ad = ad
        self.yas = yas
        self.reng = reng
        
    def surunebilme(self):
        return f"{self.ad} surunebiler"
    
    def zeherleyebilme(self, zeherleyebilme=False):
        if zeherleyebilme:
            return f"{self.ad} zeherleyebiler"
        else:
            return f"{self.ad} zeherleyebilmez"


qaranqus = qus("qaranqus", 2, "qara")

kobra = surunen("kobra", 4, "sari")

print(f"{qaranqus.ad} {qaranqus.sinif} sinifine aiddir.")
print(f"{qaranqus.ad} {qaranqus.yas} yasindadir ve rengi {qaranqus.reng}.")
print(qaranqus.ucabilme())
print(qaranqus.yeriyebiler(True))

print(f"{kobra.ad} {kobra.sinif} sinifine aiddir.")
print(f"{kobra.ad} {kobra.yas} yasindadir ve rengi {kobra.reng}.")
print(kobra.surunebilme())
print(kobra.zeherleyebilme(True))
