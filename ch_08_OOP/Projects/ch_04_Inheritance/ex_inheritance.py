
# coding: utf-8

# In[42]:

class Employee:
    
    employeeCounter = 0;
    
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        Employee.employeeCounter += 1
        print(" hello i employee")
       
      
    def displayEmployeeName(self):
        print(self.firstName + " " + self.lastName)
        
    def displayHello(self):
        print("hello from Employee class")
        


# In[3]:

emp = Employee("ahmed","khalifa")


# In[4]:

print(Employee.employeeCounter)


# In[5]:

emp.displayEmployeeName()


# # ex_01.Inheritance

# In[6]:

class Developer(Employee):
    pass


# # 1.1 take care with constructor parameters of parent

# In[7]:

dev = Developer()


# In[8]:

dev = Developer("ahmed","khalifa")


# # 1.2 working with class variable in Inheritance

# In[9]:

print(Employee.employeeCounter)


# In[10]:

print(Developer.employeeCounter)


# In[11]:

Developer.employeeCounter = 10


# In[12]:

print(Developer.employeeCounter)


# In[13]:

print(Employee.employeeCounter)


# # 1.3 working with instance variable in Inheritance

# In[14]:

print(dev.firstName)


# # 1.4 working with Methods in Inheritance

# In[15]:

dev.displayEmployeeName()


# # ex_02.Inheritance
# 

# In[43]:

class SoftwareEngineer(Employee):
    employeeCounter = 0
    def __init__(self, fullName,department):
        self.fullName = fullName
        self.department = department
        SoftwareEngineer.employeeCounter += 1
        print(" i am software engineer ")
    def displaySoftwareEngName(self):
        print(self.fullName + " worked at " + self.department )
        


# # 2.1 take care with constructor parameters 

# In[44]:

sw = SoftwareEngineer("ahmed khalifa","web")


# In[18]:

print(SoftwareEngineer.employeeCounter)


# In[19]:

print(Employee.employeeCounter)


# In[20]:

emp3 = Employee("a","z")


# In[21]:

print(SoftwareEngineer.employeeCounter)


# In[22]:

print(Employee.employeeCounter)


# In[23]:

print(Developer.employeeCounter)


# In[24]:

dev2 = Developer("zxc" , "asd")


# In[25]:

print(Employee.employeeCounter)
print(Developer.employeeCounter)
print(SoftwareEngineer.employeeCounter)


# # 2.3 working with instance variable in Inheritance

# In[31]:

print(sw.fullName)


# In[32]:

print(sw.firstName)


# # 2.4 working with Methods in Inheritance

# In[33]:

sw.displaySoftwareEngName()


# In[34]:

sw.displayEmployeeName()


# In[45]:

sw.displayHello()


# # ex_03_Inheritance

# In[73]:

class Desinger(Employee):
     def __init__(self,age,firstName,department,lastName):
        self.age = age    
        self.firstName = firstName
        self.department = department
        self.lastName = lastName
        print(" hello i designer")


# In[75]:

d = Desinger(25,'lala','photoshop','nana')


# In[76]:

d.displayEmployeeName()


# In[ ]:



