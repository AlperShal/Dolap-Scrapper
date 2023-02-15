from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.utils import formatdate
from email.mime.text import MIMEText

search_list = ['Guitar Hero', 'Rockband'] # Ex: ['Guitar Hero', 'Band Hero']
log_file = 'count_log.json'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

smtp_server = "" # Ex: mail.example.com
port = 587  # For TLS (STARTTLS)
sender = '' # Ex: alper@example.com
receiver = '' # Ex: alper@example.com
password = ''
context = ssl.create_default_context()


def append_new_to_log():
    print('Checking for new search strings.')
    db = {}
    isEdited = 0
    with open(log_file, 'r') as file:
        file_read = file.read()
        db = json.loads(file_read)
        for i in search_list:
            if i not in db:
                db[i] = 0
                isEdited = 1
    if isEdited:
        print('New search string(s) found. Adding them to log.')
        with open(log_file, 'w') as file:
            json_out = json.dump(db, file, indent=4)
    else:
        print('New search string(s) not found.')
    print('---------------')

def get_search_url(search_str):
    base = 'https://dolap.com/ara?q='
    for i in search_str.split(' '):
        base = base + i + '+'
    base = base.removesuffix('+')
    return base

def get_listing_count(url):
    # Get HTML
    html = requests.get(url, headers=headers).text

    # Convert to BS
    soup = BeautifulSoup(html, 'html.parser')

    # Find Count Element
    count_element = soup.find(attrs="span", class_='subtitle')

    # Get Count Element Text
    count_element_text = str(count_element.text)

    # Get Count Value, Print and Return
    count = int(count_element_text.split()[0])
    return count

def compare_and_mail(new_value, url, search_str):
    # Print what is being searched for
    print(f'Session: {search_str}')

    # Print new value
    print(f'Dolap: {count}')

    # Get Logged Value (From Previous Session)
    with open(log_file, 'r') as file:
        file_read = file.read()
        db = json.loads(file_read)
        log = db[search_str]
        print(f'Log: {log}')

    # Check if count changed. If not, do nothing 
    if (log == new_value):
        print('No difference on value.')
    # Check if count decreased. If so, log new value and do nothing.
    elif (log > new_value):
        print('Value decreased! Logging new value. No need for mail.')
        with open(log_file, 'r') as file:
            file_read = file.read()
            db = json.loads(file_read)
            db[search_str] = new_value
        with open(log_file, 'w') as file:
            json_out = json.dump(db, file, indent=4)
        
        print('Value logged.')
    # Check if count increased. If so, log new value and send mail.
    elif (log < new_value):
        print('Value increased! Logging new value and sending mail.')
        with open(log_file, 'r') as file:
            file_read = file.read()
            db = json.loads(file_read)
            db[search_str] = new_value
        with open(log_file, 'w') as file:
            json_out = json.dump(db, file, indent=4)

        print('Value logged. Sending mail...')
        msg = MIMEText(f'Listing count increased from {log} to {new_value}. URL: {url}')
        msg['Subject'] = f'Check Dolap for {search_str}!'
        msg['From'] = sender
        msg['To'] = receiver
        msg["Date"] = formatdate(localtime=True)

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo() 
            server.starttls(context=context)
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print('Sent mail!')
    
    print('---------------')


# Print date-time
print(datetime.now())
print('---------------')

# Check if new search strings added and log them to file.
append_new_to_log()

for search_str in search_list:
    # Get search url
    url = get_search_url(search_str)
    # Get listing count
    count = get_listing_count(url)
    # Compare with log and send mail if necessary
    compare_and_mail(count, url, search_str)

print('===============')
