import smtplib
import ssl

def send_email(link):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "your_email@gmail.com"  # Enter your address
    receiver_email = "symons1012@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        message = f"Subject: New Maximo 7.6 Release Found!\n\nLink: {link}"
        server.sendmail(sender_email, receiver_email, message)

def get_latest_link():
    url = "https://www.ibm.com/support/fixcentral/"
    maximo_product_id = "ibm/Tivoli/IBM+Maximo+Asset+Management"
    platform = "All"
    time_period = "Last 7 days"

    session = requests.Session()
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all('input')
    assert s
    hide_values = [i['value'] for i in s if i.has_attr('name') and i['name'] == 'fn']
    assert len(hide_values) == 1
    session.headers.update({
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Origin': 'https://www.ibm.com',
        'Referer': 'https://www.ibm.com/support/fixcentral/',
        'Accept-Language': 'en-US,en;q=0.9',
    })

    form_data = {
        hidden_value: ''
        for hidden_value in hide_values
    }

    form_data.update({
        'path': 'IBM/Tivoli/IBM Maximo Asset Management',
        'product': 'ibm/Tivoli/IBM Maximo Asset Management',
        'platform': platform,
        'function': 'all',
        'includeSupersedes': 0,
        'includePrerequisites': 0,
        'typeFixCriteria': 0,
        'scope': 'fix',
        'x': '22',
        'y': '13',
        'query': '*
        search
        Filter
        sort=release_date&order=desc&number=100',
        'timeframe': time_period,
        'result_page': 1,
    })
    res = session.post(f'https://www.ibm.com/support/fixcentral/{hide_values[0]}?ssdChild=ibm/2/Hardware', data=form_data)
    soup = BeautifulSoup(res.content, 'html.parser')

    download_links = soup.find_all('a', href=True)
    for link in download_links: 
        if "ibm/Tivoli/IBM Maximo Asset Management" in str(link) and "href" in str(link) and "ftp" not in str(link) and (".zip" in str(link) or ".tar.gz" in str(link)):
            latest_link = link['href']
            break

    return latest_link


def main():
    latest_link = get_latest_link()
    send_email(latest_link)

if __name__ == "__main__":
    main()
