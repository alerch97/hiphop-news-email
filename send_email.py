import smtplib, ssl, os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "alexlerch76@gmail.com"
    password = os.environ.get("PASSWORD_GMAIL")
    receiver = "alexlerch76@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    test_message = f"""\
Subject: New mail from test@test.com

From: test@test.com
Hi, this is an test mail for the portfolio homepage!
"""
    send_email(test_message)