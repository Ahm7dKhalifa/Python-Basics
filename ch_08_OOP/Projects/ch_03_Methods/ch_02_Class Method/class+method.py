
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
     
    #class method : the first parameter is must reference to the class itself   
    @classmethod
    def restEmployeeCounter(cls):
        cls. employeeCounter = 0 


# In[2]:

print(Employee.employeeCounter)


# In[3]:

emp1 = Employee('ahmed',"khalifa")


# In[4]:

emp2 = Employee('ahmed_2',"khalifa_2")


# In[5]:

emp3 = Employee('ahmed_3',"khalifa_3")


# In[6]:

print(Employee.employeeCounter)


# # note : we call class method through one of the objects and effected on class itself and all another objects

# In[7]:

emp1.restEmployeeCounter()


# In[8]:

print(Employee.employeeCounter)
print(emp1.employeeCounter)
print(emp2.employeeCounter)
print(emp3.employeeCounter)


# In[ ]:



