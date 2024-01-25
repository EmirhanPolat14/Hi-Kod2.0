#Ödev-1: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

a, b, c, d = 45, 5.2, "25", True

print(f"a:{type(a)}\nb:{type(b)}\nc:{type(c)}\nd:{type(d)}\n")

a = float(a)
b = int(b)
c = int(c)
d = str(d)

print(f"a:{a,type(a)}\nb:{b,type(b)}\nc:{c,type(c)}\nd:{d,type(d)}\n")