from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
chrome_driver_path = 'C:\Program Files (x86)\chromedriver.exe'

url = "https://en.wikipedia.org/w/index.php?search=&title=Special:Search"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
cService = webdriver.ChromeService(executable_path= chrome_driver_path)
driver = webdriver.Chrome(service = cService, options=options)

html = driver.page_source

driver.get(url)
search = driver.find_element(By.CLASS_NAME, 'oo-ui-inputWidget-input')
search.send_keys("fromsoftware")
search.send_keys(Keys.RETURN)


link = driver.find_element(By.LINK_TEXT, "Elden Ring")
link.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="firstHeading")
print(title.text)
json = json.dumps(title.text)
with open("sample.json", "w") as outfile:
    outfile.write(json)

driver.quit()