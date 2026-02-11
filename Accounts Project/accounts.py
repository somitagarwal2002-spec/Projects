class Accounts:
    
    def __init__(self, bal):
        self.bal = bal
        
    def balance(self):
        print("Your current balance is ",self.bal)
        
    def credit(self, amount):
        if(amount <= 0):
            print("Enter positive debit amount")
            return
        elif (amount > 0):
            print(amount," is been credited")
            self.bal += amount
        #print("Your new balance is ",amount+bal)

    def debit(self, amount):
        if(amount <= 0):
            print("Enter positive debit amount")
            return
        elif (amount > self.bal):
            print("Insufficient balance")
        else:
            print(amount," is been debited")
            self.bal -= amount
        
        #print("Your new balance is ",amount+bal)
    def trans(amt):
        try:
            n = int(input("Choose 1 to credit ,2 to debit or 3 to check your balance\n").strip())
        except ValueError:
            print("Enter a valid input")
            return
        
        match n:
            case 1:
                try:
                    cr = float(input("Enter amount you want to credit\n"))
                except ValueError:
                    print("Enter valid input")
                amt.credit(cr)

            case 2:
                try:
                    de = float(input("Enter amount you want to debit\n"))
                except ValueError:
                    print("Enter valid input")
                amt.debit(de)
        
            case 3:
                amt.balance()
            
            case _:
                print("Wrong input")