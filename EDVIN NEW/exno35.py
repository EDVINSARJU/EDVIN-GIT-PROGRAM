class bankdetail:
    def __init__(self,acct,name,accounttype):
        self.account=acct
        self.name=name
        self.accounttype=accounttype
        self.bal=0
    def showacctdetail(self):
        print("account holder name: ",self.name)
        print("account number", self.account)
        print("account type",self.accounttype)
        print("your account balance:",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def w(self,w1):
        self.bal=self.bal-w1
        return self.bal
name=(input("enter name"))
account=int(input("enter the acct number"))
accounttype=(input("enter the acct type"))
b=bankdetail(account,name,accounttype)
b.showacctdetail()
while[True]:
    print("\n menu")
    print("\n1 deposit")
    print("\n2 withdraw")
    c=int(input("enter the choice"))
    #d=0
    if(c==1):
        d=int(input("enter the amount to  deposit:"))
        print("total balance is :",b.dep(d))
    elif(c==2):
          w2=int(input("enter the amount to be withdrawn:"))
          if(w2>d):
              print("insufficient balance.")
          else:
              print("your total balance is:",b.w(w2))
    else:
        print("enter a valid choice.")
