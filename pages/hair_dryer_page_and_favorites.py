
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Hair_dryer(Base):

    # Locators for Hair dryer Page

    product = '//div[@class="title"]/a[contains(text(), "Pioneer HD-1010")]'
    product_add_favorites = '//div[@class="wish-compare"]//a[@data-id="41456"]'

    button_close = '//*[@id="alertModal"]/div/div/div[3]/button'
    button_favorites = '//div[@class="wishlist "]'
    
    min_price = '//input[@name="price-min"]' 
    max_price = '//input[@name="price-max"]'
    value_min_price = '500'
    value_max_price = '1000'

    button_apply_filters = '//button[@class="btn btn-primary btn-block"]'

    # Locators for Cart

    product_text_catalog = 'Pioneer HD-1010'
    product_text_favorites = '//td[@class="hidden-xs"]//a[@href="/catalog/product/pioneer-hd-1010"]'

    text_favorites = '//div[@class="col-md-9 col-sm-8"]/h2'
    value_text_favorites = 'Список желаемых товаров'

    remove_product_favorites = '//a[@class="add-wishlist btn-toggle-wishlist"]'
    return_product_favorites = '//a[@class="add-wishlist btn-toggle-wishlist"]'

    empty_favorites = '//div[@class="col-md-9 col-sm-8"]/p'
    value_empty_favorites = 'Товары не найдены'
    
    # Getters for Hair dryer Page
    
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))
    
    def get_product_add_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_add_favorites)))
     
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
    
    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))
    
    def get_button_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filters)))
    
    # Getters for Favorites

    def get_button_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close)))
    
    def get_button_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_favorites)))
    
    def get_product_text_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text_catalog)))
    
    def get_product_text_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text_favorites)))
    
    def get_text_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_favorites)))

    def get_remove_product_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_product_favorites)))

    def get_empty_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_favorites)))

    # Actions for Hair dryer Page

    def click_product_add_favorites(self):
        self.get_product_add_favorites().click()
        print('Клик на кнопку "В избранное"')

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

    def click_button_apply_filters(self):
        self.get_button_apply_filters().click()
        print('Клик на кнопку "Применить фильтры"')
    
    # Actions for Favorites
        
    def click_button_close(self):
        self.get_button_close().click()
        print('Клик на кнопку "Закрыть модальное окно"')

    def click_button_favorites(self):
        self.get_button_favorites().click()
        print('Клик на кнопку "Избранное"')
        
    def click_remove_product_favorites(self):
        self.get_remove_product_favorites().click()
        print('Удален товар из избранных')  

    # Methods 

    def add_рair_dryer_favorites(self):
        with allure.step('Добавление товара в избранное'):
            Logger.add_start_step(method='add_рair_dryer_favorites')

            self.get_current_url()   

            # Фильтр "Цена"
            self.click_min_price() 
            self.click_max_price() 
            self.get_screenshot('Фильтр Цена')

            # Применяем фильтры
            self.click_button_apply_filters()

            # Добавление товаров в избранное
            self.target_actions(self.get_product())
            self.click_product_add_favorites()
            
            Logger.add_end_step(url=self.driver.current_url, method='add_рair_dryer_favorites')

    def favorites_for_рair_dryer(self):
        with allure.step('Страница "Избранное"'):
            Logger.add_start_step(method='favorites_for_рair_dryer')

            time.sleep(2)
            self.click_button_close()
            self.click_button_favorites()
            self.get_current_url() 
            self.assert_url('https://elmart-shop.ru/account/wishlist', 'Страница "Список желаемых товаров"')
            self.get_screenshot('Товар в списоке желаемых товаров')

            # Проверки
            self.assert_text_equal(self.get_product_text_favorites(), self.product_text_catalog, "Название продукта")  # проверка текста продукта

            # Удаление товаров из cписока желаемых товаров
            self.click_remove_product_favorites()
            self.get_screenshot('Неактивный товар')
            self.driver.refresh()

            # Проверка текста пустого списока желаемых товаров
            self.assert_text_equal(self.get_empty_favorites(), self.value_empty_favorites, "Проверка текста пустой корзины")

            Logger.add_end_step(url=self.driver.current_url, method='favorites_for_рair_dryer')

    
        