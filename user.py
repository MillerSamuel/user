class User:
    def __init__(self,name):
        self.username=name
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        return self

    def withdrawl(self,amount):
        self.balance-=amount
        return self

    def user_balance(self):
        print(f"User:{self.username}  Balance:{self.balance}")
        return self
    
    def transfer(self,other_user,amount):
        self.balance-=amount
        other_user.balance+=amount
        return self

steve= User("Steve")
timmy=User("Timmy")
tom=User("Tom")

steve.deposit(150).deposit(100).deposit(50).withdrawl(50)

timmy.deposit(20).deposit(80).withdrawl(50).withdrawl(50)

tom.deposit(500).withdrawl(50).withdrawl(100).withdrawl(50).transfer(timmy,100)


steve.user_balance()
timmy.user_balance()
tom.user_balance()