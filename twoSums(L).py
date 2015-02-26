
# coding: utf-8

# In[1]:

def twoSums(L):
    """returns the separate sums of positive and of negative values in list L"""
    return sum(x), sum(y)


# In[2]:

L =[1, -6, 4, 2, 3, -7]


# In[3]:

x = [L for L in L if L < 0]
y = [L for L in L if L > 0]


# In[4]:

twoSums(L)


# In[ ]:



