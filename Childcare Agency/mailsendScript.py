from flask import Flask, request, redirect
import smtplib
import ssl
from email.message import EmailMessage
import os

app = Flask(__name__)

EMAIL_SENDER = 'mandibchaulagain8@gmail.com'
EMAIL_PASSWORD = os.environ.get("PYTHONMANDIBPASSWORD")
EMAIL_RECEIVER = 'mandibchaulagain8@gmail.com'  # same as sender for inbox safety

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    program = request.form.get('program', '')
    message = request.form.get('message', '')

    subject = f"New Inquiry from {first_name} {last_name}"
    body = f"""
    You received a new contact form submission:

    Name: {first_name} {last_name}
    Email: {email}
    Phone: {phone}
    Program of Interest: {program}

    Message:
    {message}
    """

    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = EMAIL_RECEIVER
    em['Subject'] = subject
    em['Reply-To'] = email  # important for replyability
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(em)
        return redirect("/thank-you")  # Or render a thank-you template
    except Exception as e:
        return f"Error sending email: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
