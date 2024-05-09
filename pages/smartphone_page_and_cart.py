
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Smartphone(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_model = None
        self.locator_model = None
        
    # Locators

    smartphone = './/div[text()="Смартфоны"]/..' 
    add_cart = '//*[@id="cart-add"]/button'
    button_cart = '//a[@class="btn btn-primary"]'
    button_apply_filters = '//button[@class="btn btn-primary btn-block"]'
    text_smartphone = '//div[@class="title"]//a'
    price_smartphone = '//*[@id="cart-page"]/div/div[1]/div[2]/div[3]/div'
    reset_filter = '//a[text()="сбросить фильтры"]'
    text_product_not_found = '//p[text()="Товары не найдены"]'
    value_text_product_not_found = 'Товары не найдены'

    # Getters
    
    def get_random_smart_model(self):
        self.locator_model, self.random_model, self.random_price = self.parsing_model_products()
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_model)))
        
    def get_filter_manufacturers(self):
        self.locator_filter, self.random_filter = self.parsing_filter_manufacturers()
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_filter)))
    
    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart)))
     
    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))
    
    def get_button_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filters)))
    
    def get_assert_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_smartphone)))
    
    def get_assert_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_smartphone)))
    
    def get_reset_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reset_filter)))
    
    def get_assert_not_found(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_product_not_found)))

    # Actions

    def click_smartphone_model(self):
        self.get_random_smart_model().click()
        

    def click_filter_manufacturers(self):
        self.get_filter_manufacturers().click()
        
        
    def click_add_cart(self):
        self.get_add_cart().click()
        print('Клик на кнопку "Добавить в корзину"')

    def click_button_cart(self):
        self.get_button_cart().click()
        print('Клик на кнопку "Корзина"')

    def click_button_apply_filters(self):
        self.get_button_apply_filters().click()
        print('Клик на кнопку "Применить фильтры"')

    def click_reset_filter_button(self):
        self.get_reset_filter().click()
        print('Клик на кнопку "Сбросить фильтры"')

    # Methods

    def add_smartphone(self):
        with allure.step('Add smartphone'):
            Logger.add_start_step(method='add_smartphone')

            try:
                self.get_current_url()

                # Выбираем и применяем фильтры
                self.click_filter_manufacturers() 
                self.get_screenshot('Рандомный фильтр "Производители"')
                self.click_button_apply_filters()

                # Выбираем смартфон
                self.click_smartphone_model()
                
                if self.random_model:
                    self.get_screenshot(self.random_model)

                    # Добавляем товар в корзину
                    self.click_add_cart()

            except  IndexError:
                print(f"Нет товаров производителя: {self.random_filter}")
                self.assert_text_equal(self.get_assert_not_found(), self.value_text_product_not_found, 'Проверка сообщения: "Товары не найдены"')
                self.get_screenshot('Товары не найдены')

                # Сброс фильтров
                self.click_reset_filter_button()

                # Выбираем смартфон
                self.click_smartphone_model()
                self.get_screenshot(self.random_filter)

                # Добавляем товар в корзину
                self.click_add_cart()
                time.sleep(2)

            Logger.add_end_step(url=self.driver.current_url, method='add_smartphone')

    def cart_for_smartphone(self):
        with allure.step('Cart for smartphone'):
            Logger.add_start_step(method='cart_for_smartphone')

            self.click_button_cart()
            self.assert_url('https://elmart-shop.ru/cart', 'Страница "Корзина"')
            self.get_screenshot('Смартфон в корзине')

            # Проверки
            self.assert_text_equal(self.get_assert_text(), self.random_model, 'Модель смартфона')
            self.assert_text_equal(self.get_assert_price(), self.random_price, 'Цена смартфона')

            Logger.add_end_step(url=self.driver.current_url, method='cart_for_smartphone')

        
