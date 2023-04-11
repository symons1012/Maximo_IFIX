import pandas as pd
import schedule
import time

from send_email import sendEmail

# Read the Maximo IFIX data from the CSV file
maximo_ifix_data = pd.read_csv('maximo_ifix_data.csv')

# Schedule the sendEmail function to run based on the release date
for index, row in maximo_ifix_data.iterrows():
   schedule.every().day.at(row['Release Date']).do(sendEmail, 'sender_email', 'sender_password', 'receiver_email', 'New Maximo IFIX Release!', 'A new Maximo IFIX release has been detected, please download the release at ' + row['Download Link'], row['Download Link'])

while True:
    schedule.run_pending()
    time.sleep(60*60)
