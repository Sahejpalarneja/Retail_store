import sqlite3

conn = sqlite3.connect("BScooters.sqlite")
curr = conn.cursor()

#Function takes the name of the company,the bill number,date and total money for the order and 
#saves the order for te respective company in the details table
#if a new company is entered the fucntions asks for the details of the company and starts a new company template in details
def UpdateOrder(Company,date,Bill,total):
  

    curr.execute("SELECT COUNT(*) FROM Orders WHERE Company = ?;",(Company,))
    count = int(curr.fetchone()[0])
    if count > 0:
        curr.execute('''SELECT OrderID FROM Orders WHERE Company = ?;''',(Company,))
        order_id = curr.fetchone()[0]
        curr.execute('''SELECT Due FROM Orders WHERE Company = ?;''',(Company,))
        due = curr.fetchone()[0]
        owed  = float(input("Enter the Amount Paid: "))
        due = due + (total-owed)
        curr.execute('''SELECT Total FROM Orders WHERE Company = ?;''',(Company,))
        sum = int(curr.fetchone()[0])
        total = total+sum
        if due == 0:
            status = 0
        elif due<0:
            status = -1
        else:
            status = 1
        curr.execute("UPDATE Orders SET Due ="+str(due)+" WHERE Company =? ;",(Company,))
        curr.execute("UPDATE Orders SET Total = "+str(total)+" WHERE Company = ?;",(Company,))
        curr.execute("UPDATE Orders SET 'Status' = "+str(status)+" WHERE Company = ?;",(Company,))

        curr.execute("INSERT INTO Details('Id','Bill_Number','Date')VALUES(?,?,?);",(order_id,Bill,date))
        conn.commit()
        print("The Order has been added")
    else:
            print("You have entered a new company")
            order_id = int(input("Enter New OrderID: "))
            paid = float(input("Enter the amount paid:"))
            if total-paid == 0:
                status =0
            elif total-paid < 0:
                status = -1
            else:
                status = 1
            curr.execute('''INSERT INTO Orders('Company','Total','Due','OrderID','Status')VALUES(?,?,?,?,?);''',(Company,total,total-paid,order_id,status))
            curr.execute('''INSERT INTO Details('Id','Bill_Number','Date')VALUES(?,?,?);''',(order_id,Bill,date))
            conn.commit()
            print("The Order has been added")
    conn.close()

def AddOrder():
    Company = input("Enter the Company: ")
    Bill = input("Enter the Bill No.")
    date = input("Enter the date (yyyy-mm-dd):")
    Bill ="'"+Bill+"'"
    sql  = "CREATE TABLE {}('Sr No.' INTEGER,'Item' TEXT,'Quantity' INTEGER,'Per Piece' REAL,'Total' REAL,PRIMARY KEY('Sr No.' AUTOINCREMENT));".format(Bill)  
    curr.execute(sql)
    conn.commit()
    total = list()
    while(True):
        item = input("Enter the Item: ")
        try:
            quantity = int(input("Enter the quantity: "))
        except:
            print("Incorrect input")
            continue
        try:
            PerPiece = float(input("Enter the price: "))
        except:
            print("Incorrect input")
            continue
           
        total.append(PerPiece*quantity)
        curr.execute(" INSERT INTO "+Bill+"('Item','Quantity','Per Piece','Total')VALUES(?,?,?,?);",(item,quantity,PerPiece,quantity*PerPiece))
        conn.commit()
        choice = input("Press Y to continue")
        if choice == 'Y' or choice == 'y':
            continue
        else:
            UpdateOrder(Company,date,Bill,sum(total))
            break  
