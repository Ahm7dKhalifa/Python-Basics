
# coding: utf-8

# # 1.add attributes for any objects with constructor

# In[7]:

class Employee :
    def  __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
        


# In[3]:

emp1 = Employee('ahmed',25,'ahm7dkhalifa@gmail.com')


# In[4]:

print(emp1.name)


# # 2.Modify Value of Instance Variable

# In[5]:

emp1.name = "asd"


# In[6]:

print(emp1.name)


# In[ ]:



