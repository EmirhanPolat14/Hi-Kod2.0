#Ödev-2: İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.

emirhan, hamdi, alperen = 23, 25, 28

result1 = emirhan > alperen
result2 = emirhan < hamdi
result3 = alperen > hamdi
result4 = emirhan < alperen and emirhan < hamdi
result5 = emirhan > alperen or emirhan < hamdi

print(result1,result2,result3,result4,result4)