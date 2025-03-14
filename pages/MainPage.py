class MainPage():
    URL = "https://www.coupang.com/"
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)