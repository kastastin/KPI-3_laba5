from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def testSearch():
    searchWorld = 'book'

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)

    driver.get('https://www.moyo.ua/')
    driver.find_elements_by_css_selector('#search-input')[0].send_keys(searchWorld)
    driver.find_elements_by_css_selector('#search-input')[0].send_keys(Keys.ENTER)

    actualText = driver.find_elements_by_css_selector('.search_title span')[0].text
    expectedText = 'book'
    print(actualText)

    assert actualText == expectedText, 'Red test'
    # python -m pytest test.py

# testSearch()