#!/usr/bin/env python
# coding: utf-8

# In[61]:


import re 

s ='this is test code. mobile number is 8854566766 **^63and flkjhfjkhdjh gj33 jh 5jhbh6gh6776!?'

#get all digits
print(re.findall('\d',s)) #return digits


# In[55]:


print(re.findall('\D',s)) #return non-digit


# In[58]:


#return alpha-numeric
print(re.findall('\w',s))


# In[62]:


#return special char
print(re.findall('\W',s))


# In[64]:


#split by given seperator 
print(re.split('is',s))


# In[67]:


##match : what shoud be exist and what should not 
st = input('enter data ')
o = re.match('(.*) are (.*)',st) # string should contain are 

#(.*) group 1 , and gorup 2
print(o.groups())
if o:
    print('are is exist')
else:
    print('are is not match')


# In[69]:


#validate emaild id 
#search: what should be exist 

email = input('enter email id ')

res = re.search('@gmail.com$',email)

if res:
    print('valid email id ')
else:
    print('invalid email id')


# In[78]:


#print(re.findall('\d',s)) #return digits

o = re.findall('\d',s)

print(o)
#[1,2,6]    126
res = ''.join(o)

print(res)


