from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
try:
  # Открываем веб-страницу
  browser.get("http://example.com")
  # Проверяем заголовок страницы
  assert "Example" in browser.title, "Заголовок страницы не содержит слово 'Example'"
  print("Заголовок содержит 'Example'")
  # Находим элемент по тексту "More information" и кликаем по нему
  try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "More information..."))
    )
    element.click()
    print("Кликнули на 'More information...'")

  except TimeoutException:
    print("Не удалось найти элемент 'More information...'")
    browser.quit()
    exit()
  #Проверяем URL после перенаправления
  try:
    WebDriverWait(browser, 10).until(
        EC.url_to_be("https://www.iana.org/help/example-domains")
        )
    assert browser.current_url == "https://www.iana.org/help/example-domains", f"URL не совпадает: {browser.current_url}"
    print("Перенаправление произошло успешно!")
  except TimeoutException:
    print("Перенаправление не произошло вовремя.")
finally:
  browser.quit()
  exit()