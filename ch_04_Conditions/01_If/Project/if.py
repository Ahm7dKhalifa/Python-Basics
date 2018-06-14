
# coding: utf-8

# # 1.if only with One Condition

# In[1]:

x = 100


# In[2]:

y = 200


# In[3]:

if(x < 200):
    z = 300    


# In[4]:

print(z)


# # 2.if with multi conditions

# In[6]:

a = 15


# In[7]:

b = 20


# In[8]:

c = 30


# In[9]:

if(a < b & b < c):
    c = 50


# In[10]:

print(c)


# # 3.if and elif 

# In[12]:

if ( b > c ):
    a = 100
elif ( b > a):
    a = 200


# In[13]:

print(a)


# # when more condition is true .. the first block well be excute

# In[15]:

x = 1


# In[16]:

y = 2


# In[18]:

if(x < y):
    z = 10
elif( y > x):
    z = 100000


# In[19]:

print(z)


# # 4.if with else

# In[21]:

h = 1


# In[22]:

if( h > 100 ):
    f =100
elif( h > 10000 ): 
    f =10000
else:
    f = 0


# In[23]:

print(f)


# In[ ]:



