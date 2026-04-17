import smtplib
from email.mime.text import MIMEText

class EmailSender:

    def __init__(self, sender_email, app_password):
        self.sender_email = sender_email
        self.app_password = app_password

    def send_email(self, receiver_email, subject, message):

        try:
            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = receiver_email

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(self.sender_email, self.app_password)

            server.send_message(msg)
            server.quit()

            print("✅ Email sent successfully!")

        except Exception as e:
            print("❌ Error:", e)