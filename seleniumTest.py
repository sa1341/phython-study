from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISFTimeAnnStut.xml&divisionId=MDIS01002002000000&serviceId=SDIS01002002000')
sleep(10)


response = driver.find_elements(By.ID, 'grdMain_body_tbody')[0].text

result = list()
lines = response.split('\n')

for i in lines:
    result.append(i)

for i in result:
    print(i)

driver.quit()
