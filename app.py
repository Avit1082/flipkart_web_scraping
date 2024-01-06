import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
def web_scrape_flipkart_mobiles(query):
    base_url = f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=88'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        mobiles = []
        for mobile in soup.find_all('a', {'class': '_1fQZEK'}):
            price = mobile.find('div', {'class': '_30jeq3' }).text.strip()
            name = mobile.find('div', {'class': '_4rR01T'}).text.strip()
            rating = mobile.find('div', {'class': '_3LWZlK'}).text.strip()
            mobiles.append({'Name': name, 'Price': price, 'Rating': rating})
        # print(mobiles)
        return mobiles
    else:
        print(f'Error: {response.status_code}')
        return None

query = 'iPhone'
filename = 'flipkart_mobiles.csv'
mobiles_data = web_scrape_flipkart_mobiles(query)
if mobiles_data:
    df=pd.DataFrame.from_records(mobiles_data)
    df.to_csv(filename,index=False)
    print(f'Data saved to {filename}')
else:
    print('Failed to scrape data from Flipkart.')
