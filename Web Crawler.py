#!/usr/bin/env python
# coding: utf-8

# In[18]:


import bs4
import time
import urllib
import requests


# In[19]:


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


# In[37]:


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html,"html.parser")
    
    content_div = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output")
    
    article_link = None
    
    for element in content_div.find_all("p",recursive = False):
        if element.find("a",recursive = False):
            article_link = element.find("a",recursive = False).get("href")
            break
    if not article_link:
            return
        
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/',article_link)
        
    return first_link


# In[38]:


def continue_crawl(search_history,target_url,max_steps = 25):
    if search_history[-1] == target_url:
        print("We have found the target article")
        return False
    elif len(search_history) > max_steps:
        print("We have gone too long")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("a loop is going on")
    else:
        return True
    
article_chain = [start_url]


# In[39]:


while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2) # Slow things down so as to not hammer Wikipedia's servers


# In[ ]:




