from bs4 import  BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless  = False

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, 
						options=options)

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
# print(soup.prettify())

# search for table tag with class name
table = soup.find('table', class_ = 'chart')

# search for td tag with class name
for td in table.find_all('td', class_ = 'titleColumn'):
	print(td.text.strip().replace('\n','').replace('      ',''))






