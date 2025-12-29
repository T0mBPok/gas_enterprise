import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Iterable

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "sasha.kowal.sergee@gmail.com"
SMTP_PASSWORD = "fdlr aecf dvcm fwij"


def send_email(
    to: Iterable[str],
    subject: str,
    body: str,
):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = ", ".join(to)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)