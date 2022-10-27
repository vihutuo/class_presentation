import cl_pr
from IPython.display import clear_output
from colorama import Fore, Back, Style,init
import sys
def ShowMenu():
    print("1.View Student Details")
    print("2.Spend Tokens")
    print("3.Show Recent Transactions")
    print("4.Show Total Tokens Issued")
    print("0.Exit")
    sys.stdout.flush()
    c=int(input("Enter choice : "))
    return c
def ViewStudentDetails():
        student_id=int(input("Enter student id : "))
        try:
            x=cl_pr.GetStudentDetails(student_id)
        except:
            print("Connection Error")
            return
        if x["status"] == 1:
            if x["tokens"] is None:
                x["tokens"] = 0
            if x["total_tokens_earned"] is None:
                x["total_tokens_earned"] = 0    
            if x["tokens"] <=0:
               print(Fore.RED + "Token Balance : ",Fore.RED + str(x["tokens"]) )

            else:
               print(Fore.GREEN + "Token Balance : ",Fore.GREEN + str(x["tokens"]) )
            print(Fore.BLACK)
        print(x)
        #print("Connection error")
        try:
            cl_pr.ShowTokenTransactions(student_id)
        except:
            print("Connection Error")
            return    
            
   
        #print("Connection error")
def SpendTokens():
    student_id=int(input("Enter student id : "))
    tokens=int(input("Enter tokens to spend : "))
    tokens=abs(tokens)
    try:
        x=cl_pr.AddTokens(student_id,-tokens,"Spend")
        print(x)
    except:
        print("Connection error")
def ShowRecentTransactions():
    try:
        cl_pr.ShowRecentTokenTransactions(50)
        
    except:
        print("Connection error")  
def ShowTotalTokensIssued():
    try:
        cl_pr.ShowTotalTokensIssued()
        
    except:
        print("Connection error")        
                
        
ch =1
#init(autoreset=True) #colorama

while ch != 0:
    clear_output()
    ch=ShowMenu()
   
    if ch == 1:
        ViewStudentDetails()
        input("Press Enter to continue")
        
    elif ch == 2:
        SpendTokens()
        input("Press Enter to continue")
    elif ch == 3:
        ShowRecentTransactions()
        input("Press Enter to continue")
    elif ch == 4:
        ShowTotalTokensIssued()
        input("Press Enter to continue")     
    elif ch == 0:
        pass
    else:
        print("Invalid choice")
print("Program ended")        