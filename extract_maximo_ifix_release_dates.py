import requests\nfrom bs4 import BeautifulSoup\nimport pandas as pd\ndef get_links():\n    url = 'https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm%7ETivoli&product=ibm/Tivoli/IBM+Maximo+Asset+Management&release=7.6.1.3&platform=All&function=all'\n    page = requests.get(url)\n    soup = BeautifulSoup(page.content, 'html.parser')\n    results = soup.find_all('a', class_='downloadDesc')\n    links = []\n    for r in results:\n        if 'ifix' in r['href'] and 'TA' in r['href']:\n            links.append(r['href'])\n    return links\ndef scrape_version(links):\n    list_of_links = []\n    for link in links:\n        page = requests.get(link)\n        soup = BeautifulSoup(page.content, 'html.parser')\n        url = link.replace('/download', '/downloadFixes')\n        results = soup.find_all('a', href=True)\n        for r in results:\n            if 'downloadFixes' in r['href'] and '.txt' not in r['href'] and 'requisite' not in r['href']:\n                if 'http' not in r['href']:\n                    url_folder = url + r['href']\n                else:\n                    url_folder = r['href']\n            if 'downloadFixes' in r['href'] and '.txt' in r['href']:\n                if 'http' not in r['href']:\n                    url_file = url + r['href']\n                else:\n                    url_file = r['href']\n        list_of_links.append(url_file)\n    df = pd.DataFrame(list_of_links, columns=['HTTPS Link'])\n    return df\ndef main():\n    links = get_links()\n    df = scrape_version(links)\n    df.to_excel('maximo_ifix_links.xlsx', index=False)\n\nif __name__ == '__main__':\n    main()