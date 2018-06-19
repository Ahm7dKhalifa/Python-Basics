
# coding: utf-8

# # 1.Create List

# In[1]:

#1.1 by brackets


# In[2]:

list1 = [1,2,3,4]


# In[3]:

print(list1)


# In[4]:

list2 = [1,2.5,3+5j,"ahmed"]


# In[5]:

print(list2)


# In[6]:

#1.2 By Constructor


# In[7]:

list3 = list((1,2,3,"hello world"))


# In[8]:

print(list3)


# # 2.add Item

# In[10]:

list4 = [1,2,3,5]


# In[11]:

#1.add new item in last position


# In[12]:

list4.append(6)


# In[13]:

print(list4)


# In[14]:

#2.add new item in index position


# In[15]:

list4.insert(3,4)


# In[16]:

print(list4)


# In[17]:

#3.add iterable 


# In[18]:

list5 = [7,8,9,10]


# In[19]:

list4.extend(list5)


# In[20]:

print(list4)


# # 3.remove item

# In[21]:

#3.1 remove first item which match this value


# In[22]:

list6 = [ 1,2,3,4,1,2,3,4]


# In[23]:

list6.remove(1)


# In[24]:

print(list6)


# In[25]:

#3.2 remove item in certain index


# In[26]:

list6.pop(3)


# In[27]:

print(list6)


# # 4.information and access

# In[ ]:

#1.access


# In[28]:

x = list6[0]


# In[29]:

y = list6[1]


# In[30]:

z = x + y


# In[31]:

print(z)


# In[32]:

#2.update


# In[33]:

list6[2] = 100


# In[34]:

print(list6)


# In[37]:

#3.write in index out of range


# In[36]:

list6[6] = 1000


# In[38]:

#4.get size or length of the list


# In[39]:

print(len(list6))


# In[40]:

#5. number of copies of this value


# In[42]:

list6.count(3)


# In[ ]:




# # General Functions

# In[43]:

listWithDifferentTypes = [1,2,3,4,5,"ahmed","khalifa","zzz"]


# In[44]:

listOfString = ["ahmed","khalifa","zzz"]


# In[45]:

listOfNumber = [1,2,3,4,5]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



