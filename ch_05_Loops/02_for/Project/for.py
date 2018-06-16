
# coding: utf-8

# # for with length of list

# In[2]:

myList = [ 'ahmed' , 'mohamed' , 'eisa', 'mousa']
for i in myList :
    print(i)


# In[3]:

myNumberList = [1,2,3,4,5,6,7,8,9]
for i in myNumberList :
    print(i)


# # for with range

# In[4]:

for i in range(1,10):
     print(i)


# In[5]:

for i in range(1,10,2):
     print(i)


# In[6]:

for i in range(len(myList)):
     print(i)


# # for with break

# In[8]:

for i in range(len(myList)):
    if( i < 2): 
        print(i)
    else:   
        break


# # for with continue
# 

# In[10]:

for i in range(len(myList)):
    if( i == 2): 
        continue
    print(i)   
        


# In[ ]:



