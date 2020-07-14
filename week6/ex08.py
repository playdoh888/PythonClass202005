# Import smtplib for the actual sending function
import smtplib
import ssl

loginCredential_User_ID = 'jack.wang888@gmail.com'
loginCredential_Password = 'Enter your password here'

to_addrs = "the email address that you want to send the email to"
from_addr = "jack.wang888@gmail.com"
smtp_server = 'smtp.gmail.com'
port = 587

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(loginCredential_User_ID, loginCredential_Password)
    server.sendmail(from_addr, to_addrs, "Hello World!")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

print("Email sent!")
