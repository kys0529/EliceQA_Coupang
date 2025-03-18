from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage():
    URL = "https://cart.coupang.com/cartView.pang"
    PRODUCT_URL = "https://www.coupang.com/vp/products/7975088162?itemId=22105168560&vendorItemId=89152120239&pickType=COU_PICK&q=%EB%A7%A5%EB%B6%81+%EC%97%90%EC%96%B4&itemsCount=36&searchId=68f9d4232357058&rank=1&searchRank=1&isAddedCart="
    PROD_CART_BUTTON_CLASS = "prod-cart-btn"
    
    def __init__(self, driver):
        self.driver = driver
        
    def openProductPage(self):
        self.driver.get(self.PRODUCT_URL)
    
    def openCartPage(self):
        self.driver.get(self.URL)
        
    def addProductToCart(self):
        prodCartButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.PROD_CART_BUTTON_CLASS)))
        prodCartButton.click()