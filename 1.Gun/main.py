# değişken tipi belirtmeye veya noktalı virgüle gerek yok. Indent mantığı ile çalışıyor.
print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
# int, integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"
# vade + 2 => 38 yaparken
# vade2 + 2 => 38 yapmaz :)

# float, decimal, double => ondalıklı sayı
aylikOdeme = 200.50

# bool, boolean => true / false
yukselisteMi = True  # ilk harf büyük

# matematiksel operatörler
# +
print(10 + 5)
print(vade + 4)
print(vade + ekVade)

# -
print(10 - 5)
print(vade - 4)
print(vade - ekVade)

# *
print(10 * 5)
print(vade * 4)
print(vade * ekVade)

# / (sonuçları float olarak gösteriyor tam sayı olsa bile)
print(10 / 5)
print(vade / 4)
print(vade / ekVade)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod operatörü % (iki sayının birbirine bölenden kalan)
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatörler (karşılaştırma operatörleri)
print(1 == 1)  # True
print(1 == 2)  # False

print(1 > 2)  # False
print(3 > 2)  # True
print(1 > 1)  # False
print(1 >= 1)  # True

print(1 < 1)
print(1 <= 1)

print(1 != 3)  # True
print(1 != 1)  # False

# or / and
print(1 > 2 or 5 > 2)  # True
print(1 > 2 and 5 > 2)  # False
print(1 > 2 or 5 > 2 and 3 > 2)  # True
print(1 > 2 and 5 > 2 and 1 > 2)  # False
print(2 > 1 or 1 > 2 and 3 > 2)  # True

# karar yapıları
# if else (elif)

sayi1 = 10
sayi2 = 15
# sayi1 sayi2 den büyükse eksaran sayi 1 daha büyük yazdır.

# indent
if sayi1 < sayi2:
    print("Sayı 1 küçüktür.")
elif sayi1 == sayi2:
    print("Sayılar eşittir.")
# eğer if ve elif bloklarından hiç birine girmezse çalışır
else:
    print("Sayı 1 sayı 2 den büyüktür.")
print("Burası if bloğunun dışıdır.")