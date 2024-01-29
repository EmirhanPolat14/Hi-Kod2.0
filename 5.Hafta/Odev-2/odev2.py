#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

yeni_liste = []
for i in liste:
    if i == str(i):
        yeni_liste.append(i)

print(yeni_liste)