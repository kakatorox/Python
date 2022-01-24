import smtplib
from email.mime.text import MIMEText

msg=MIMEText("Contenido de Correo")

msg['subject']='Asunto del correo'
msg['From']='kakatorox@gmail.com'
msg['to']='felipetorresmora@outlook.es'

mailServer=smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('kakatorox@gmail.com','Pastel157ftm')
mailServer.sendmail('kakatorox@gmail.com','felipetorresmoraoutlook.es',msg_as_string())

mailServer.close()
