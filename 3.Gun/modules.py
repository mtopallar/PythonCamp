# Aşağıdaki importların hepsi geçerli.
# import matematik as m  burada m alias. m.topla() diye kullanabiliriz. vermek zorunda değiliz. vermezsek matematik.bol() diye kullanırız.
from matematik import topla #mesela sadece toplama işlemine ihtiyaç duyarsak bu şekilde sadece onu import edebiliriz.
#from matematik import topla,bol
# from matematik import topla as toplamaIslemi, bol as bolmeIslemi
from human import Human
import random #built-in modul
#dışarıdan package
from selenium import webdriver

#sonuc = m.topla(6,3)
sonuc = topla(6,9)
print(sonuc)

print(random.randint(0,100)) #0 ve 100 dahil :)

#dosya = modül
human1 = Human("Mirza")
human1.talk("Merhaba")

#packages
#diğer developerların hazırladı kodları paket olarak nitelendiriyoruz.
# https://pypi.org/project/pip/   => python package yönetim sistemi
# terminale pip enter yaparak test ettik. pip çalışıyor mu diye :)

chromeDriver = webdriver.Chrome()