import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    URL = "https://www.coupang.com/"
    SEARCH_INPUT_ID = "headerSearchKeyword"
    SEARCH_BUTTON_ID = "headerSearchBtn"
    CART_BUTTON_CLASS = "mycart-preview-module"
    SELLER_SPECIALS_XPATH = "//a[span[text()='판매자특가']]"
    
    def __init__(self, driver):
        self.driver = driver
    
    def openMainPage(self):
        self.driver.get(self.URL)
        
    def searchProduct(self, productName):
        searchInputBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.SEARCH_INPUT_ID)))
        searchInputBox.send_keys(productName)
        
        time.sleep(3)
        
        searchButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.SEARCH_BUTTON_ID)))  
        searchButton.click()
        
        time.sleep(3)
        
        return self.driver.find_element(By.ID, "headerSearchKeyword").get_attribute("value")
    
    def openCartPage(self):
        cartButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.CART_BUTTON_CLASS)))
        cartButton.click()
        
    def openSellerSpecialPage(self):
        sellerSpecialButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SELLER_SPECIALS_XPATH)))
        sellerSpecialButton.click()