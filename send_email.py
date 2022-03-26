from email.message import EmailMessage
from smtplib import SMTP
msg = EmailMessage()
msg.set_content('Este es un mensaje de prueba')

msg['Subject'] = 'Asunto de prueba'
msg['From'] = 'cristianrobles2020@itp.edu.co'
msg['To'] = 'shaydruano2020@itp.edu.co'

username = 'cristianrobles2020@itp.edu.co'
password = ''

server = SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
#server.sendmail(from_addr, to, message
server.send_message(msg)