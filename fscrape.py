import copy
import pandas as pd
import requests
from lxml import html
url = 'https://cryptofundresearch.com/list-of-crypto-funds/'
page = requests.get(url).content
tree = html.fromstring(page)
rows = tree.xpath('//table[@id="tablepress-13"]//tbody//tr')
data = []
for row in rows:
    row = copy.copy(row)
    data.append(row.xpath('//td/text()'))
df = pd.DataFrame(data, columns=['Fund Name', 'City', 'Country', 'Launch Year', 'Type'])
df