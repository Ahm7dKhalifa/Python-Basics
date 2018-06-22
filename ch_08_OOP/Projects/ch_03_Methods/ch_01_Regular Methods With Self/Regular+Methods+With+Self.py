
# coding: utf-8

# In[1]:

class Employee :
    #this is class variable
    employeeCounter = 0
    #constructor
    def  __init__(self,firstName,lastName):
        self.firstName =firstName
        self.lastName = lastName
        Employee.employeeCounter += 1
    #normal or regular method and the first parameter is must reference to the current obj      
    def setFullName(self):
        self.fullName = self.firstName + " " + self.lastName


# In[2]:

emp1 = Employee('ahmed',"khalifa")


# In[3]:

#call normal method without pass its object
emp1.setFullName()


# In[4]:

print(emp1.fullName)


# In[ ]:



