import yagmail
import time
from sendingMail import password

people = ["andrew","ismail"]
mail_adress =["andrewfade41@gmail.com","iismailbilge@gmail.com"]

subject = "From the last session of python:("
sender = "iismailbilge@gmail.com"
yag = yagmail.SMTP(user = sender, password ="Mustafa99086")
for i in range(2):
    content= f"Hello {people[i]},\n\t Thanks for your mail!  \n\nBest Reagards"
    yag.send(to = mail_adress[i], subject = subject, contents = content)
    print(f"Email sent to {mail_adress[i]} for {people[i]}")
    time.sleep(3)