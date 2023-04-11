import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get('https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm%7ETivoli&product=ibm/Tivoli/IBM+Maximo+Asset+Management&release=7.6.1.3&platform=All&function=all')
    soup = BeautifulSoup(response.text, 'html.parser')
    fix_array = []

    for fix_parent in soup.find_all(class_='mod-content'):
        for fix in fix_parent.find_all('a'):
            if 'IF' in fix.text:
                fix_name = fix.text
                fix_date = fix.find_previous_sibling().text
                fix_url = fix['href']

                download_url = "https://www.ibm.com/"+fix_url.replace("selectFixes", "downloadFixes")+"&downloadMethod=http"
                fix_array.append([fix_name, fix_date, download_url])

    with open('maximo_7.6.1.3_ifixes.csv', mode='w', newline='') as ifix_file:
        ifix_writer = csv.writer(ifix_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ifix_writer.writerow(['ifix_name', 'ifix_date', 'ifix_download_link'])

        for fix_data in sorted(fix_array, key=lambda x: x[1]):
            ifix_writer.writerow(fix_data)

if __name__ == '__main__':
    main()
