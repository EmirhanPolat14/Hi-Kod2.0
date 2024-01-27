"""Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır.
 Kullanıcının geliri;


 10000 ve altındaysa maaşından %5 kesinti olur. 
 25000 ve altındaysa maaşından %10 kesinti olur. 
 45000 ve altındaysa maaşından %25 kesinti olur. 
 Diğer koşullarda %30 kesinti olur. 

Bu durumlara göre kullanıcının yeni maaşı yazdırılır."""

maas = float(input("Maaşınızı Giriniz:"))

if maas <= 10000:
    print(f"Vergi kesildikten sonra maasınız {maas - maas * 0.05} TL'dir ")
elif maas > 10000 and maas <= 25000:
    print(f"Vergi kesildikten sonra maasınız {maas - maas * 0.10} TL'dir ")
elif maas > 25000 and maas <= 45000 :
    print(f"Vergi kesildikten sonra maasınız {maas - maas * 0.25} TL'dir ")
else:
    print(f"Vergi kesildikten sonra maasınız {maas - maas * 0.30} TL'dir ")