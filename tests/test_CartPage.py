import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.CartPage import CartPage

# 장바구니 페이지에서 검증해야 할 기능 (테스트 케이스 명세 참고 / expectedResult는 비로그인 vs 일반회원)
#  테스트 케이스 2. 장바구니 페이지 기능

def test_open_product_page(cartPage):
    try:
        cartPage.searchProduct("노트북")
        time.sleep(3)
        
        WebDriverWait(cartPage.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, cartPage.SEARCH_PRODUCT_CSS_SELECTOR)))
        productList = cartPage.getProductList()
        time.sleep(3)
        
        cartPage.driver.get(productList[3]["href"]) # TODO: get(URL)은 안 되나? -> 클릭해서 페이지 접근하도록 변경?
        time.sleep(3)
        
        # TODO: 검증하기
        # WebDriverWait(cartPage.driver, 10).until()
        # assert
    except Exception as e:
        print(f"[❗] {e}")

@pytest.mark.skip()
def test_add_product_to_cart():
    try:
        pass
    except Exception as e:
        print(f"[❗] {e}")
        
@pytest.mark.skip()
def test_change_productNum_in_cart():
    try:
        pass
    except Exception as e:
        print(f"[❗] {e}")
        
@pytest.mark.skip()
def test_remove_product_from_cart():
    try:
        pass
    except Exception as e:
        print(f"[❗] {e}")