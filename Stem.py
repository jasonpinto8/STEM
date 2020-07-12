#!/usr/bin/env

import subprocess
import time
from datetime import datetime
import smtplib, ssl





def maildown(ping_two):
    # port = 587  # For starttls
    # smtp_server = "smtp.gmail.com"
    # sender_email = "example@gmail.com"
    # receiver_email = "example@aol.com"
    # password = 'password'
    # message = '''\
    # Subject : %s is Down
    #
    # This device is down : %s ''' % (ping_two, ping_two)
    # # test=message + str(ping)
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)
        print('down mail sent !',ping_two) # this line is just to test if the email function is called

def mailup(ping):
    # port = 587  # For starttls
    # smtp_server = "smtp.gmail.com"
    # sender_email = "example@gmail.com"
    # receiver_email = "example@aol.com"
    # password = 'password'
    # message = '''\
    # Subject : %s is UP
    #
    # This device is down : %s ''' % (ping, ping)
    # # test=message + str(ping)
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)

          print('upmail sent !',ping)  # this line is just to test if the email function is called


# datetime object containing current date and time
now = datetime.now()

# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)


lis = ['microsoft.com', 'fb.com', 'asana.com']
new = list()


while True:


    for ping in lis:
       
        res = subprocess.call(['ping', '-c', '1', ping])
        time.sleep(3)

        if res == 0:
            print(dt_string, "ping to", ping, "OK", file=open("up.txt", "a"))

        elif res == 2 or res == 1:
            print(dt_string, "no response from", ping, file=open("down.txt", "a"))

            maildown(ping)
            new.append(str(ping))
            lis.remove(str(ping))


    for ping_two in new:
            res = subprocess.call(['ping', '-c', '1', ping_two])
            time.sleep(5)

            if res == 0:
                print(dt_string, "ping to", ping_two, "OK", file=open("up.txt", "a"))
                mailup(ping_two)
                lis.append(str(ping_two))
                new.remove(str(ping_two))

            elif res == 2 or res == 1:
                print(dt_string, "no response from", ping_two, file=open("down.txt", "a"))



            else:
                print(dt_string, "no response from", ping_two, file=open("down.txt", "a"))







