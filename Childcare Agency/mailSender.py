import os
from email.message import EmailMessage
import ssl
import smtplib
import pandas as pd

# Function to check if the file is open
def is_file_open(file_path):
    try:
        # Try to open the file in exclusive write mode
        with open(file_path, 'a'):
            return False  # File is not open
    except IOError:
        return True  # File is open by another process

# Path to the Excel file
file_path = "C:\\Users\\lenovo\\Desktop\\Frontend-Designs\\Childcare Agency\\contacts.xlsx"
# Check if the file is open
if is_file_open(file_path):
    print(f"Error: The file '{file_path}' is open. Please close the file before proceeding.")
    exit()  # Exit the script if the file is open

# Load the data from the Excel sheet
df = pd.read_excel(file_path)  # Replace with your actual file path

# Ensure you are correctly using the email addresses as plain text
email_sender = 'mandibchaulagain8@gmail.com'
email_password = os.environ.get('PYTHONMANDIBPASSWORD')  # Ensure your environment variable is set

# Set up SSL context for secure connection
context = ssl.create_default_context()

# Function to send emails
def send_email(email_receiver, client_name, compliment, pain_point, case_study, company_name):
    subject = 'Free Website Built For Your Business'
    body = f"""
    Hi {client_name},

    I hope you're doing well! As {compliment}, I believe your business can benefit from a quick free website analysis that can help you attract more customers.

    Many businesses face challenges with {pain_point}, and I'd love to show you how simple changes can make a big difference. For example, after implementing similar changes for {case_study}, they saw a significant increase in customer engagement and sales.

    I’m offering you a free website analysis—no strings attached. We’ll take a look at your website, provide a detailed report, and recommend steps you can take to start seeing results.

    Ready to get started?

    Warm regards,  
    Mandib Chaulagain
    """
    
    # Create the email message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    
    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(f"Email sent successfully to {email_receiver}")
    except Exception as e:
        print(f"Error sending email to {email_receiver}: {e}")

# Ensure the 'status' column is of string type to prevent dtype issues
df['status'] = df['status'].astype(str)

# Clean up spaces (leading/trailing) in the 'status' column
df['status'] = df['status'].str.strip()

# Loop through the rows in the DataFrame and send emails
for index, row in df.iterrows():
    # Check if the status is 'SENT', empty, 'nan' (as string), or NaN
    if row['status'].lower() != "sent" and (pd.isna(row['status']) or row['status'].lower() == "nan" or row['status'] == ""):
        # Only send the email if the status is not 'SENT' and is empty, NaN, or 'nan'
        email_receiver = row['email_receiver']
        client_name = row['client_name']
        compliment = row['compliment']
        pain_point = row['pain_point']
        case_study = row['case_study']
        company_name = row['company_name']

        # Call the send_email function for each recipient
        send_email(email_receiver, client_name, compliment, pain_point, case_study, company_name)

        # Update the status to "SENT" after sending the email
        df.at[index, 'status'] = 'SENT'
    else:
        print(f"Skipping {row['client_name']} as the email status is '{row['status']}'.")

# Save the updated DataFrame back to Excel
df.to_excel(file_path, index=False)  # Replace with the desired file path
