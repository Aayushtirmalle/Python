#taking senders,receivers,message from user
import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
a=input("Enter senders email")
b=input("Enter receiver email")
m=input("Message")
p=getpass.getpass()
s.login(a,p)
s.sendmail(a,b,m)
print("msg sent successfully")
s.quit()