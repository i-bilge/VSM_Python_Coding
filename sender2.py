# importing yagmail and its packages
import yagmail
  
# initiating connection with SMTP server
yag = yagmail.SMTP("iismailbilgegmail.com",
                   "Mustafa99086")
# Adding Content and sending it
yag.send("andrewfade41@gmail.com", 
         "Last Sessions Mail",
         "Hello...")