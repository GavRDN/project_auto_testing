
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://elmart-shop.ru/'  
        
    # Locators

    signin_button = '/html/body/div[1]/nav/div/div[2]/ul/li[2]/a'
    catalog_button = '/html/body/div[1]/nav/div/div[1]/ul/li[2]/a'
    universal_catalog_button = '//a[@href="/catalogs/universal"]'

    # Getters

    def get_signin_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.signin_button))) 
    
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    
    def get_main_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_text)))

    # Actions

    def click_signin_button(self):
        self.get_signin_button().click()
        print('Клик на кнопку "Войти"')

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Клик на кнопку "Каталог"')

    # Methods
        
    def personal_area(self):
        with allure.step('Личный кабинет'):
            Logger.add_start_step(method='personal_area')

            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()  
            self.assert_url('https://elmart-shop.ru/', 'Главная страница')   
            self.click_signin_button()
            
            Logger.add_end_step(url=self.driver.current_url, method='personal_area')
        
    def go_in_catalog(self):
        with allure.step('Переход в каталог'):
            Logger.add_start_step(method='go_in_catalog')

            self.click_catalog_button()

            Logger.add_end_step(url=self.driver.current_url, method='go_in_catalog')
        
        