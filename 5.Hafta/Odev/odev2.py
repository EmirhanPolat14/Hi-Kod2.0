#• Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır.
# Format metodunu kullanılarak ekrana yazdırılır.

def faktoriyel(sayi):
    if sayi == 0:
        return 1
    elif sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)
    

sayi = int(input("Faktöriyelini öğrenmek istediğiniz sayıyı girin:"))

print("{} sayısının faktöriyeli {}'dir.".format(sayi,faktoriyel(sayi)))