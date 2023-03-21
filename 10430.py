#!/usr/bin/env python
# coding: utf-8

# In[2]:


A, B, C = map(int,input().split()) #정수형으로 

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

