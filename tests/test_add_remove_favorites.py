# import sys
# sys.path.append("E:\\finaly_project_el_market") # если не находит модули

import allure
import time
from pages.catalog_page import Catalog
from pages.checkout_page import Checkout
from pages.hair_dryer_page_and_favorites import Hair_dryer
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@allure.description('Test add and remove favorites')
def test_add_remove_favorites():
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # Создание экземпляров страниц
    main_page = Main_page(driver)
    login_page = Login_page(driver)
    catalog_page = Catalog(driver)
    hair_dryer_page_and_cart = Hair_dryer(driver)


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
        catalog_page.hair_dryer_catalog()

    except Exception as e:
        print("Ошибка на шаге 4:", e)
        raise e

    try:
        # Шаг №5
        hair_dryer_page_and_cart.add_рair_dryer_favorites()

    except Exception as e:
        print("Ошибка на шаге 5:", e)
        raise e

    try:
        # Шаг №6
        hair_dryer_page_and_cart.favorites_for_рair_dryer()

        print("Тест пройден")

    except Exception as e:
        print("Ошибка на шаге 6:", e)
        raise e
        
    finally:
        driver.quit()

