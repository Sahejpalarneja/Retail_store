import sqlite3
import pandas as pd



conn = sqlite3.connect("BScooters.sqlite")
curr = conn.cursor()

   #Shows the history of all the orders
def ViewAll(): 
    print(pd.read_sql_query('''SELECT Orders.Company,Details.Bill_Number,Details.Date,Orders.Status
                        FROM Orders JOIN Details
                            ON Orders.OrderID = Details.Id;
                       ''',conn))

#shows the orders which have a pending payment
def ViewPending():
    try:
        print(pd.read_sql_query('''SELECT Orders.Company,Details.Bill_Number,Details.Date,Orders.Status
                        FROM Orders JOIN Details
                            ON Orders.OrderID = Details.Id
                            WHERE Status = 1;''',conn))
    except:
        print("No pending orders")

#show orders with completed payments
def ViewCompleted():
    try:
        print(pd.read_sql_query('''SELECT Orders.Company,Details.Bill_Number,Details.Date,Orders.Status
                        FROM Orders JOIN Details
                            ON Orders.OrderID = Details.Id
                            WHERE Status = 0;''',conn))
    except:
        print("No complted orders")


#Menu functions to execute the select queries
def ViewOrders():
    print("\t\t\t\t\MENU")
    print("\t\t\t\t1.View All orders")
    print("\t\t\t\t2.View Orders with Pending Payment")
    print("\t\t\t\t3.View Orders with Completed Payment ")
    switcher = {
            '1':lambda:ViewAll(),
            '2':lambda:ViewPending(),
            '3':lambda:ViewCompleted()
            }
    choice = input("Enter your choice")
    FUNC = switcher.get(choice,"Invalid Choice")
    print(FUNC())
       
#Shows the details of each order with then item names and other details,
def ViewOrderDetails():
    id = input("Enter the Bill Number")
    id = "'"+id+"'"
   
    try:
       
        print(pd.read_sql_query("SELECT * FROM "+id+";",conn))
        
       
    except:
        print("Bill Number not valid")