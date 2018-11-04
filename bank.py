class Account:
    cbname = "sbi"

    def __init__(self, cname, cadd, cacno, cbal):

        self.cnmae = cname
        self.cadd = cadd
        self.cacno = cacno
        self.cbal = cbal
        check = False
        if (cbal <= 0):
            print("The Initial balcance was invalid")
            cbal = 0
        print(cname, cadd, cacno, cbal)

    def credit(self, cram):
        # adding money
        check = False
        print("in credit")
        self.cbal += cram
        print("Balance is credited with " + str(cram), "new balance is " + str(self.cbal))
        check = True;
        return (check)

    def debit(self, dbamt):
        # debit shoud not exceed the Account's balance
        rt = False
        print("in debit")
        if (dbamt > self.cbal):
            print("Debit amount is more than Account balance")
        else:
            self.cbal -= dbamt
            print("Balance is debited with " + str(dbamt), "new balance is " + str(self.cbal))
            rt = True
        return rt

    def getbalance(self):
        # print avalable balance
        print("balance")
        print("Available balance is " + str(self.cbal))


class SavingAccount(Account):
    def __init__(self, cname, cadd, cacno, cbal, interest):
        self.cbal = cbal
        self.interest = interest
        super().__init__(cname, cadd, cacno, cbal)

    def calinterest(self, cbal, nm):
        # calculate interest
        self.p = cbal
        self.t = nm
        self.r = self.interest
        self.a = self.p * (1 + (self.r / 100) * self.t)
        self.i = self.a - self.p;
        print("earned interest is " + str(self.i), self.credit(self.i))


class CheckingAccount(Account):
    def __init__(self, cname, cadd, cacno, cbal, tc):

        self.tc = tc
        super().__init__(cname, cadd, cacno, cbal)

    def debit(self, damt):
        self.damt = damt;
        check = super(CheckingAccount, self).debit(self.damt)
        if (check):
            self.cbal -= self.tc
            print("A transcation of Rs" + str(self.tc),
                  "is charged for previous transaction Available balance is" + str(self.cbal))

    def credit(self, cram):
        self.cramt = cram
        check = super(CheckingAccount, self).credit(self.cramt)
        if (check):
            self.cbal -= self.tc
            print("A transcation charge of Rs" + str(self.tc),
                  "is charged for previous transaction Available balance is" + str(self.cbal))


class CurrentAccount(Account):
    def __init__(self, cname, cadd, cacno, cbal, obal):
        self.obal = obal
        self.cbal = cbal
        super().__init__(cname, cadd, cacno, cbal)

    def debit(self, dbamt):
        if (dbamt <= (self.cbal + abs(self.obal))):
            self.cbal -= dbamt
            print("Account is debited with rs " + str(dbamt), "Available balance is " + str(self.cbal))
            if (self.cbal < 0):
                print("Account balance is in Overdraft ")
        else:
            print("Debit amount is exceeding the Overdraft limit")


a1 = Account("Avdhesh", "punjab", 1000, 2000)
a1.debit(500)
a1.debit(5000)
a1.credit(3000)
a1.getbalance()

b1 = SavingAccount("Rahul", "Ludhiana", 2000, 3000, 5)
b1.calinterest(3000, 10)
b1.credit(1000)
b1.debit(1000)

c1 = CheckingAccount("Abhishek", "Delhi", 1000, 2000, 10)
c1.debit(1000)
c1.credit(2000)
c1.getbalance()

d1 = CurrentAccount("Sandeep", "UP", 2000, 1000, 5000)
d1.credit(2000)
d1.debit(8000)
d1.debit(5000)
d1.getbalance()
