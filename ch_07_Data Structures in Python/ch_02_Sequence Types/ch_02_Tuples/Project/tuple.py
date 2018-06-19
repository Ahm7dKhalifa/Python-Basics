
# coding: utf-8

# # 1.create

# In[1]:

#1.1 with parentheses 


# In[4]:

tuple1 = (1,2,3,4)


# In[5]:

print(tuple1)


# In[ ]:

# 1.2 with constructor


# In[6]:

tuple2 = tuple((5,6,7))


# In[7]:

print(tuple2)


# In[8]:

#1.3 without parentheses


# In[9]:

tuple3 = 8,9,10


# In[10]:

print(tuple3)


# In[11]:

print(type(tuple3))


# # 2.access and read operations

# In[13]:

print(tuple1[1])


# In[14]:

print(tuple1[0:3])


# # 3.no insert new item

# In[15]:

tuple1.append(5)


# # 4.no update exiting item

# In[16]:

tuple1[0] = 100


# # 5.delete tuple

# In[18]:

del tuple1


# In[ ]:



