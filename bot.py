#устанавливаем нужные библиотеки beautifulsoup для парсинга, request для отправки запросов на сайт
import requests
from bs4 import BeautifulSoup
#указываем ссылку на сайт к которому будем обращаться
url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#дэфолтный get запрос, тут даже скаать нечего (он нужен скорее для создания соединения между клиентом и сервером)
response = requests.get(url)
#lxml получает полностью все данные html страницы (попробуйте просто написать print (fullresponse))
fullresponse = BeautifulSoup(response.text, 'lxml')
#из полученной страницы мы вытаскиваем нужные нам данные
request = fullresponse.find_all('td', class_='exrate')
#это хуйня колхозное, не буду объяснять
print("USD/KGS ", request[1].text)
print("EUR/KGS ", request[3].text)
print("RUB/KGS ", request[5].text)
print("KZT/KGS ", request[7].text)
