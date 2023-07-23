import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium import webdriver
from write_results import *

options = webdriver.ChromeOptions()
chrome_driver_path = "http://chromedriver.storage.googleapis.com/114.0.5735.16/chromedriver_linux64.zip"
# chrome_driver_path = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.98/linux64/chromedriver-linux64.zip"
ser = Service(chrome_driver_path)
browser = webdriver.Chrome(service=ser, options=options)
temp = ''


def launch_weather_shopper():
    print('Opening Weather Shopper page')
    try:
        browser.get("http://weathershopper.pythonanywhere.com")
        print(browser.title)
        if 'Current Temperature' in browser.title:
            my_worksheet.write('B3', 'Passed', passed_format)
        else:
            my_worksheet.write('B3', 'Failed', failed_format)
        time.sleep(2)
        html_data = browser.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        temp_var = soup.find("span", id="temperature")
        if temp_var != '':
            my_worksheet.write('B4', 'Passed', passed_format)
        else:
            my_worksheet.write('B4', 'Failed', failed_format)
        print(temp_var.text)
        if len(temp_var.text) == 5:
            final_temp = temp_var.text[0:3].strip()
        else:
            final_temp = temp_var.text[0:2].strip()
        print(final_temp)
        select_item(int(final_temp))
    except Exception as e:
        print('Exception occurred')
        my_workbook.close()


def select_item(final_temp):
    if final_temp < 19:
        print('Calling Moisturiser')
        add_cheap_items_to_cart('Moisturiser', 'Buying Moisturiser', 'https://weathershopper.pythonanywhere.com'
                                                                     '/moisturizer')
        my_worksheet.write('B5', 'Passed', passed_format)

    elif final_temp > 34:
        print('Calling sunscreen')
        add_cheap_items_to_cart('Sunscreen', 'Buying Sunscreen', 'https://weathershopper.pythonanywhere.com'
                                                                 '/sunscreen')
        my_worksheet.write('B8', 'Passed', passed_format)
    else:
        print('Enjoy the weather!!!')


def add_cheap_items_to_cart(call_data, print_text, url_data):
    print(print_text)
    browser.get(url_data)
    time.sleep(2)
    html_data = browser.page_source
    if call_data == 'Moisturiser':
        my_worksheet.write('B8', 'NA', na_format)
        my_worksheet.write('B9', 'NA', na_format)
        my_worksheet.write('B10', 'NA', na_format)

        find_cheap_item('aloe', html_data)
        my_worksheet.write('B6', 'Passed', passed_format)
        find_cheap_item('almond', html_data)
        my_worksheet.write('B7', 'Passed', passed_format)
    else:
        my_worksheet.write('B5', 'NA', na_format)
        my_worksheet.write('B6', 'NA', na_format)
        my_worksheet.write('B7', 'NA', na_format)

        find_cheap_item('spf-50', html_data)
        my_worksheet.write('B9', 'Passed', passed_format)
        find_cheap_item('spf-30', html_data)
        my_worksheet.write('B10', 'Passed', passed_format)


def find_cheap_item(keyword, html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    temp_var = soup.find_all("button", class_="btn btn-primary")
    items_filtered = []
    counter = 0
    current_price = 0
    price_counter = 0
    for i in temp_var:
        if keyword in str(i).lower():
            price_data = str(i)[str(i).find(",") + 1:str(i).find(")")]
            items_filtered.append(i)
            if int(current_price) != 0:
                if int(current_price) > int(price_data):
                    current_price = int(price_data)
                    price_counter = int(counter)
            else:
                current_price = price_data
            counter = int(counter) + 1
    button_found = items_filtered[int(price_counter)]
    browser.execute_script("javascript:" + button_found['onclick'] + "")


launch_weather_shopper()
try:
    browser.execute_script("javascript:goToCart()")
    time.sleep(3)
    my_worksheet.write('B11', 'Passed', passed_format)
except:

    print('Problem occured while opening the cart')
    my_worksheet.write('B11', 'Failed', failed_format)
finally:
    my_workbook.close()
    browser.close()