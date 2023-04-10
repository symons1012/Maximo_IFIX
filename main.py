import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def extract_links(page_html):
    link_list = []
    soup = BeautifulSoup(page_html, 'html.parser')
    link_tables = soup.find_all('table', {'class': 'tborder_grey'})
    for table_index in range(len(link_tables)):
        if 'HF' in link_tables[table_index].text and 'IF' in link_tables[table_index].text:
            for row in link_tables[table_index].find_all('tr'):
                fix_dict = {}
                col_index = 0
                for col in row.find_all('td'):
                    if '.jar' in col.text:
                        fix_dict['Link'] = col.find('a')['href']
                    elif 'IF' in col.text or 'HF' in col.text:
                        fix_dict['IFIX Number'] = col.text.strip()
                    elif 'Released' in col.text:
                        fix_dict['Release Date'] = datetime.strptime(col.text.strip(), '%m/%d/%Y').strftime('%Y-%m-%d')
                    else:
                        continue
                    col_index += 1
                if fix_dict:
                    link_list.append(fix_dict)
    return link_list

maximo_versions = {'7.6.1.3': 'https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm%7ETivoli&product=ibm/Tivoli/IBM+Maximo+Asset+Management&release=7.6.1.3&platform=All&function=all', '7.6.1.2': 'https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm%7ETivoli&product=ibm/Tivoli/IBM+Maximo+Asset+Management&release=7.6.1.2&platform=All&function=all'}
all_scraped_links = []
for version, url in maximo_versions.items():
    page_html = requests.get(url).content
    extracted_links = extract_links(page_html)
    for link in extracted_links:
        link['Maximo Version'] = version
    all_scraped_links.extend(extracted_links)
if all_scraped_links:
    df = pd.DataFrame(all_scraped_links)
    df = df[['Maximo Version', 'IFIX Number', 'Release Date', 'Link']]
    output_path = 'maximo_ifix_links.xlsx'
    df.to_excel(output_path, index=False)
    print(f'Successfully saved {len(df)} IFIX links to {output_path}.')
else:
    print('No IFIX links were found on Fix Central.')