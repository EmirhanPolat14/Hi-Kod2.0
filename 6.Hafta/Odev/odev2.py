#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.

#değer değiştirme

dictionary = {"Emirhan":{"Matematik": 35, "Fizik":75, "Kimya":60 },
              "Hamdi":{"Matematik": 45, "Fizik":72, "Kimya":40 },
              "Alperen":{"Matematik": 85, "Fizik":77, "Kimya":33}}

dictionary["Alperen"]["Fizik"] = 45
print(dictionary)
#yeni değer ekleme
dictionary["Celal"] = {"Matematik": 15, "Fizik":56, "Kimya":84 }
print(dictionary)

#ulaşmak istenen değer

while True:
    print("\nKimin notlarını görmek istersin?" + "\n1.Emirhan" + "\n2.Hamdi" + "\n3.Alperen" + "\n4.Celal")

    kod = input("Kodu giriniz:")

    if kod == '1':
        print("\n***********************\n" + str(dictionary["Emirhan"]) + "\n***********************")
    elif kod == '2':
        print("\n***********************\n" + str(dictionary["Hamdi"]) + "\n***********************")
    elif kod == '3':
        print("\n***********************\n" + str(dictionary["Alperen"]) + "\n***********************")
    elif kod == '4':
        print("\n***********************\n" + str(dictionary["Celal"]) + "\n***********************")
    elif kod == 'q':
        break
    else:
        print("\nHatalı bir kod girdiniz!")

    print("\nÇıkmak için 'q'ya basınız...")




