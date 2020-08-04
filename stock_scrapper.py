import pandas as pd
import requests

url_all = 'http://www.fundamentus.com.br/resultado.php'
url_stock = 'http://www.fundamentus.com.br/detalhes.php?papel='

request = requests.get(url_all)
print(request.content)