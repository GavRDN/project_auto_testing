
import datetime
import os
from random import choice
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

 
class Base():

    def __init__(self, driver):
        self.driver = driver
        self.screenshot_path = None

    """Текущий URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий URL: {get_url}')

    """Проверка текста"""

    def assert_text_equal(self, value, result, name_assert):
        value = value.text
        assert value.lower() == result.lower()
        print(f'{name_assert}: {value}')
        print(f'{name_assert}: OK!')

    """Проверка URL"""

    def assert_url(self, result, name_page):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'Проверка URL {name_page}: OK')

    """Скриншот"""

    def get_screenshot(self, name):
        screen_path = os.path.join('screenshots', '')
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'{name} screenshot {now_date}.png'
        screenshot_full_path = os.path.join(screen_path, name_screenshot)
        self.driver.save_screenshot(screenshot_full_path)
        print(f'Скриншот: {name}')

    """Наведение курсора"""

    def target_actions(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()
        print('Навелся на товар')

    """Парсинг и рандомный выбор модели продукта"""

    def parsing_model_products(self):
        all_models = self.driver.find_elements(By.XPATH, '//div[@class="product-item"]')
        phone_dict = {}

        for el in all_models:
            title_element = el.find_element(By.XPATH, './/div[@class="title"]')
            price_element = el.find_element(By.XPATH, './/div[@class="price-current"]')
            
            key = title_element.text
            value = price_element.text
            phone_dict[key] = value

        random_model = choice(list(phone_dict.keys()))
        random_price = phone_dict[random_model]
        locator_model = f'//div[@class="title"]/a[contains(text(), "{random_model}")]' 
        print(f'Выбран продукт: {random_model}')
        print(f'Его цена: {random_price}')

        return locator_model, random_model, random_price
        
    """Парсинг и рандомный выбор в фильтре по производителю"""

    def parsing_filter_manufacturers(self):
        manufacturers = self.driver.find_elements(By.XPATH, '//div[@class="category-filter"]//label')
        manufacturers_list = []

        for el in manufacturers:
            manufacturers_list.append(el.text)

        random_manufacturer = choice(manufacturers_list)
        locator_filter = f'.//label[text()="{random_manufacturer}"]/..'
        print(f'Выбран фильтр производителя: {random_manufacturer}')

        return locator_filter, random_manufacturer
    
    """Парсинг городов на странице "Оформление заказа" """
    
    def parsing_city(self):
        cities = self.driver.find_elements(By.XPATH, '//select[@id="order-city"]/option')
        cities_list = []

        for el in cities:
            cities_list.append(el.text)

        random_city = choice(cities_list)
        locator_filter = f'//option[text()="{random_city}"]'
        print(f'Выбран город: {random_city}')

        return locator_filter

    """Выборка цены, т.к нет локаторов для цен"""

    def parsing_price(self):
        price_element = self.driver.find_element(By.XPATH, '//div[@class="price-current"]')
        price = price_element.text
        return price
 
        