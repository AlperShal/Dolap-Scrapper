from datetime import datetime
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.utils import formatdate
from email.mime.text import MIMEText


url = '' # Ex: https://dolap.com/ara?q=Guitar+Hero
url2 = '' # You can leave this empty
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

smtp_server = "" # Ex: mail.example.com
port = 587  # For TLS (STARTTLS)
sender = '' # Ex: alper@example.com
receiver = '' # Ex: alper@example.com
password = ''
context = ssl.create_default_context()


def get_search_str(url):
    after_q = url.split('q=')[1]
    words = after_q.split('+')
    search_str = ''
    for i in words:
        search_str = search_str + i + ' '
    search_str = search_str.removesuffix(' ')
    return search_str

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

def compare_and_mail(log_file, new_value, url, search_str):
    # Print what is being searched for
    print(f'Session: {search_str}')

    # Print new value
    print(f'Dolap: {count}')

    # Get Logged Value (From Previous Session)
    with open(f'{log_file}', 'r') as count_log:
        log = int(count_log.read())
        print(f'Log: {log}')

    # Check if count changed. If not, do nothing 
    if (log == new_value):
        print('No difference on value.')
    # Check if count decreased. If so, log new value and do nothing.
    elif (log > new_value):
        print('Value decreased! Logging new value. No need for mail.')

        with open(f'{log_file}', 'w') as count_log:
            count_log.write(str(new_value))
        print('Value logged.')
    # Check if count increased. If so, log new value and send mail.
    elif (log < new_value):
        print('Value increased! Logging new value and sending mail.')
        with open(f'{log_file}', 'w') as count_log:
            count_log.write(str(new_value))

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
            print('Sent mail! See you tomorrow!')
    
    print('---------------')


# Print date-time
print(datetime.now())
print('---------------')

# Get listing count
count = get_listing_count(url)

# Get search string
search_str = get_search_str(url)

# Compare with log and send mail if necessary
compare_and_mail('count_log.txt', count, url, search_str)

# Check if there is another URL (url2) and if so apply same steps (You can multiply this block and change vars according to your needs)
if url2 != '':
    count = get_listing_count(url2)
    search_str = get_search_str(url2)
    compare_and_mail('count_log2.txt', count, url2, search_str)


# Seperator for Docker logs
print('===============')
