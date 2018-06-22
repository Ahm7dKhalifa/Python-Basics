
# coding: utf-8

# In[12]:

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
    
    #static method : the first parameter is (not) reference to the class or the object   
    @staticmethod
    def calculateTwoNumber(x,y):
        return x + y
    


# In[11]:

add = Employee.calculateTwoNumber(10,2)
print(add)


# In[2]:

emp1 = Employee('ahmed',"khalifa")


# In[5]:

addFromObj = emp1.calculateTwoNumber(10,2)
print(addFromObj)


# In[ ]:



