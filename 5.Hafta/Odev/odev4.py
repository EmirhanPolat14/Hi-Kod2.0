import datetime
#• Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
#(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
#(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" 
#yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." 
#yanıtını versin.

isim = input("İsminiz:")
doğumYılı = int(input("Doğum yılınız:"))

def yasHesapla(doğumYili):
    now = datetime.datetime.now().year
    return now - doğumYili   

def emeklilik(dy,ad):
    yas = yasHesapla(dy)
    if yas >= 65:
        return "Emekli oldunuz"
    else:
        return f"{ad} kişisinin emekliliğine {65 - yas} yıl kaldı."

print(emeklilik(doğumYılı,isim))
