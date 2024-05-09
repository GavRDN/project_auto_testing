
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Fridge(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for Fridge Page

    filter_manufacturer = './/label[text()="INDESIT"]/..'

    product = '//div[@class="title"]/a[contains(text(), "Indesit ES18")]'
    product_add_cart = '//*[@id="cart-add"]/button'
    
    min_price = '//input[@name="price-min"]' 
    max_price = '//input[@name="price-max"]'
    value_min_price = '5000'
    value_max_price = '70000'

    button_apply_filters = '//button[@class="btn btn-primary btn-block"]'

    # Locators for Cart

    product_text_catalog = '//div[@class="title"]//a[@href="/catalog/product/indesit-es18"]'

    value_price = ''

    product_text_cart = '//*[@id="cart-page"]/div/div[1]/div[1]/div[2]/div/a'

    price_cart = '//*[@id="cart-page"]/div/div[1]/div[1]/div[5]/div'

    button_cart = '//a[@class="btn btn-primary"]'

    remove_product = '//*[@id="cart-page"]/div/div[1]/div[1]/div[5]/a'

    empty_cart = '//*[@id="cart-page"]/div/h3'
    value_empty_cart = 'Корзина пуста'
    
    # Getters for Fridge Page

    def get_filter_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer)))
    
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))
    
    def get_product_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_add_cart)))
     
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
    
    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))
    
    def get_button_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filters)))
    
    # Getters for Cart

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))
    
    def get_product_text_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text_cart)))
    
    def get_product_text_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text_catalog)))
    
    def get_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_cart)))
    
    def get_remove_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_product)))
    
    def get_empty_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart)))

    # Actions for Fridge Page

    def click_product(self):
        self.get_product().click()
        self.value_price = self.parsing_price()
        print('Клик по продукту')

    def click_product_add_cart(self):
        self.get_product_add_cart().click()
        print('Клик на кнопку "В корзину"')

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

    def click_filter_manufacturer(self):
        self.get_filter_manufacturer().click()
        print('Выбран производитель в фильтре')

    def click_button_apply_filters(self):
        self.get_button_apply_filters().click()
        print('Клик на кнопку "Применить фильтры"')
    
    # Actions for Cart
        
    def click_button_cart(self):
        self.get_button_cart().click()
        print('Клик на кнопку "Корзина"')
        
    def click_remove_product(self):
        self.get_remove_product().click()
        print('Удален товар из корзины')
    

    # Methods 

    def add_fridge(self):
        with allure.step('Add fridge'):
            Logger.add_start_step(method='add_fridge')

            self.get_current_url() 

            # Фильтр "Производители"
            self.click_filter_manufacturer()  
            self.get_screenshot('Фильтр Производители')  

            # Фильтр "Цена"
            self.click_min_price() 
            self.click_max_price() 
            self.get_screenshot('Фильтр Цена')

            # Применяем фильтры
            self.click_button_apply_filters()

            # Заходим на страницу товара
            self.click_product()
            self.get_screenshot('Indesit ES18')

            # Добавление товара в корзину
            self.click_product_add_cart()
            self.get_screenshot('Добавлен Indesit ES18T')
            time.sleep(2)
            
            Logger.add_end_step(url=self.driver.current_url, method='add_fridge')

    def cart_for_fridge(self):
        with allure.step('Cart for fridge'):
            Logger.add_start_step(method='cart_for_fridge')

            self.click_button_cart()
            self.get_current_url() 
            self.assert_url('https://elmart-shop.ru/cart', 'Страница "Корзина"')
            self.get_screenshot('Товары в корзине')

            # Проверки
            self.assert_text_equal(self.get_product_text_cart(), self.get_product_text_catalog().text, "Название продукта")  # проверка текста продукта           
            self.assert_text_equal(self.get_price_cart(), self.value_price, "Цена продукта")  # проверка цены продукта
            
            # Удаление товаров из корзины
            self.click_remove_product()
            self.get_screenshot('Пустая корзина')

            # Проверка текста пустой корзины
            self.assert_text_equal(self.get_empty_cart(), self.value_empty_cart, "Проверка текста пустой корзины")

            Logger.add_end_step(url=self.driver.current_url, method='cart_for_fridge')

    
        