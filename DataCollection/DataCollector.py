# This class will pull the data from the website
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from DataAccess.Write import WriteData
from DataAccess.Rules import DataAccessRules

from Recession import RecessionController


def open_webpage(website_url):
    driver.get(website_url)
    time.sleep(5)
    close_button = driver.find_element(By.CSS_SELECTOR, "button.box-flex.btn-close.p-absolute.r-lg")
    close_button.click()
    time.sleep(3)
    get_vendor_info()
    driver.quit()


def get_vendor_info():
    print('getting vendor info')
    vendor_info_container = driver.find_element(By.CSS_SELECTOR, "div.vendor-section")

    # Get Vendor Name
    vendor_info = vendor_info_container.find_element(By.CSS_SELECTOR, "div.box-flex.vendor-info-main.section-container.ai-start.fw-wrap")
    vendor_name_temp = vendor_info.find_element(By.TAG_NAME, 'h1')
    vendor_name = vendor_name_temp.text

    # Get Rating
    rating_info = vendor_info.find_element(By.ID, 'vendor-rating')
    rating_value = rating_info.find_element(By.TAG_NAME, 'span').text

    # Get Vendor Type
    vendor_type_info = vendor_info.find_element(By.TAG_NAME, 'ul')
    vendor_type_container = vendor_type_info.find_elements(By.CSS_SELECTOR, 'li.characteristic-list-item[data-testid=vendor-characteristic-list-item]')[0]
    vendor_type = vendor_type_container.find_element(By.TAG_NAME, 'span').text

    vendor_info = [vendor_name, rating_value, vendor_type]
    vendor_infos.append(vendor_info)

    rule_result = DataAccessRules.check_if_restaurant_already_searched(vendor_name)
    if rule_result[0] is True:
        print(rule_result[1])
        get_menus(vendor_name, rule_result[0])
        print(RecessionController.check_recession(vendor_datas))
        return
    else:
        print(rule_result[1])
        get_menus(vendor_name, rule_result[0])
        WriteData.write_to_restaurant_info_csv(vendor_infos)


def get_menus(restaurant_name, bool_result):
    print('getting the menu')

    time.sleep(5)
    menu = driver.find_element(By.ID, 'menu')
    sections = menu.find_elements(By.CSS_SELECTOR, "div.box-flex.dish-category-section.bg-white.mt-sm")

    for section in sections:
        item_list = section.find_element(By.TAG_NAME, 'ul')
        items = item_list.find_elements(By.TAG_NAME, 'li')
        for item in items:
            item_name = item.find_element(By.CSS_SELECTOR, 'span.vertical-align-middle[data-testid=menu-product-name]').text
            item_price = float(item.find_element(By.CSS_SELECTOR, 'p[data-testid=menu-product-price]').text.split(' ')[0].replace(',', '.'))
            item_info = [item_name, item_price, restaurant_name]
            vendor_datas.append(item_info)

    if bool_result is True:
        return
    else:
        WriteData.write_to_restaurant_menu_csv(vendor_datas)


vendor_infos = []
vendor_datas = []
firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options)
