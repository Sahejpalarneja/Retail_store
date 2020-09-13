import edits
import Views

#Menu function to call the view and edit fucntions from their imports
def MENU():
    while True:
        print("\t\t\t\t Menu")
        print("\t\t\t\t1.Add Order")
        print("\t\t\t\t2.View Orders ")
        print("\t\t\t\t3.View Order Details")
        switcher = {
              '1':lambda:edits.AddOrder(),
                '2':lambda:Views.ViewOrders(),
             '3':lambda:Views.ViewOrderDetails(),
                 '4':lambda:exit(0)
        }
        choice = input("Enter your choice: ")
        FUNC = switcher.get(choice,lambda:"ERROR")
        print(FUNC())
    


if __name__ == "__main__":
    
    print("\t\t\t\t\tBombay Scooters\n\n")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if(username == 'admin' and password == 'password'):
        MENU()
    else:
        print("Wrong password or username")
