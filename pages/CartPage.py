import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage():
    MAINPAGE_URL = "https://www.coupang.com/"
    CARTPAGE_URL = "https://cart.coupang.com/cartView.pang"
    SEARCH_INPUT_ID = "headerSearchKeyword"
    SEARCH_BUTTON_ID = "headerSearchBtn"
    SEARCH_PRODUCT_CSS_SELECTOR = "li.search-product"
    PROD_CART_BUTTON_CLASS = "prod-cart-btn" # "장바구니 담기" 버튼
    
    def __init__(self, driver):
        self.driver = driver
        
    def openMainPage(self):
        self.driver.get(self.MAINPAGE_URL)
        
    def searchProduct(self, productName):
        searchInputBox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.SEARCH_INPUT_ID)))
        searchInputBox.send_keys(productName)
        
        time.sleep(3)
        
        searchButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.SEARCH_BUTTON_ID)))  
        searchButton.click()
        
        time.sleep(3)
        
        return self.driver.find_element(By.ID, "headerSearchKeyword").get_attribute("value")
    
    def openCartPage(self):
        self.driver.get(self.CARTPAGE_URL)
        
    def getProductList(self):
        productList = []
        
        products = self.driver.find_elements(By.CSS_SELECTOR, self.SEARCH_PRODUCT_CSS_SELECTOR)
        for product in products:
            productID = product.get_attribute("id")
            productHREF = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            productList.append({"id": productID, "href": productHREF})
        
        return productList
        
    def addProductToCart(self):
        prodCartButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.PROD_CART_BUTTON_CLASS)))
        prodCartButton.click()