import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 메인 페이지에서 검증해야 할 기능 (테스트 케이스 명세 참고 / expectedResult는 비로그인 vs 일반회원)
#  테스트 케이스 1. 쿠팡 상품 검색 기능
#  테스트 케이스 2. 장바구니 페이지 이동
#  테스트 케이스 4. 쿠팡 검색 필터 기능 (이거는 검색어 입력 및 결과 반환 후에만 가능한 듯? 메인페이지에 있기 애매한가?)
#  테스트 케이스 5. 판매자특가 페이지 이동
#  테스트 케이스 6. 최근 본 상품 기능

@pytest.mark.skip()
def test_open_main_page(mainPage):
    try:
        WebDriverWait(mainPage.driver, 10).until(EC.url_contains("coupang.com"))
        assert "coupang.com" in mainPage.driver.current_url
    except Exception as e:
        print(f"[❗] {e}")
        
@pytest.mark.skip()
@pytest.mark.parametrize("productName", ["노트북"])
def test_search_product(mainPage, productName): # 쿠팡 상품 검색 기능
    try:
        value = mainPage.searchProduct(productName)
        time.sleep(3)
        
        assert productName == value
    except Exception as e:
        print(f"[❗] {e}")

@pytest.mark.skip()    
def test_open_cart_page(mainPage): # 장바구니 페이지 이동
    try:
        mainPage.openCartPage()
        time.sleep(3)
        
        WebDriverWait(mainPage.driver, 10).until(EC.url_contains("cartView.pang"))
        assert "cartView.pang" in mainPage.driver.current_url
    except Exception as e:
        print(f"[❗] {e}")
  
@pytest.mark.skip()
def test_open_sellerSpecial_page(mainPage):
    try:
        mainPage.openSellerSpecialPage()
        time.sleep(3)
        
        WebDriverWait(mainPage.driver, 10).until(EC.url_contains("np/omp"))
        assert "np/omp" in mainPage.driver.current_url
    except Exception as e:
        print(f"[❗] {e}")