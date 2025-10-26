class Bank:

    def __init__(self, balance: List[int]):
        self.balance = Counter(dict(enumerate([0]+balance)))

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        return self.withdraw(account1,money) and (self.deposit(account2,money) or not self.deposit(account1,money))

    def deposit(self, account: int, money: int) -> bool:
        return account<len(self.balance) and not self.balance.update({account:money})

    def withdraw(self, account: int, money: int) -> bool:
        return account<len(self.balance) and self.balance[account]>=money and not self.balance.update({account:-money})



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
