import pandas as pd

# pozisyonlara göre dataFrame döndürür
def getir(pozisyon,yıl):
    obje=pd.read_excel(yıl)
    kelime=obje['POZİSYON UNVANI']==pozisyon
    df=obje[kelime]
    return df
# benzersiz olan pozisyon isimimlerini liste olarak döndürür
def pozi(yıl):
    obje=pd.read_excel(yıl)
    sobje=obje['POZİSYON UNVANI'].unique()
    return sobje

#kategorilere ayrılmış olan dataFrameleri pozisyon ismine göre kaydeder.
for i in pozi("2021.xlsx"):
    
    obje1=getir(i,"2021.xlsx")
    string=str(i)+".xlsx"
    
    if (string=="İŞ VE UĞRAŞI TERAPİSTİ\n(ERGOTERAPİST).xlsx"):
        string="İŞ VE UĞRAŞI TERAPİSTİ.xlsx"
        obje1.to_excel(string)
        print(string+" kaydedildi")
    
    obje1.to_excel(string)
    print(string+" kaydedildi")



