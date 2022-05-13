class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("Breson = 100")
        print("Shan = 200")
        print("Rigo = 300")

    def withdrawl1(self,breson):
        new_amount = 100 - breson
        print("You have withdrawn amount "+str(breson) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,shan):
        new_amount = 200 - shan
        print("You have withdrawn amount "+str(shan) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,rigo):
        new_amount = 300 - rigo
        print("You have withdrawn amount "+str(rigo) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to SBI Bank!")
    Account = input("Please enter your account number: ")
    Card_number = input("Insert your card number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add Breson")
        print("2. Add Shan")
        print("3. Add Rigo")
        choose = int(input("1. Add Breson  2. Add Shan 3. Add Rigo: "))
        if (choose == 1):
           breson = int(input("Enter the amount:- "))
           new_user.withdrawl1(breson)
        if (choose == 2):
           shan = int(input("Enter the amount:- "))
           new_user.withdrawl2(shan)    
        if (choose == 3):
           rigo = int(input("Enter the amount:- "))
           new_user.withdrawl3(rigo)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()