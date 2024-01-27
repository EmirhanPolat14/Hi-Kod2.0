"""Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.


 Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
 Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
 Tercihe göre kalan hak bilgisi verilir. """

kulAd = input("Kullanıcı adınız:")
pasS = "123456"
hak = 3
while True:

    sifre = input("Şifre:")
    if sifre == pasS:
        print("Giriş yapıldı.")
        break
    else:
        hak -= 1
        print(f"Yanlış şifre girildi! {hak} deneme hakkınız kaldı!")
        if hak <= 0:
            print("Hakkınız bitti...")
            break