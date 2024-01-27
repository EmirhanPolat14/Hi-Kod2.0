"""Ödev-3: Bir önceki örnek geliştirilir.


 Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. 
 Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
 Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
 Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder """

kulAd = input("Kullanıcı adınız:")

while True:

    sifre = input("Lütfen bir şifre belirleyiniz:")

    if len(sifre) >= 5 and len(sifre) <= 10:
        print("Hesabınız başarıyla oluşturulmuştur.")
        break
    else:
        print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")


