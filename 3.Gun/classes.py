from human import Human

# sınıflar (class)
# modules
# paket yönetimi

# class Human: (human.py ye taşıdık.)
#     #name = "Halit"
#     #built-in
#     def __init__(self,name): #ctor - initialize
#         self.name = name
#         print("Bir human instance ı üretildi.")
#     def __str__(self) -> str: #seri dönüş tipi
#         return f"STR fonksiyonundan dönen değer: {self.name}" #class direk print edilirse bu çalışıyor.
#     def talk(self,sentence):
#         print(f"{self.name}, {sentence}")        
#         #class içindeki name değişkenine direk ulaşamıyoruz. method gövdesi içinde bir name varsa direk erişebiliriz ancak class içindekine erişmek için self.name dememiz lazım.
#         # self.walk() aynı şekilde metod içinden metod çağırırken de self.metod adı şeklinde çağırmamız lazım.    
#     def walk(self):
#         print("Human is walking...")

#self parametresi python a özel bir keyword. diğer programlama dillerindeki this e karşılık gelir. bir class içinde tanımlanan her metod için ilk parametre self kelimesi için rezerve edilmiştir. isim self olmak zorunda değildir. bir parametre verilmek zorundadır. okuma kolaylığı ve community gelenekleri gereği self kullanılır.

#instance (örnek)
human1 = Human("Enes")
#human1.name = "Enes" (ctor içine alındı)
human1.talk("Bu direk sentencedir. Self olarak algılanmaz.")
human1.walk()
print(human1)

human2 = Human("Cem")
#human2.name = "Cem" (ctor içine alındı)
human2.talk("Merhaba")
human2.walk()
print(human2)
# nesneye genel değişkenleri metod parametresi olarak değil, class içinde değişken olarak tanımlamak isteriz. çünkü diğer fonksiyonlar da kullanır ve human ile ilgilidir. DRY!
