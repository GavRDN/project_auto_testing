
import allure
import time
from pages.catalog_page import Catalog
from pages.checkout_page import Checkout
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.tv_page_broken_locator import Tv_broken_locator

@allure.description('Негативный тест: покупка телевизора')

def test_negative_buy_tv():
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # Создание экземпляров страниц
    main_page = Main_page(driver)
    login_page = Login_page(driver)
    catalog_page = Catalog(driver)
    tv_page_and_cart = Tv_broken_locator(driver)
    checkout_page = Checkout(driver)


    try:
        print("Старт теста")

        # Шаг №1
        main_page.personal_area()

    except Exception as e:
        print("Ошибка на шаге 1:", e)
        raise e

    try:
        # Шаг №2
        login_page.authorization()
        time.sleep(2)

    except Exception as e:
        print("Ошибка на шаге 2:", e)
        raise e

    try:
        # Шаг №3
        main_page.go_in_catalog()

    except Exception as e:
        print("Ошибка на шаге 3:", e)
        raise e

    try:
        # Шаг №4
        catalog_page.tv_catalog()

    except Exception as e:
        print("Ошибка на шаге 4:", e)
        raise e

    try:
        # Шаг №5
        tv_page_and_cart.add_tv()

    except Exception as e:
        print("Ошибка на шаге 5:", e)
        raise e

    try:
        # Шаг №6
        tv_page_and_cart.cart_for_tv()

    except Exception as e:
        print("Ошибка на шаге 6:", e)
        raise e

    try:
        # Шаг №7
        checkout_page.checkout()

        print("Тест пройден")

    except Exception as e:
        print("Ошибка на шаге 7:", e)
        raise e
        
    finally:
        driver.quit()

