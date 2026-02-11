from accounts import Accounts
        
bal = 100000
a1 = Accounts(bal)
run = True
while run:
    try:
        a1.trans()
    except Exception as e:
        print("An unexpected error occurred ",e)
    
    while True:
        try:
            f = int(input("Enter 4 to for more transactions or 5 to exit\n").strip())
        except ValueError:
                print("Enter valid input")
        if (f==4):
            break
        elif (f==5):
            print("Thank you, Exiting......")
            run = False
            break
        else:
            print("Wrong Input")
    
