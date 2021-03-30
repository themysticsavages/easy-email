
def startemail():
    # Configuration file for EasyEmail
    # EasyEmail, makes mass text emailing easy.
    # Make sure less secure apps is turned on the account you're sending emails from.

    import smtplib, ssl, os, time

    from email.mime.text import MIMEText
    from email.utils import formataddr

    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    clear = lambda: os.system("cls")

    clear()

    names = 0
    emails = 0

    # Users
    sender_email = "senderemail@email.com"
    sender_name = "Enter Name Here"

    receiver_emails = ['receiveremail@email.com'] # You can enter multiple emails. It should look like this ['receiver1@email.com', 'receiver2@email.com']
    receiver_names = ['Enter Name Here'] # Make sure to enter names for each email you want to send to.

    password = input("Enter the password for " + sender_email + ": ")

    # Email
    os.chdir(r'location of easyemail') # If you saved this in the Downloads folder, say 'C:\Users\YOUR Username\Downloads'

    email_body = '''
    Enter your email here
	
    '''

    # Attachment
    attach= 'info.txt' # If you want to attach something, add a file to the same folder EasyEmail is in.

    clear()

    print('Starting script...')

    print("")

    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
    
    # Email information
        msg = MIMEMultipart()
        msg['To'] = formataddr((receiver_name, receiver_email))
        msg['From'] = formataddr((sender_name, sender_email))
    
        msg['Subject'] = "Hello " + receiver_name

        msg.attach(MIMEText(email_body, 'html'))

        try:
            # Open PDF file in binary mode
            with open(attach, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)
            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attach}",
            )
            msg.attach(part)
        except Exception as e:
            print(f'Script sent a warning. Attachment could not be found.\n{e}')

        # Email sending code
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            context = ssl.create_default_context()
            server.starttls(context=context)

            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

            print('Email sent to ' + (receiver_names[names]), 'at ' + (receiver_emails[emails]))

            names = names + 1
            emails = emails + 1

        except Exception as e:
            print(f'Email failed to send. Check your internet connection.\n{e}')

        print("")
        print("Email sent.")

    time.sleep(2)

startemail()

