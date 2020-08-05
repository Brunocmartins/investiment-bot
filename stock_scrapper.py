import pandas as pd
import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def get_data() -> pd.DataFrame:
    """Function that makes request from Fudamentus and get the data from
    current brazilian stocks.

    Returns
    -------
    pd.DataFrame
        DataFrame containing data from all active stocks traded in B3
    """

    url_all = 'http://www.fundamentus.com.br/resultado.php'

    agent = {'User-Agent': 'Mozilla/5.0'}
    source = requests.get(url_all, headers=agent)

    stocks = pd.read_html(source.content, index_col='Papel')[0]
    # Remove rows without liquidity in the past 2 months
    stocks = stocks[stocks['Liq.2meses'] != '000']

    return stocks

def get_stock(stock: str) -> pd.DataFrame:
    """

    Parameters
    ----------

    Returns
    -------
    """

    url_stock = 'http://www.fundamentus.com.br/detalhes.php?papel='
    agent = {'User-Agent': 'Mozilla/5.0'}

    req = Request(url_stock+stock, headers=agent)
    response = urlopen(req)
    # Read response as bytes
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    oscil = soup.findAll('span', {'class': 'oscil'})
    data = list()
    for item in oscil_data:
        data.append(item.get_text())

    oscil_label = soup.findAll('td', {'class': 'label w1'})
    index = list()
    for label in oscil_label:
        index.append(label.findAll('span', {'class': 'txt'}))

    pass

if __name__ == '__main__':
    get_data()
    get_stock('VVAR3')