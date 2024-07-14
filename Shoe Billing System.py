#Importing mysql and datetime module

from datetime import datetime
from datetime import date
import mysql.connector as sql

#Connecting Mysql

conn=sql.connect(host='localhost',user='root',passwd='iamakash',database='shoebilling')
if conn.is_connected():
    print("YOUR MySql CONNECTION IS SUCCESSFULLY ESTABLISHED!")
else:
    print("Error while estabilishing connection")

conn.autocommit=True
c1=conn.cursor()
########################




#Menu Function

def Menu():
    print("**************************************")
    print()
    print("MAIN MENU")
    print()
    print("1.Enter Details")
    print()
    print("2.Print Bill")
    print()
    print("3.Quit")
    print()
    print("**************************************")
    return 0

#Quit Function 

def Quit():
    breakpoint
    return 0

#New Login Function

def login():
    attempt=0
    for attempt in range(3):
        username=input("Enter the username: ")
        password=input("Enter the password: ")

        if(username!="Akash"):
            print("Wrong Username!!")
            attempt+=1
            print(3-attempt,"Attempts left!!")

        elif(username=="Akash" and password=="iamakash"):
            print("Logged in Successfully!!")
            Menu()
            break

        else:
            attempt+=1
            print(3-attempt,"Attempts left!!")
    else:
        print("Login Failed !!")
        quit()
    
login()



def enterdata():
    c1.execute("select max(Bill_no) from customers")
    myresult=c1.fetchone()
    Bill_no=myresult[0]
    if Bill_no==None:
        Bill_no=1
    else:
        Bill_no=Bill_no+1
    print("Bill No.: ", Bill_no)
    C_name=input("Enter Customers Name: ")
    C_mob=int(input("Enter Customers's Mobile Number: "))
    P_code=int(input("Enter Product Code: "))
    Qty=int(input("Enter Quantity: "))
    sql = "INSERT INTO customers (Bill_no, C_name, C_mob, P_code, Qty) VALUES (%s, %s, %s, %s,%s)"
    val = (Bill_no, C_name, C_mob, P_code, Qty)
    c1.execute(sql, val)
    conn.commit()

    def option():
        print("Do you want to enter more products to this order??")
        option=input("Y/y for Yes and N/n for No: ")
        return option 

    while True:
        option_input=option()
        if (option_input.lower()=="n"):
            print("Data Saved Successfully!")
            Menu()
            break

        elif (option_input.lower()=="y"):
            P_code=int(input("Enter Product Code: "))
            Qty=int(input("Enter Quantity: "))
            sql = "INSERT INTO customers (Bill_no, C_name, C_mob, P_code, Qty) VALUES (%s, %s, %s, %s,%s)"
            val = (Bill_no, C_name, C_mob, P_code, Qty)
            c1.execute(sql, val)
            conn.commit()
        else:
            print("Invalid input!! Please try again.")
        
            
        
    return 0






#Shop Name Printing in Output using asterisks

def shopname():
    print("\t\t\t\t**********************************************************")
    print("\t\t\t\t**********************************************************")
    print("\t\t\t\t**\t\t\t\t\t\t\t**") 
    print("\t\t\t\t**\t\t\tXYZ SHOE STORE\t\t\t**")
    print("\t\t\t\t**\t\t\t\t\t\t\t**") 
    print("\t\t\t\t**********************************************************")
    print("\t\t\t\t**********************************************************")
    return 0

#Bill Printing Function

def bill():
    shopname()
    now = datetime.now()
    today = date.today()
    time = now.strftime("%H:%M:%S")
    bill_no=input("Enter the bill number: ")

    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Bill No.: ",bill_no,"\t\t\t\t\t\t\t\t\t\t\t\t","Date: ",today)
    
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t Time:",time)

    cn = f"""select distinct C_name from customers where Bill_no = {bill_no}"""
    c1.execute(cn)
    result=c1.fetchall()
    for row in result:
        print("Customer's Name: ",str(row[0]))

    mn=f"""select distinct C_mob from customers where Bill_no = {bill_no}"""
    c1.execute(mn)
    result=c1.fetchall()
    for row in result:
        print("Customer's Mobile No. : ",str(row[0]))



    
    print()
  
    
    print("{:<90} {:<20} {:<20}".format("DESCRIPTION", "QTY", "PRICE"))
    
    
    query = f""" select store.Pname, customers.Qty, store.Price from customers join store on customers.P_code=store.P_code where customers.Bill_no = {bill_no}"""
    c1.execute(query)
    result=c1.fetchall()
    total=0
    for row in result:
        print("{:<90} {:<20} {:<20}".format(row[0],row[1],row[2]))
        total+=row[2]
        
    
   
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("{:<90} {:<20} {:<20}".format("","Total",total))

    choice1=input("Do you want to print more bills?\nPress Y/y for Yes and N/n for No: ")
    if(choice1.lower()=="y"):
        bill()
    elif(choice1.lower()=="n"):
        Menu()
    else:
        print("Wrong Input")
        breakpoint

    return 0





while True:
    choice=int(input("Enter choice: "))
    if(choice==1):
        enterdata()
    elif(choice==2):
        bill()
    elif(choice==3):
        print("Thank you !")
        quit()

