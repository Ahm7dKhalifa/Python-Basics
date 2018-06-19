
# coding: utf-8

# # python as queue

# # queue : first in first out

# In[2]:

from collections import deque


# In[3]:

myList = [1,2,3]


# # 1.insert 

# In[4]:

queue = deque(myList)


# In[6]:

queue.append(4)
print(queue)


# # 2.delete

# In[7]:

queue.popleft() 
print(queue)


# In[ ]:



