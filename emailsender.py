#For Aeroconsult 2019 I needed to send each of the participants who bothered to sign up their code to be used at check-in and other stuff

import csv
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('mailinglist.csv', newline='') as csvfile:#csv file with contained a list of each participants's code and email address
    emails = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in emails:
        number, adress = row[0].split(",")#number is the code needed to be send, address is the email address
        print(number + " " + adress)
        msg = email.mime.multipart.MIMEMultipart()

        msg['From'] = ''#the email address from which they received the email
        msg['To'] = adress
        msg['Subject'] = 'AEROCONSULT 2019-Confirmare Inscriere'
        msg.attach(MIMEText())#message in here

        user = ''#email address for login
        password = ''#password
        smtp_host = 'smtp.gmail.com'
        smtp_port = '587'
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, adress, msg.as_string())

