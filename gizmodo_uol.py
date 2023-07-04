import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)
navegador.get('https://gizmodo.uol.com.br')


lista_noticias = []


content = navegador.page_source
site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'list-item'})

for i in range(10):
    noticia = noticias[i]

    titulo = noticia.find('a', attrs={'rel': 'bookmark'})
    data = noticia.find('span', attrs={'class': 'metaText metaDate'})
    resumo = noticia.find('div', attrs={'class': 'postSummary entry-content'})

    print('Titulo da noticia:')
    print(titulo.text)
    print('----')
    print('data da notícia:')
    print(data.text)
    print('----')
    print('Resumo da notícia:')
    print(resumo.text)
    print('----')

    lista_noticias.append([titulo.text, data.text, resumo.text])

navegador.quit()


news = pd.DataFrame(lista_noticias, columns=['Título da notícia', 'data da notícia','Resumo da notícia'])

news.to_csv('noticias.csv', index=False)








