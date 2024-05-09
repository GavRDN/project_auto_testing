
import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = '//*[@id="login-email"]'
    password = '//*[@id="login-pass"]'
    login_button = '//*[@id="authentication"]/div/div/div/section/form/div[4]/button'
    main_text = '//*[@id="section-auth"]/h1'
    
    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    
    def get_login_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    
    def get_main_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_text)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Введен логин')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Введен пароль')

    def click_login_button(self):
        self.get_login_button_enter().click()
        print('Клик на кнопку "Войти"')

    # Methods
        
    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')

            self.get_current_url()
            self.assert_url('https://elmart-shop.ru/login', 'Страница входа')
            self.input_user_name("gavr050588@gmail.com")
            self.input_password("Qwe112233")
            self.click_login_button()
            self.get_screenshot("Вход")
            
            Logger.add_end_step(url=self.driver.current_url, method='authorization')
        

        