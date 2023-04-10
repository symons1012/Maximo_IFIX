# adding code here to scrape IBM Maximo Asset Management Fix Central website for Maximo IFIXES

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_maximo_ifixes(url):
    '''
    A function to scrape Maximo IFIXes data from IBM Maximo Asset Management Fix Central website.
    '''
    # send a GET request to the URL and create a BeautifulSoup object
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # define the columns in the Excel sheet
    columns = ['IFIX Number', 'Release Date', 'Download Link']
    data = {column: [] for column in columns}
    
    # loop through the IFIX table rows and parse the data
    table_rows = soup.find_all('table', class_='fe-shop fw-resultstable')[0].find_all('tr')[1:]
    for row in table_rows:
        columns = row.find_all('td')[-3:]
        data['IFIX Number'].append(columns[0].text)
        data['Release Date'].append(columns[1].text)
        data['Download Link'].append(columns[2].find('a')['href'])
    
    # convert the dict item into a pandas dataframe
    df = pd.DataFrame(data)
    return df
