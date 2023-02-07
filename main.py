import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.utils import formatdate
from email.mime.text import MIMEText


url = '' # Ex: https://dolap.com/ara?q=Guitar+Hero
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

smtp_server = "" # Ex: mail.example.com
port = 587  # For TLS (STARTTLS)
sender = '' # Ex: alper@example.com
receiver = '' # Ex: alper@example.com
password = ''
context = ssl.create_default_context()

# Get HTML
html = requests.get(url, headers=headers).text

# Convert to BS
soup = BeautifulSoup(html, 'html.parser')

# Find Count Element
count_element = soup.find(attrs="span", class_='subtitle')

# Get Count Element Text
count_element_text = str(count_element.text)

# Get Count Value and Print
count = int(count_element_text.split()[0])
print(f'Dolap: {count}')

# Get Logged Value (From Previous Session)
with open('count_log.txt', 'r') as count_log:
    log = int(count_log.read())
    print(f'Log: {log}')

# Check if count changed. If not, do nothing 
if (log == count):
    print('No difference on value.')
# Check if count decreased. If so, log new value and do nothing.
elif (log > count):
    print('Value decreased! Logging new value. No need for mail.')

    with open('count_log.txt', 'w') as count_log:
        count_log.write(str(count))
    print('Value logged.')
# Check if count increased. If so, log new value and send mail.
elif (log < count):
    print('Value increased! Logging new value and sending mail.')
    with open('count_log.txt', 'w') as count_log:
        count_log.write(str(count))

    print('Value logged. Sending mail...')
    msg = MIMEText(f'Listing count increased from {log} to {count}. URL: {url}')
    msg['Subject'] = 'Check Dolap!'
    msg['From'] = sender
    msg['To'] = receiver
    msg["Date"] = formatdate(localtime=True)
    
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print('Sent mail! See you tomorrow!')

# Seperator for Docker logs
print('===============')