import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.MainPage import MainPage
from pages.CartPage import CartPage

@pytest.fixture(scope="function")
def CreateDriver():
    
    chromeService = Service()
    chromeOptions = Options()
    
    chromeOptions.add_argument("--start-maximized")
    
    # 1) User-Agent 변경
    chromeOptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")
    # 2) SSL 인증서 에러 무시
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--ignore-ssl-errors")
     # 4) Selenium이 automation된 브라우저임을 숨기는 몇 가지 설정
    #    - (disable-blink-features=AutomationControlled) 제거
    #    - excludeSwitches, useAutomationExtension
    chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeOptions.add_experimental_option("useAutomationExtension", False)
    # 혹은 다음 방식으로 Blink 특징을 비활성화할 수도 있으나
    # "AutomationControlled" 자체가 표기되지 않도록 한다.
    chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
    # 6) Sandbox나 DevShm 사이즈 문제 우회 (리눅스 환경에서 발생 가능)
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
    
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.coupang.com/"}})
    
    print("🛠️ WebDriver 생성!")
    
    yield driver
    
    print("\n🛠️ WebDriver 종료!")
    
    driver.quit()
    
@pytest.fixture(scope="function")
def mainPage(CreateDriver):
    mainPage = MainPage(CreateDriver)
    print("📦 MainPage 클래스 객체 생성!")
    
    mainPage.openMainPage()   
    print("🌍 쿠팡 메인 페이지 오픈!")
    
    time.sleep(3)
    
    return mainPage

@pytest.fixture(scope="function")
def cartPage(CreateDriver):
    cartPage = CartPage(CreateDriver)
    print("📦 CartPage 클래스 객체 생성!")
    
    cartPage.openProductPage()
    print("🌍 상품 페이지 오픈!")
    
    time.sleep(3)
    
    return cartPage