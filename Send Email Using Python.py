#!/usr/bin/env python
# coding: utf-8

# # Send Email using python

# In[1]:


import smtplib, ssl


# In[3]:


port = 587 #465,587,25 are standard ports of smtp
smtpServer = "smtp.gmail.com"
senderEmail = "gneeraj32595@gmail.com"
receiverEmail = "neeraj0595.cse19@chitkara.edu.in"
password = input("Type your email password")
message = """Subject: Hi There

This message is sent from Python.

~Neeraj Gupta
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtpServer,port) as server:
    server.ehlo()
    server.starttls(context = context)
    server.ehlo()
    server.login(senderEmail, password)
    server.sendmail(senderEmail, receiverEmail, message)


# In[ ]:




