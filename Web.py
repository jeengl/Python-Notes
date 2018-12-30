#!/usr/bin/env python
# coding: utf-8

# In[9]:


#! python3
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('More Info')
type(linkElem)
linkElem.click() # follows the "Read IT Online" link

