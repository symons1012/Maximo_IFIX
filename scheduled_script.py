import pandas as pd
import schedule
import time
from maximo_ifix_scraper import getMaximoIFIXes
from extract_maximo_ifixes import extractIFIXes
from send_email import sendEmail


# Set up the email details
sender_email = 'your_sender_email@gmail.com'
sender_password = 'your_sender_email_password'
recipient_email = 'recipient_email'

# Set up the file path
file_path = 'maximo_ifixes.csv'


# Define the function to check for new releases


def checkForReleases():
    # Get the existing and latest releases scraped from the IBM Fix Central page
    existing_releases = pd.read_csv(file_path)

    latest_releases = extractIFIXes()

    # Compare the two data frames to check for new releases
    new_releases = latest_releases[~latest_releases.isin(existing_releases)].dropna()

    # If new releases are detected, send an email notification
    if not new_releases.empty:
        subject = 'New Maximo IFIX Release detected'
        message = f'The following new Maximo IFIX releases are now available on IBM Fix Central:\n{new_releases.to_string(index=False)}'
        sendEmail(sender_email, sender_password, recipient_email, subject, message)
        
        # Append the new releases to the existing releases dataframe and save the updated dataframe in the CSV file
        updated_releases = pd.concat([existing_releases, new_releases], ignore_index=True)
        updated_releases.to_csv(file_path, index=False)
        
        print('New releases detected and notification sent.')
    else:
        print('No new releases detected.')
        

# Schedule the script to run every day at a specific time
schedule.every().day.at('09:15').do(checkForReleases)


while True:
    schedule.run_pending()
    time.sleep(1)
