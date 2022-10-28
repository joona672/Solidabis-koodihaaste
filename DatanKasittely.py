import json
import requests




class RuokaHahmot:
    
    def __init__(self, nimi, kalorit, proteiinit, hiilihydraatit, rasvat):
        self.nimi = nimi
        kalori = f'{kalorit:.1f}'
        self.kalorit = float(kalori)
        proteiini = f'{proteiinit:.1f}'
        self.proteiinit = float(proteiini)
        hiilihyd = f'{hiilihydraatit:.1f}'
        self.hiilihydraatit = float(hiilihyd)
        rasva = f'{rasvat:.1f}'
        self.rasvat = float(rasva)
        
    
    
def hae(*args):
    for j in range(1):
        #hakusana = input("Anna hakusana: ")
        
        adress = f'https://fineli.fi/fineli/api/v1/foods?q={args}'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34'}
        x = requests.get(adress, headers=headers)
        x1 = json.loads(x.text)

        for i in x1:
            hahmo = RuokaHahmot(i['name']['fi'],i['energyKcal'],i['protein'],i['carbohydrate'],i['fat'])
            varasto.lisaa_hahmo(hahmo)


        #print(x1[0]['id'])

        print(type(x1))
    
        
class Ruoat:
    def __init__(self):
        self.__ruoat = []

    def lisaa_hahmo(self, hahmo:RuokaHahmot):
        self.__ruoat.append(hahmo)
    
    def PalautaHahmot(self):
        return self.__ruoat
    
    def Tyhjenna(self):
        self.__ruoat.clear()
        
    def HaeValitutPelaajat(self, ruoka):
        pelaaja = {}
        for i in self.__ruoat:
            if ruoka == i.nimi.replace(" ","").replace("/", ""):
                pelaaja['nimi']= i.nimi
                pelaaja['kalorit'] = i.kalorit
                pelaaja['proteiinit'] = i.proteiinit
                pelaaja['hiilihydraatit'] = i.hiilihydraatit
                pelaaja['rasvat'] = i.rasvat
        print(pelaaja)
        
        return pelaaja        
        
        
        
varasto = Ruoat()