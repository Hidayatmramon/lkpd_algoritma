a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

if (a >= b) and (a >= c):
    terbesar = a
elif (b >= a) and (b >= c):
    terbesar = b
else:
    terbesar = c

print("Bilangan terbesar dari ketiga bilangan tersebut", terbesar)
