import requests
import smtplib

#python3 -m venv monitorUrl if  don't have python3-venv installed then you should install it by
#typing sudo apt install python3-venv
#source monitorUrl/bin/activate
#pip install requests
#wrote by me, myself and i. Lotervik :P

def notificationMail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()  # crypter le traffic
        smtp.ehlo()

        smtp.login(adressmail, mdp)
        subject = 'Your Site is down'
        body = 'nanani nanana '
        msg = f'Subject: {subject}\n\n{body}'

        #smtp.sendmail(SENDER,RECEIVER, msg)
        smtp.sendmail(adressmail, adressmail, msg)



adressmail = "yourgmail@gmail.com"
mdp = "yourmdp"

try:
    # 5s le temps d attente , si le site ne repond pas ==> exception
    r = requests.get("https://www.google.com/", timeout=5)
    if r.status_code != 200:
        # https://myaccount.google.com/lesssecureapps
        #notificationMail()
        print("your site is down")
    else : print("mcha")

except Exception as e:
    #notificationMail()
    print("your site is down")







