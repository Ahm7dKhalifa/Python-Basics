
# coding: utf-8

# # 1.add attributes for any objects with normal Method

# In[5]:

class Employee :
    def  __init__(self,firstName,lastName):
        self.firstName =firstName
        self.lastName = lastName
        
    def setFullName(self):
        self.fullName = self.firstName + " " + self.lastName
        
          


# In[7]:

emp1 = Employee('ahmed',"khalifa")


# In[9]:

print(emp1.firstName)


# In[10]:

print(emp1.lastName)


# In[12]:

#this well give error
#print(emp1.fullName)


# In[14]:

emp1.setFullName()


# In[15]:

print(emp1.fullName)


# # modify attributes that implement in normal method 

# In[16]:

emp1.fullName = "asd zxc"


# In[17]:

print(emp1.fullName)
print(emp1.firstName)
print(emp1.lastName)


# In[ ]:



