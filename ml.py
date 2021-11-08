# exemplo
# - obtendo produtos e precos do mercado livre a partir de uma busca realizada pelo usuario

import requests
from bs4 import BeautifulSoup
from requests.models import Response
import pandas

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto voce deseja buscar?')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={
    'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})
    real = produto.find('span', attrs={'class': 'price-tag-fraction'})

    # print(produto.prettify())
    print('Titulo do produto:', 'Link do produto:', 'Preco do produto' titulo.text)
    print('Link do produto:', link['href'])
    print('Preco do produto: R$', real.text)

product = pandas.DataFrame
