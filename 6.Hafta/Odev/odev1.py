# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. 
#Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

dictionary = {"Emirhan":{"Matematik": 35, "Fizik":75, "Kimya":60 },
              "Hamdi":{"Matematik": 45, "Fizik":72, "Kimya":40 },
              "Alperen":{"Matematik": 85, "Fizik":77, "Kimya":33}}

isim = input("İsim giriniz:")
ders = input("Dersin adını giriniz:")

print(dictionary[f"{isim}"][f"{ders}"])
