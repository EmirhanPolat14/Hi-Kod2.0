import datetime
#• Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

now = datetime.datetime.now().year

def yasHesapla(doğumYili):
    return now - doğumYili   

doğumyili = int(input("Doğum yılınızı giriniz:"))
print(f"Yaş:{yasHesapla(doğumyili)}") 


