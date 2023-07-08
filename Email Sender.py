import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, content):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    smtp_username = 'your_username'  # Replace with your SMTP username
    smtp_password = 'your_password'  # Replace with your SMTP password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    body = MIMEText(content, 'plain')
    msg.attach(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print('Error sending email:', str(e))

def main():
    print('Welcome to Email Sender!')

    sender_email = input('Enter the sender email address: ')
    recipient_email = input('Enter the recipient email address: ')
    subject = input('Enter the email subject: ')
    content = input('Enter the email content: ')

    send_email(sender_email, recipient_email, subject, content)

if __name__ == '__main__':
    main()