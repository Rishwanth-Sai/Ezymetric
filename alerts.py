import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'youremail@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("youremail@example.com", "password")
        server.send_message(msg)

if __name__ == "__main__":
    send_alert_email("Alert: Campaign Threshold Reached", "Campaign has exceeded expected clicks.")
