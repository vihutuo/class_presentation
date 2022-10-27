#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cl_pr
from IPython.display import clear_output
from colorama import Fore, Back, Style,init
import sys
def ShowMenu():
    print("1.View Student Details")
    print("2.Spend Tokens")
    print("0.Exit")
    c=int(input("Enter choice : "))
    return c
def ViewStudentDetails():
    student_id=int(input("Enter student id : "))
    try:
        x=cl_pr.GetStudentDetails(student_id)
        print(x)
        if x["tokens"] <=0:
           print(Fore.RED + "Token Balance : ",Fore.RED + str(x["tokens"]) )
          
        else:
           print(Fore.GREEN + "Token Balance : ",Fore.GREEN + str(x["tokens"]) )
        
    except:
        print("Connection error")
    try:
        cl_pr.ShowTokenTransactions(student_id)
    except:
        print("Connection error")
def SpendTokens():
    student_id=int(input("Enter student id : "))
    tokens=int(input("Enter tokens to spend : "))
    tokens=abs(tokens)
    try:
        x=cl_pr.AddTokens(student_id,-tokens,"Spend")
        print(x)
    except:
        print("Connection error")
ch =1
#init(autoreset=True) #colorama

while ch != 0:
    clear_output()
    ch=ShowMenu()
    sys.stdout.flush()
    if ch == 1:
        ViewStudentDetails()
        input("Press Enter to continue")
        
    elif ch == 2:
        SpendTokens()
        input("Press Enter to continue")
    elif ch == 0:
        pass
    else:
        print("Invalid choice")
print("Program ended")        


# In[2]:





# In[ ]:




