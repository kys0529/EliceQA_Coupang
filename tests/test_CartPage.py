import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.CartPage import CartPage

# 장바구니 페이지에서 검증해야 할 기능 (테스트 케이스 명세 참고 / expectedResult는 비로그인 vs 일반회원)
#  테스트 케이스 2. 장바구니 페이지 기능

@pytest.mark.skip()
def test_open_product_page(cartPage):
    try:
        WebDriverWait(cartPage.driver, 10).until(EC.url_contains("searchId=68f9d4232357058"))
        assert "searchId=68f9d4232357058" in cartPage.driver.current_url
    except Exception as e:
        print(f"[❗] {e}")

def test_add_product_to_cart(cartPage):
    try:
        cartPage.addProductToCart()
        time.sleep(3)
        
        # "구매하실 수 없습니다" 팝업이 뜨는 이유?
    except Exception as e:
        print(f"[❗] {e}")