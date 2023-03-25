from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

#pytestte çalışan örneklere init ekleyemiyoruz. bu yüzden bu yapı pytest e uygun değil. pytest bunu test dosyası olarak görmesin diye dosyanın adını test_sauce iken sauce olarak değiştirdik. Bu sınıf manuel olarak çalıştırılabilir bir sınıf ancak pytest içinde çalışmaya uygun değil. manuel test örneği olarak bu örneği de sakladık.

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_invalid_login(self):        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) 
        #max 5 sn user-name elementi görünür olana kadar bekle. 5 saniye içinde görünmez ise akmaya devam eder.
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        #Hata mesajını görmek için hata elementini print ettik breakpoint koyup debug yaparak inceledik.
        #testResult = errorMessage.text == "HATALI GİRİŞ" #boolean false dönecek
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service" #boolean true dönecek.
        print(f"TEST: {testResult}")
        #sleep(100)
    
    def valid_login(self):    
        self.driver.get("https://www.saucedemo.com/")    
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))         
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) 
        passwordInput = self.driver.find_element(By.ID,"password")        
        #Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # userNameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()   
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)") #js kodu.
        sleep(20)
        



        

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.valid_login()