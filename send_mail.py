import smtplib
from email.mime.text import MIMEText


def send_email(customer, dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = "d01a25f2ddb575"
    password = "1522ae5eeb7837"

    message = f"""<h3>Feedback Submission</h3>
                  <ul>
                      <li>Customer: {customer}</li>
                      <li>Dealer: {dealer}</li>
                      <li>Rating: {rating}</li>
                      <li>Comments: {comments}</li>
                  </ul>"""

    sender_email = "noreply@feedbackapp.test"
    receiver_email = "admin@company.test"

    msg = MIMEText(message, "html")
    msg["Subject"] = "Lexus Feedback"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
