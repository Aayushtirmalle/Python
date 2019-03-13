import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='aayushmt6@gmail.com'
reciever='abishekabi673@gmail.com,superabdur3'
msg="hii PPYTHON EMAIL"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,reciever,msg)
print("msg sent successfully")
s.quit()