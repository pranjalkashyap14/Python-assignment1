#!/usr/bin/env python
# coding: utf-8

# In[3]:


#  1.   Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#      between 2000 and 3200 (both included) The numbers obtained should be printed in a comma-separated sequence
#      on a single line.


# In[4]:


A = []
for x in range (2000,3200):
    if(x%7==0) and (x%5==0):
        A.append(str(x))
print(A)


# In[5]:


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
#    with a space between first name and last name.


# In[9]:


First_name = input()
Last_name = input()
print(Last_name,First_name)


# In[10]:


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm. using Formula: V=4/3 * π * r 3


# In[13]:


import math


# In[15]:


pi = math.pi
Diameter=12
R=Diameter/2
Volume=4/3*pi* R**3
print("volume of sphere is", Volume)


# In[ ]:





# In[ ]:




