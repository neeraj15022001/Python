#!/usr/bin/env python
# coding: utf-8

# # Get Your External IP Address using Python

# In[10]:


import socket as s
pcName = s.gethostname()
IPAddress = s.gethostbyname(pcName)
print("Your Computer name is:",pcName)
if IPAddress == "127.0.0.1":
    print("This is loopback address that is you are on local host with IP Address:",IPAddress)
else:
    print("Your IPAddress is:",IPAddress)


# In[ ]:




