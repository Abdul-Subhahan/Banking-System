
                   # Banking systems amount Credit and Debit  write a python code

class Bank:
    
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.bal=balance

    
    def Credit (self,amount):
        self.bal +=amount
        print("₹",amount,"was Credited")
        print("Total amount is:", self.get_bal())
    
    
    def Debit (self,amount):
        self.bal -=amount
        print("₹",amount,"was Debited")
        print("Total amount is:", self.get_bal())


    def get_bal (self):
        return self.bal
    

# Creating a object
acc=Bank(166132,55000)

acc.Credit(10000)
acc.Debit(5000)
