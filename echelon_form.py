#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp


# In[2]:


a = sp.Matrix([
    [1, 2, -3, 0],
    [2, 4, -2, 2],
    [3, 6, -4, 3]
])


# In[3]:


a.echelon_form()


# In[ ]:




