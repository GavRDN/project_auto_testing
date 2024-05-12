
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker
from utilities.logger import Logger


class Checkout(Base):

    fake = Faker()
    random_name = fake.first_name()
    random_lastname = fake.last_name() 
    random_phone_number = fake.random_number(digits=11)
    random_comment = fake.text()

    # Locators
          
    checkout_button = '//a[@class="le-button big"]'
    city_dropdown = '//select[@id="order-city"]'
    city = '//option[text()="Заринск"]' 
    first_name = '//input[@id="order-first-name"]'
    last_name = '//input[@id="order-last-name"]'
    phone_number = '//input[@id="order-phone"]'
    comment = '//textarea[@id="order-comment"]'
    plastic_card = '//*[@id="payment-area"]/div/div[2]/div'
    
    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_city_dropdown(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_dropdown)))
    
    def get_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.parsing_city())))
    
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    
    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))
    
    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))
    
    def get_plastic_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plastic_card)))
    
    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Клик на кнопку "Оформить"')

    def click_city_dropdown(self):
        self.get_city_dropdown().click()
        print('Клик на дропдаун списка городов')

    def click_city(self):
        self.get_city().click()

    def click_and_sand_first_name(self):
        self.get_first_name().click()
        self.get_first_name().clear()
        self.get_first_name().send_keys(self.random_name)
        print('Введено имя')

    def click_and_sand_last_name(self):
        self.get_last_name().click()
        self.get_last_name().clear()
        self.get_last_name().send_keys(self.random_lastname)
        print('Введена фамилия')

    def click_and_sand_phone_number(self):
        self.get_phone_number().click()
        self.get_phone_number().send_keys(self.random_phone_number)
        print('Введен номер телефона')

    def click_and_sand_comment(self):
        self.get_comment().click()
        self.get_comment().send_keys(self.random_comment)
        print('Введен текст комментария')

    def click_plastic_card(self):
        self.get_plastic_card().click()
        print('Выбрана оплата "Пластиковая карта"')

    # Methods
        
    def checkout(self):
        with allure.step('Оформление заказа'):
            Logger.add_start_step(method='checkout')
            self.click_checkout_button()
            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/cart/checkout', 'Страница "Оформление заказа"')

            # Выбор способа оплаты
            self.click_plastic_card()   

            # Выбор города
            self.click_city_dropdown()  
            self.click_city()  

            # Заполнение данных покупателя
            self.click_and_sand_first_name() 
            self.click_and_sand_last_name()  
            self.click_and_sand_phone_number()   
            self.click_and_sand_comment()  
            self.get_screenshot('Оформление заказа')  
            Logger.add_end_step(url=self.driver.current_url, method='checkout')

        