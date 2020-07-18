from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
import time


driver = webdriver.PhantomJS()
driver.set_window_size(1920, 1080)


for i in range(305, 364):  # Start page, End page
    url = "https://ebook.mirae-n.com/@kb3873/" + str(i)  # http://textbook-miraen.cdn.x-cdn.com/event/E-book_link.pdf
    driver.get(url)

    el = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//img[@src]")))
    WebDriverWait(driver, 10).until(lambda d: 'loading' not in el.get_attribute('class'))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    soup = soup.find("viewer-pdf-page")

    image = soup.findAll('img')[1]['src']
    urllib.request.urlretrieve(image, str(i) + '.jpg')

    print(str(i) + "페이지 완료")