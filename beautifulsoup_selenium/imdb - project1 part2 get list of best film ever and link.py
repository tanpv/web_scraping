from bs4 import BeautifulSoup
from selenium import webdriver


def get_movies():

	options = webdriver.ChromeOptions()
	options.headless  = False

	chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
	driver = webdriver.Chrome(executable_path=chrome_driver_path, 
							options=options)

	url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'

	driver.get(url)

	# print driver.page_source

	soup = BeautifulSoup(driver.page_source,'lxml')

	table = soup.find('table', class_ = 'chart')

	movies = []

	for td in table.find_all('td', class_ = 'titleColumn'):
		
		full_title = td.text.strip().replace('\n','').replace('      ','')
		print(full_title)

		rank = full_title.split('.')[0]
		print(rank)

		title = full_title.split('.')[1].split('(')[0]
		print(title)

		year = full_title.split('(')[1][:-1]
		print(year)

		a = td.find('a')
		print(a['href'])

		print('\n')

		movie = {}
		movie['rank'] = rank		
		movie['title'] = title
		movie['year'] = year
		movie['link'] = a['href']

		movies.append(movie)

	driver.quit()
	
	return movies


movies = get_movies()

for mv in movies:
	print(mv['title'])
	print(mv['rank'])
	print(mv['year'])
	print(mv['link'])


