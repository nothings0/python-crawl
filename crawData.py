from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quizlet.com/vn/518558389/fruit-flash-cards/")

sleep(20)
data = driver.find_elements(By.CLASS_NAME,"SetPageTerms-term")
for item in data:
    prompts = item.find_elements(By.CLASS_NAME, "SetPageTerm-wordText")
    for i in prompts:
        prompt = i.find_element(By.CLASS_NAME, "TermText")
        print('{"prompt": "',prompt.text,'"', sep='')
    terms = item.find_elements(By.CLASS_NAME, "SetPageTerm-definitionText")
    for j in terms:
        term = j.find_element(By.CLASS_NAME, "TermText")
        print(',"answer": "',term.text,'"},', sep='')
sleep(5)
driver.close()