import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg['Subject'] = 'Job list for today'
    msg['From'] = 'asupraja527@gmail.com'
    msg['To'] = 'asupraja527@gmail.com'
    msg.set_content() (f"""This is the job list for today. 
                       Please find the attached file with the job details.
                       Thanks,Supraja""")
    with open('filtered_jobs.csv','rb') as f:
        msg.add_attachment(f.read(), maintyope='application',subtype='octet-stream', filename='jobslist.csv')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login("asupraja527@gmail.com", "nadp bdzt wury bqyw")
        smtp.send_message(msg)