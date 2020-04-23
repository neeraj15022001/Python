#!/usr/bin/env python
# coding: utf-8

# # Random Password Generator

# In[4]:


import random

words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#^%$&*!-_"

passwordLength = 15

password = "".join(random.sample(words,passwordLength))

print(password)


# In[ ]:





# In[ ]:




