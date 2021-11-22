import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

if __name__ == "__main__":
    receiver_address = input("Enter receiver's email address: ")
    OTP = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print(f"OTP: {OTP}")

    mail_content = f"""
    <html>
    <head></head>
    <body>
        <p style="line-height: 1.5;">
            <span style="font-family: Georgia, serif;">
                Hello!<br>
                Thank you for verifying with The Mythos Conservatory. Please enter the following code into your ticket channel for verification:
            </span>
            <span style="font-family: Georgia, serif;"><br></span>
            <span style='font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;'>
                <strong><span style="font-size: 20px;">{OTP}</span></strong>
            </span>
            <span style="font-family: Georgia, serif;"><br><br>Thanks,<br>The Mythos Conservatory Team</span>
        </p>
        <img style="height:150px" src="https://i.imgur.com/KhmTHRv.png" alt="Welcome Banner">
    </body>
    </html>
    """
    #mail_content = f'Hello!\nThank you for verifying with The Mythos Conservatory. Please enter the following code into your ticket channel for verification.\n{OTP}\n\nThanks,\nThe Mythos Conservatory Team'

    sender_address = 'themythosconservatory@gmail.com'
    sender_pass = '!Q2w#E4r%T6y'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f'{OTP} is your Institute Verification Code for The Mythos Conservatory'   #The subject line

    message.attach(MIMEText(mail_content, 'html'))
    # message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('MCEmailVerifier.log', 'a') as f:
        f.write(f"{current_time} {receiver_address} {OTP}\n")