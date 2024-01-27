"""Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. 
Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)"""

kulAd = input("Kullanıcı adınız:")
sifre = input("Lütfen bir şifre belirleyiniz:")

if len(sifre) >= 6:
    print("Hesabınız başarıyla oluşturulmuştur.")
else:
    print("Şifreniz en az 6 karakterden oluşmalıdır!")