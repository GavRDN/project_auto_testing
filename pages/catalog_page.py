
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Catalog(Base):

    # Locators

    smartphone_and_other = './/div[text()="Смартфоны, телефоны, часы"]/..'
    smartphone = './/div[text()="Смартфоны"]/..' 

    tv_and_accessories = './/div[text()="Телевизоры и аксессуары"]/..'
    tv_33_48 = '//div[@class="col-lg-2 col-md-3 col-sm-3 col-xs-12 no-margin category-holder"]//a[@href="/catalog/category/televizory"]'

    appliances = './/div[text()="Бытовая техника"]/..'
    fridge = './/div[text()="Холодильники"]/..'

    beauty_and_health = './/div[text()="Красота и здоровье"]/..'
    hair_dryer = './/div[text()="Фены"]/..'

    # Getters

    def get_smartphone_and_other(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_and_other)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone)))
    
    def get_tv_and_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_and_accessories)))
    
    def get_tv_33_48(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_33_48)))
    
    def get_appliances(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.appliances)))
    
    def get_fridge(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fridge)))
    
    def get_beauty_and_health(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.beauty_and_health)))
    
    def get_hair_dryer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hair_dryer)))
    
    # Actions

    def click_smartphone_and_other(self):
        self.get_smartphone_and_other().click() 
        print('Выбрана категория: "Смартфоны, телефоны, часы"')

    def click_smartphone(self):
        self.get_smartphone().click() 
        print('Выбрана категория: "Смартфоны"')

    def click_tv_and_accessories(self):
        self.get_tv_and_accessories().click()
        print('Выбрана категория: "Телевизоры и аксессуары"')  

    def click_tv_33_48(self):
        self.get_tv_33_48().click()
        print('Выбрана категория: "Телевизоры 33-48"')

    def click_appliances(self):
        self.get_appliances().click()
        print('Выбрана категория: "Бытовая техника"')  

    def click_fridge(self):
        self.get_fridge().click()
        print('Выбрана категория: "Холодильники"')

    def click_beauty_and_health(self):
        self.get_beauty_and_health().click()
        print('Выбрана категория: "Красота и здоровье"')  

    def click_hair_dryer(self):
        self.get_hair_dryer().click()
        print('Выбрана категория: "Фены"')

    # Methods 
        
    def smartphone_catalog(self):
        with allure.step('Каталог смартфонов'):
            Logger.add_start_step(method='smartphone_catalog')
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/catalog', 'Страница "Каталог"')
            self.click_smartphone_and_other()
            self.click_smartphone()
            self.assert_url('https://elmart-shop.ru/catalog/category/mobil-nye-telefony', 'Страница "Смартфоны"')
            Logger.add_end_step(url=self.driver.current_url, method='smartphone_catalog')

    def tv_catalog(self):
        with allure.step('Каталог телевизоров'):
            Logger.add_start_step(method='tv_catalog')
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/catalog', 'Страница "Каталог"')
            self.click_tv_and_accessories()
            self.click_tv_33_48()
            self.assert_url('https://elmart-shop.ru/catalog/category/televizory', 'Страница "Телевизоры 33-48"')
            Logger.add_end_step(url=self.driver.current_url, method='tv_catalog')

    def fridge_catalog(self):
        with allure.step('Каталог холодильников'):
            Logger.add_start_step(method='fridge_catalog')
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/catalog', 'Страница "Каталог"')
            self.click_appliances()
            self.click_fridge()
            self.assert_url('https://elmart-shop.ru/catalog/category/holodil-niki', 'Страница "Холодильники"')
            Logger.add_end_step(url=self.driver.current_url, method='fridge_catalog')

    def hair_dryer_catalog(self):
        with allure.step('Каталог фенов'):
            Logger.add_start_step(method='hair_dryer_catalog')
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/catalog', 'Страница "Каталог"')
            self.click_beauty_and_health()
            self.click_hair_dryer()
            self.assert_url('https://elmart-shop.ru/catalog/category/feny', 'Страница "Фены"')
            Logger.add_end_step(url=self.driver.current_url, method='hair_dryer_catalog')

