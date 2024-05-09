
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Tv(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for TV Page

    filter_manufacturer_1 = './/label[text()="ASANO"]/..'
    filter_manufacturer_2 = './/label[text()="BQ"]/..'

    button_apply_filters = '//button[@class="btn btn-primary btn-block"]'

    product_1 = '//div[@class="title"]/a[contains(text(), "ASANO 28LH7010T")]'
    product_1_add_cart = '//div[@class="add-cart-button"]//a[@data-id="47141"]'

    product_2 = '//div[@class="title"]/a[contains(text(), "BQ 40S03B Black")]'
    product_2_add_cart = '//div[@class="add-cart-button"]//a[@data-id="45387"]'

    button_close = '//*[@id="cart-modal"]/div/div/div[1]/button/span'
    
    min_price = '//input[@name="price-min"]' 
    max_price = '//input[@name="price-max"]'
    value_min_price = '10000'
    value_max_price = '50000'

    # Locators for Cart

    value_text_1_title = '//div[@class="title"]//a[@href="/catalog/product/asano-28lh7010t"]'
    value_text_2_title = '//div[@class="title"]//a[@href="/catalog/product/bq-40s03b-black"]'

    value_price_1 = ''
    value_price_2 = ''

    text_assert_1_cart = '//*[@id="cart-page"]/div/div[1]/div[1]/div[2]/div/a'
    text_assert_2_cart = '//*[@id="cart-page"]/div/div[1]/div[2]/div[2]/div/a'

    price_tv_1_cart = '//*[@id="cart-page"]/div/div[1]/div[1]/div[5]/div'
    price_tv_2_cart = '//*[@id="cart-page"]/div/div[1]/div[2]/div[5]/div'
    sum_price = '//*[@id="cart-page"]/div/div[1]/div[3]/div[3]/div'

    button_cart = '//*[@id="cart-modal"]/div/div/div[3]/a'

    plus_product_1 = '//*[@id="cart-page"]/div/div[1]/div[1]/div[4]/div/div/form/a[2]'
    plus_product_2 = '//*[@id="cart-page"]/div/div[1]/div[2]/div[4]/div/div/form/a[2]'

    minus_product_1 = '//*[@id="cart-page"]/div/div[1]/div[1]/div[4]/div/div/form/a[1]'
    minus_product_2 = '//*[@id="cart-page"]/div/div[1]/div[2]/div[4]/div/div/form/a[1]'
    
    # Getters for TV Page

    def get_filter_manufacturer_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer_1)))
    
    def get_filter_manufacturer_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer_2)))
    
    def get_button_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filters)))
    
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    
    def get_product_1_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_add_cart)))
    
    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))
    
    def get_product_2_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_add_cart)))
    
    def get_button_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close)))
     
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
    
    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))
    
    
    # Getters for Cart

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))
    
    def get_assert_text_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_assert_1_cart)))
    
    def get_assert_text_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_assert_2_cart)))
    
    def get_value_text_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_text_1_title)))
    
    def get_value_text_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_text_2_title)))
    
    def get_tv_price_1_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_tv_1_cart)))
    
    def get_tv_price_2_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_tv_2_cart)))
    
    def get_sum_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price)))
    
    def get_plus_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_product_1)))
    
    def get_plus_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_product_2)))
    
    def get_minus_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minus_product_1)))
    
    def get_minus_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minus_product_2)))

    # Actions for TV Page

    def click_tv_product_1(self):
        self.get_product_1().click()
        self.value_price_1 = self.parsing_price()
        print('Клик по продукту №1')

    def click_tv_product_2(self):
        self.get_product_2().click()
        self.value_price_2 = self.parsing_price()
        print('Клик по продукту №2')

    def click_product_1_add_cart(self):
        self.get_product_1_add_cart().click()
        print('Добавлен товар: ASANO 28LH7010T')

    def click_product_2_add_cart(self):
        self.get_product_2_add_cart().click()

    def click_button_close(self):
        self.get_button_close().click()
        print('Клик на кнопку "Закрыть"')

    def click_min_price(self):
        self.get_min_price().click()
        self.get_min_price().clear()
        self.get_min_price().send_keys(self.value_min_price)
        print('Установлена "Минимальная цена"')

    def click_max_price(self):
        self.get_max_price().click()
        self.get_max_price().clear()
        self.get_max_price().send_keys(self.value_max_price)
        print('Установлена "Максимальная цена"')

    def click_filter_manufacturer_1(self):
        self.get_filter_manufacturer_1().click()
        print('Выбран первый производитель в фильтре')

    def click_filter_manufacturer_2(self):
        self.get_filter_manufacturer_2().click()
        print('Выбран второй производитель в фильтре')

    def click_button_apply_filters(self):
        self.get_button_apply_filters().click()
        print('Клик на кнопку "Применить фильтры"')

    # Actions for Cart 
        
    def click_button_cart(self):
        self.get_button_cart().click()
        print('Клик на кнопку "Корзина"')
        
    def click_plus_product_1(self):
        self.get_plus_product_1().click()
        print('Плюс TV: ASANO 28LH7010T')

    def click_plus_product_2(self):
        self.get_plus_product_2().click()
        print('Плюс TV: BQ 40S03B Black')

    def click_minus_product_1(self):
        self.get_minus_product_1().click()
        print('Минус TV: ASANO 28LH7010T')

    def click_minus_product_2(self):
        self.get_minus_product_2().click()
        print('Минус TV: BQ 40S03B Black')  

    # Methods 

    def add_tv(self):
        with allure.step('Add tv'):
            Logger.add_start_step(method='add_tv')

            self.get_current_url() 

            # Фильтр "Производители"
            self.click_filter_manufacturer_1()  
            self.click_filter_manufacturer_2()
            self.get_screenshot('Фильтр №1 и №2 Производители')  

            # Фильтр "Цена"
            self.click_min_price() 
            self.click_max_price() 
            self.get_screenshot('Фильтр Цена')

            # Применяем фильтры
            self.click_button_apply_filters()

            # Заходим на страницы товаров и забираем цены (костыль т.к нет локаторов для сбора цен)
            self.click_tv_product_1()
            self.get_screenshot('TV ASANO 28LH7010T')
            self.driver.back()
            self.click_tv_product_2()
            self.get_screenshot('TV BQ 40S03B Black')
            self.driver.back()

            # Добавление товаров в корзину
            self.target_actions(self.get_product_1())
            self.click_product_1_add_cart()
            self.get_screenshot('Добавлен TV ASANO 28LH7010T')
            self.click_button_close()
            self.target_actions(self.get_product_2())
            self.click_product_2_add_cart()
            self.get_screenshot('Добавлен TV BQ 40S03B Black')
            time.sleep(2)          

            Logger.add_end_step(url=self.driver.current_url, method='add_tv')

    def cart_for_tv(self):
        with allure.step('Cart for tv'):
            Logger.add_start_step(method='cart_for_tv')

            self.click_button_cart()
            self.get_current_url() 
            self.assert_url('https://elmart-shop.ru/cart', 'Страница "Корзина"')
            self.get_screenshot('Товары в корзине')

            # Проверки
            self.assert_text_equal(self.get_assert_text_1(), self.get_value_text_1().text, "Название продукта")  # проверка текста продукта №1
            self.assert_text_equal(self.get_assert_text_2(), self.get_value_text_2().text, "Название продукта")  # проверка текста продукта №2
            self.assert_text_equal(self.get_tv_price_1_cart(), self.value_price_1, "Цена продукта")  # проверка цены продукта №1
            self.assert_text_equal(self.get_tv_price_2_cart(), self.value_price_2, "Цена продукта")  # проверка цены продукта №2
            self.assert_text_equal(self.get_sum_price(), str(int(self.value_price_1) + int(self.value_price_2)), "Сумма цен продукта")  # проверка суммы продуктов

            # Кнопка "+" для товаров внутри корзины
            self.click_plus_product_1()
            time.sleep(1)
            self.assert_text_equal(self.get_tv_price_1_cart(), str(int(self.value_price_1) * 2), "Цена продукта №1 X2")
            self.click_plus_product_2()
            time.sleep(1)

            # Проверки
            self.assert_text_equal(self.get_tv_price_2_cart(), str(int(self.value_price_2) * 2), "Цена продукта №2 X2")
            self.assert_text_equal(self.get_sum_price(), str((int(self.value_price_1) * 2) + (int(self.value_price_2) * 2)), "Сумма цен продукта X2")

            # Кнопка "-" для товаров внутри корзины 
            self.click_minus_product_1()
            time.sleep(1)
            self.click_minus_product_2()
            time.sleep(1)
            self.assert_text_equal(self.get_sum_price(), str(int(self.value_price_1) + int(self.value_price_2)), "Сумма цен продукта")

            Logger.add_end_step(url=self.driver.current_url, method='cart_for_tv')



        