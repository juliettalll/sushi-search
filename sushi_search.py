from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://hisushi.pl/delivery/search")

accept_button=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Akceptuj")]'))
)
accept_button.click()

time.sleep(2)

search_input = driver.find_element(By.XPATH, '//input[@placeholder="Szukaj"]')
search_input.send_keys("burger krewetka")
search_input.send_keys()

time.sleep(3)

elements = driver.find_elements(By.XPATH, '//div[contains(@class, "CategoryItem_grid__b7rtC")]')
print("Кількість елементів після пошуку: ",len(elements))



check_name=driver.find_element(By.XPATH, '//div[contains(@class, "GridItem_title__Jo9AJ")]')
check_price=driver.find_element(By.XPATH,'//div[contains(@class, "styles_PriceDiscount__zS0u0 styles_PriceDiscountInline__Karf8")]')
print(f"Назва та ціна: {check_name.text}, {check_price.text}")



