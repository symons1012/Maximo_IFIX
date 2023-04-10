import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


 def get_links():
    """Get the link for the latest Maximo 7.6 release or IFIX update"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www-945.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm~Tivoli&product=ibm/Tivoli/IBM+Maximo+Asset+Management&release=7.6.1.3&platform=All&function=all")

    # search for the most recent version of Maximo 7.6
    elem = driver.find_element_by_link_text("IBM Maximo Asset Management 7.6.1.3 - All platforms and languages")
    driver.get(elem.get_attribute("href"))
    elem = driver.find_element_by_link_text("IBM Maximo Asset Management 7.6.1.3 Fix Pack 001 - All platforms and languages")
    link = elem.get_attribute("href")

    driver.quit()

    return link