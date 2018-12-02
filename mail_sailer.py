import smtplib
smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
smpt_obj.ehlo()
smpt_obj.starttls()
smpt_obj.login('8600999@gmail.com', 'qwerty8600999')
smpt_obj.sendmail('8600999@gmail.com', '4008@emercit.ru', 'Subject: Hellow \nThis is test messenge!')
smpt_obj.quit()