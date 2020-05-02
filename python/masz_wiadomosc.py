
import os, csv, time
import smtplib
from email.message import EmailMessage
start=time.time()
EMAIl_ADDRESS = os.environ.get('EMAIL_USER')
EMAIl_PASSWORD = os.environ.get('EMAIL_PASS')

"""contacts = ['dhoin9@op.pl', 'dhoin9@live.com']
msg = EmailMessage()
msg['Subject'] = "Melanż"
msg['From'] = EMAIl_ADDRESS
msg['To'] = Lud.man
msg.set_content('Witaj mordo!!\n\nCo powiesz na małe chlanie?\n\nWsyłane z systemu Linux')
"""

class Lud:
    def __init__(self, man, file1, file2, file3):
        self.man = man
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3

record_list = []
with open('list.csv', 'r') as fi:
    reader = csv.reader(fi, delimiter=';')
    for line in reader:
        man, file1, file2, file3 = line
        record = Lud(man, file1, file2, file3)
        record_list.append(record)

for person in record_list:
    msg = EmailMessage()
    msg['Subject'] = "Melanż"
    msg['From'] = EMAIl_ADDRESS
    msg['To'] = person.man
    msg.set_content('Witaj mordo!!\n\nCo powiesz na małe chlanie?\n\nWsyłane z systemu Linux')
    print(msg['To'])
    files = [person.file1, person.file2, person.file3]
    print(files)
    for file in files:
        #załaczanie plików
        try:
            with open(file,'rb') as f:
             print(file)
             file_data = f.read()
             file_name = f.name
             msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file)
        except:
            continue

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
       smtp.login(EMAIl_ADDRESS, EMAIl_PASSWORD)
       smtp.send_message(msg)
stop=time.time()
print(stop-start)
print(time.process_time())