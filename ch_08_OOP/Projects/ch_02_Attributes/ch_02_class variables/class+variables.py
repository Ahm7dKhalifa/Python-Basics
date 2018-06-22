
# coding: utf-8

# In[1]:

class Employee :
    #this is class variable
    employeeCounter = 0
    def  __init__(self,firstName,lastName):
        self.firstName =firstName
        self.lastName = lastName
        Employee.employeeCounter += 1
        
    def setFullName(self):
        self.fullName = self.firstName + " " + self.lastName
        


# In[2]:

print(Employee.employeeCounter)


# In[3]:

emp1 = Employee('ahmed',"khalifa")


# In[4]:

emp2 = Employee('ahmed_2',"khalifa_2")


# In[5]:

print(Employee.employeeCounter)


# # we can acess and modify the class variable by the object not by class name but this well be not effected on any another objects

# In[6]:

emp1.employeeCounter = 100


# In[7]:

print(emp1.employeeCounter)
print(emp2.employeeCounter)
print(Employee.employeeCounter)


# In[ ]:



