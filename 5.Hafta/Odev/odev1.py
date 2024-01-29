#• Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

def daireAlan(yariCap,pi):
    alan = (yariCap ** 2) * pi
    return alan

yariCap = float(input("Yarıçapı giriniz:"))
pi = float(input("Pi sayısı:"))

print(daireAlan(yariCap,pi))