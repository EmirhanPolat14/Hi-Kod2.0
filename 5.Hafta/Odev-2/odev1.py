#Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.
liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

# "3" değerine ulaşmak için indexleme yapın.
result = liste[3]
# "Hi-Kod" değerine ulaşmak için indexleme yapın.
result = liste[-3]
# 4.7 değerine ulaşmak için indexleme yapın.
result = liste[-1]
# 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
result = liste[2:6]
# 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
result = liste[4:-1]

print(result)