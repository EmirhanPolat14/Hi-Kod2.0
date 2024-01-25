"""Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.


 İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir. 
 İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ") 
 İfadeyi hepsini büyük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi") 

"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")"""

baslik = "Hi-Kod Veri Bilimi Atölyesi"
bol =baslik.split()
print(bol)

buyuk_harf = baslik.upper()
print(buyuk_harf)

kucuk_harf = baslik.lower()
print(kucuk_harf)

sayi = "0123456789"
cift_sayi = sayi[::2]
tek_sayi = sayi[1::2]
print(f"Çift sayılar: {cift_sayi}\nTek sayılar: {tek_sayi}")