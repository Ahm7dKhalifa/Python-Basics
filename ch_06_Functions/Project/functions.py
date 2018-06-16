
# coding: utf-8

# # define function and call it 

# In[2]:

def printHello():
    print("hello")
    
    
printHello()
printHello()
    


# # function with parameters
# 

# In[4]:

def printMyName( name ):
    print( name )

myName = "ahmed"   
printMyName(myName)    


# # function with default values for parameters

# In[5]:

def printTheName( name = 'ahmed' ):
    print( name )

printTheName()    


# In[6]:

printTheName("ahmed khalifa") 


# # function with return

# In[7]:

def addTwoNumber(x,y):
    z = x + y
    return z

a = addTwoNumber(5,5)
print(a)


# # function with reference value 

# In[13]:

myList = [1,2,3,4,5]
for i in myList:
    print(i)


# In[15]:

def addItemsToList(yourList):
    yourList.insert(0,0)

addItemsToList(myList)
for i in myList:
    print(i)


# # primitive value VS reference value

# In[16]:

variable = 10
print(variable)


# In[21]:

def testchangeValue(myVariable):
    myVariable = 100
    
testchangeValue(variable)   
print(variable)


# # global vs local variable

# In[20]:

#global variable
x = 10
print(x)


# In[24]:

def global_VS_local():
    #local variable 
    x = 100

global_VS_local()   
print(x)  #global variable


# # local variable : define inside function and can not use inside anthor funcions  

# # global variable : define in main program and can use inside any funcions  

# In[26]:

globalVar = 10
def test1(x1):
    print(x1)
    
def test2(x2):
    print(x2)
    
test1(globalVar) 
test2(globalVar)


# In[27]:

def test3():
    localVariable = 123
    print(localVariable)
    
def test4():
    #localVariable is undefined
    print(localVariable)
    
test3()
test4()


# # Variable-length arguments

# In[32]:

def add(x , *list):
    print("this is x : ")
    print(x)
    for i in list:
        print("this is list item :") 
        print(i)

add(1,2)        


# In[33]:

add(1,2,3,4,5,6,7,8,9)


# In[ ]:



