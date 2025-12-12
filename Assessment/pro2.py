class ATM:
    def __init__(self):
        self.name = None
        self.mobile = None
        self.pin = None
        self.balance = 0
        self.transactions = []
    def activate_card(self):
        print("======ATM card activation=======")
        self.name = input("Enter your full name:")
        self.mobile = input("Enter your 10 digit mobile number")
        
        if not self.mobile.isdigit() or len(self.mobile) != 10:
            print("Invalid mobile number")
            return
        pin1 = int(input("Create 4 digit PIN"))
        Pin2 = int(input("Re-enter PIN"))
        if pin1 != Pin2:
            print("PINS do not match")
            return
        self.pin = pin1
        deposit = int(input("Enter initial deposit minimum $1000"))
        if deposit < 1000:
            print("Minimum 1000 required ")
            return
        self.balance = deposit
        self.transactions.append(deposit)
        print(f"Card Activated Successfully for {self.name}")
        print(f"Available Balance:{self.balance}")
    
    def varify_pin(self):
        entered_pin = int(input("Enter your 4-digit PIN:"))
        return entered_pin == self.pin
    
    def change_pin(self):
        print("====Change PIN ====")
        if not self.varify_pin():
            print("Incorrect PIN")
            return
    
        new_pin = input("Enter new 4-digit PIN ")
        self.pin = new_pin
        print("PIN changed sucessfully!")
    def deposit_money(self):
        print("====Deposit Money===")
        if not self.varify_pin():
            print("Incorrect PIN")
            return
        amount = int(input("Enter deposite amount"))
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        self.transactions.append(amount)
        print(f"{amount} deposited successfully! new Balance {self.balance}")
    def withdraw_money(self):
        print("===Withdraw Money===") 
        if not self.varify_pin():
            print("Incorrect PIN")
            return
        amount = int(input("Enter amount to withdraw"))
        if amount <= 0:
            print("Invalid amount") 
            return
        if amount > self.balance:
            print("Insufficient balance") 
            return

        if amount <= 1000:
            charge = 0
        elif amount <= 20000:
            charge = 100
        elif amount <= 1000000:
            charge = 1000
        else:
            pass
        total_deduction = amount + charge
        if total_deduction > self.balance:
            print("Insufficient balance ")
            return
        self.balance -= total_deduction
        self.transactions.append(charge)
        print("Remaining Balance",self.balance)
    def check_balance(self):
        print("check")