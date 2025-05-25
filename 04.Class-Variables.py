class Bank:
    bank_name = "Askari Bank"  

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  
acc1 = Bank("Alice")
acc2 = Bank("Bob")


print(acc1.bank_name)  
print(acc2.bank_name)  


Bank.change_bank_name("Meezan Bank")


print(acc1.bank_name)  
print(acc2.bank_name)  
