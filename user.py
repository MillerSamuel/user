class User:
    def __init__(self,name):
        self.username=name
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount

    def withdrawl(self,amount):
        self.balance-=amount

    def user_balance(self):
        print(f"User:{self.username}  Balance:{self.balance}")
    
    def transfer(self,other_user,amount):
        self.balance-=amount
        other_user.balance+=amount

steve= User("Steve")
timmy=User("Timmy")
tom=User("Tom")

steve.deposit(150)
steve.deposit(100)
steve.deposit(50)
steve.withdrawl(50)

timmy.deposit(20)
timmy.deposit(80)
timmy.withdrawl(50)
timmy.withdrawl(50)


tom.deposit(500)
tom.withdrawl(50)
tom.withdrawl(100)
tom.withdrawl(50)
tom.transfer(timmy,100)


steve.user_balance()
timmy.user_balance()
tom.user_balance()