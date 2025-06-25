import smtplib
from email.mime.text import MIMEText
from assistant import speak

SENDER_EMAIL = "dilipkumar2000105@gmail.com"
APP_PASSWORD = "ntzp kylx gyec oaha"  

def send_email():
    speak("Sir, Please enter the recipient's email address.")
    recipient = input("To: ")

    speak("Sir, What is the subject of the email?")
    subject = input("Subject: ")

    speak("What should I say in the email,Sir?")
    body = input("Message: ")

    try:
        msg = MIMEText(body)
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

       
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        speak("Email has been sent successfully sir.")
    except Exception as e:
        speak("sir,Failed to send the email.")
        print("Sir im facing an error:", e)
