from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

#isim karmaşasına dikkat. Kullanılacak modül ile anynı isimli dosya oluşturmayı tercih etmeyiz.
# selenium; kabaca bir tarayıcıda yaptığımız işlemlerin otomatize edilmesini sağlayan bir yapıdır.Bir test otomasyonudur.
# selenium python ile çalışmak zorunda değildir. Örneğin Java veya C# ile de kullanılabilir.
# selenium a chrome driver kuracağız. adres https://chromedriver.chromium.org/downloads ilgili kinkten chrome versiyonuna uygun olanı indirmeliyiz. (ilk 3 hane yeterli) Bu işlem selenium a kullanması için chrome u vermek gibi düşünülebilir.

#chrome driver ı yükleyebilmek için:
#1) chrome driver ı çalışan py dosyası ile aynı dizine atmak,
#2) chromedriver ın adresini driver = webdriver.Chrome("chromedriver.exe nin adresi")
#3) pip install webdriver-manager paketini yükledik. driver = webdriver.Chrome(ChromeDriverManager().install()) ile kullanabiliyoruz. bu ilgili driver ı indirip yolunu kendisi handle ediyor. Bu tercih edilen yöntem çünkü otomatik indirip yolu kendi ayarlıyor. Çoklu test ortamında da bu işlemlerin otomatik olması tercih edilir.

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com.tr/")
sleep(5) # sayfa tam yüklensin, elemanı bul, rahat rahat bul ki içine yazı yazabilelim.
input = driver.find_element(By.NAME,"q") #name ve id form için unique alanlardır. (id her türlü unique dir) *
#print(f"Input: {input}")
input.send_keys("kodlama.io") #input alanına yazı yazdıracağız. *
searchButton = driver.find_element(By.NAME,"btnK")
print(searchButton)
sleep(2)
searchButton.click() # sleep olmadan erişilemiyor hatası veriyor. Bu seleniumda önemli ve dikkat edilmesi gereken bir durumdur:*
sleep(2)
#firstResult = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a") #yukarıdaki ya da bu ikisi de çalışır.
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing") #class name i course-listing olan elementlerin listesini getirir.
print(f"Kodlama.io sitesinde şu anda {len(listOfCourses)} adet kurs var.")

#sleep(10) => #10 saniye kodu bekletir.
while True:
    continue

# HTML LOCATORS
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a  => full xpath index mantığı yok. rakam direk hedefi gösterir. xpath ler de güvenilir sayılır ancak güncelleme ile bir mesela div vs eklenir veya çıkarılırsa xpath yenilenmek durumunda kalır.
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a   => xpath (full değil) en yakın unique alandan başlar.
#find_element ilgili locator ile bulunan ilk elementi geri döner, tek bir element döner.
#  find_elements ile ilgili locator ile bulunan elementlerin listesini döner.
# data scraping ya da web scraping - veri kazıma :) kodlamaio da 7 adet kurs olduğunu bize bir endpoint ya da api söylemedi, biz kodlamaio üzerindeki verileri sayarak bunu selenium a buldurduk. kabaca bu işleme veri kazıma deniyor.