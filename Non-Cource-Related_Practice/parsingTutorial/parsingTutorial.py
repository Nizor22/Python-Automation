from bs4 import BeautifulSoup
import requests

# ACCESS WEBSITES
#URL = 'https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAff8peBUNUVXTjNPNTBOMllaSVdETEVZR1RTQlY5Ni4u'
#html_file = requests.get(URL)
#soup = BeautifulSoup(html_file, 'lxml')
with open('simple.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')
#match = soup.find('input', class_='office-form-question-textbox office-form-textfield-input form-control border-no-radius')
article = soup.find('div', class_='article')
print(article)