import smtplib
import ssl
from email.message import EmailMessage
import mimetypes
import os
import pandas as pd

from dotenv import load_dotenv

# Load environment variables (Sender Data)
# The email and app-specific password for that email that are stored in the .env file
load_dotenv()
email_sender = os.environ.get('SENDER_EMAIL')
email_password = os.environ.get('SENDER_PASSWORD')

print(f"The emails will be sent from: {email_sender}")

# Add SSL ( of security)
context = ssl.create_default_context()

def send_email(receiver, subject, body, pdf_path=None, is_html=False): 

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    
    if is_html:
        em.add_alternative(body, subtype='html')
    else:
        em.set_content(body)
    
    # Attach PDF if provided
    if pdf_path:
        # Guess the MIME type and subtype
        mime_type, _ = mimetypes.guess_type(pdf_path)
        mime_type, mime_subtype = mime_type.split('/')
        
        with open(pdf_path, 'rb') as pdf_file:
            em.add_attachment(pdf_file.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(pdf_path))
    
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())

