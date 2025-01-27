import requests 
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
data=[]
for page in tqdm(range(1,11)):
    link      = 'https://quotes.toscrape.com/page/'+str(page)
    response  = requests.get(link)
    soup      = BeautifulSoup(response.text, 'html.parser')
    for sp in soup.find_all('div',class_='quote'):
        quote     = sp.find('span',class_='text').text[1:-1]
        author    = sp.find('small').text
        author_id = sp.find('a').get('href')
        tags=[]
        for tag in sp.find_all('a',class_=('tag')):
            tags.append(tag.text)
        tags      = ','.join(tags)
        data.append([quote, author, author_id, tags])
        print(quote,author,author_id,tags)
        print('-'*100)
df = pd.DataFrame(data, columns = ['quote','author','author_id','tags'])
df['author_link'] = 'https://quotes.toscrape.com'+df['author_id']
df.to_csv('Quotes_data.csv',index = False)
