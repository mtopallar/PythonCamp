faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#type conversion
print(int(vade) + 12)
# print(int(krediAdi)) çevrilemeyeceği için hata verir.
print(type(str(faiz)))

#kullanıcıdan girdi alacağız:
vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: ")) #direk buradan da int e çevirebiliriz. tabi str değer girilirse dönüşüm hatası verir :)
print(type(vade)) #string python da input default olarak string değerine sahip olur.
vade = vade + 12

#string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade: numara
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade)) #bunun yerine;
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade)) #vaya
print("------------------------------------")

isim = "Halit"
metin = "Merhaba {name}".format(name = isim) #buradaki name = yerine direk bir string veya numerik bir değer verilebilir sorun yaratmaz.
print(metin)
print("------------------------------------")

#string interpolation 2 (f-string)
metin = f"Hoşgeldiniz {1+1}" #{} içinde python kodu da çalıştırılabilir değişken de çağrılabilir.
print(metin)
print("------------------------------------")

#listeler
dizi = ["İhtiyaç Kredisi", 10, 5.2]
print(dizi)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler)) #list

print(krediler)
print(krediler[0]) # => İhtiyaç Kredisi
# print(krediler[5]) => out of range
print(len(krediler)) #length (eleman sayısı index değil! indexten 1 fazla çıkar.)

krediler.append("Özel Kredi") #append sona ekliyor.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop() # son elemenı (veya verilen indexteki elemanı pop(1) gibi) siler.
krediler.pop(0) # 0 indexteki elemanı siler.
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi") #index değil de değer bazlı çalışır. index sırasına göre eşleşen ilk elemanı siler. Birden fazla varsa sadece birini siler. Bulamazsa hata verir.
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"]) # birden fazla elemanı listeye tek seferde ekler.
print(krediler)

#döngüler
#for döngüsü
print("------------------------------------")
# i=0 i<10

for i in range(10): #10 dahil değil i default 0. 10 yerine integer bir değişkenden veri de kullanılabilir.
    print(i)

print("------------------------------------")

for i in range(5,10): #5 den başla 10 a kadar (10 dahil değil)
    print(i)

print("------------------------------------")

for i in range(5,20,2): #5 den başla 20 ye kadar (20 dahil değil), 2 şer 2 şer atla
    print(i)

print("------------------------------------")

#for i in range(0.1,0.5): => hata verir. index integer olmalı float olmaz.
    #print(i)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

for kredi in krediler:
    print(kredi) #bu ve bir alttaki aynı çıktıyı verecek.

print("------------------------------------")

for i in range(len(krediler)):
    print(krediler[i]) #bu ve bir üstteki aynı çıktıyı verecek.

print("------------------------------------")

#while döngüsü

#syntax örneği - sonsuz döngü - ctrl c :)
#while True:
    #print("x")

i = 0
while i<10:
    print("x")
    i += 1
print("y")

print("------------------------------------")

while True:
    print("x")
    break # break döngüyü kırar.

print("------------------------------------")

i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break #ilk kredi olsaydı direk döngüden çıkardı.
    print(krediler[i])
    i += 1

print("------------------------------------")

j = 0
while j < len(krediler):
    j += 1 
    print(j)
    print(krediler[j])    
    #j += 1 
    if krediler[j] == "Konut Kredisi":
        break
    
# özetle while içinde yapılan işlemlerin yapılma sırası önemli.
   
#fonksiyonlar

print("------------ Fonksiyonlar ------------------")

fiyat = 100
indirim = 20

#definition - define / tanımlama
def calculate():
    print(100 - 20)

calculate()

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

calculateWithParams(100,30)

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("Halit")

def calculateAndReturn(price,discount):
    return price - discount
yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)