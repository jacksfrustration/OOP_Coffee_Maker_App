class MoneyMachine:

    CURRENCY="£"
    COIN_VALUES={
        "quarters":0.25,
        "dimes":0.1,
        "nickles":0.05,
        "pennies":0.01
    }

    def __init__(self):
        self.profit=0
        self.money_received=0


    def report(self):
        '''pribts out report of profit'''
        print(f"Profit of {self.CURRENCY}{self.profit}")

    def process_coins(self):
        '''processes coins received and returns total value'''
        for coin in self.COIN_VALUES:
            self.money_received+=int(input(f"How many {coin}?\n"))*self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self,cost):
        '''checks if money received is more or equal to the cost of the drink. returns change
        and returns boolean value if the money was enough for the cost'''
        money_received=self.process_coins()
        if money_received>=cost:
            change=round(money_received - cost,2)
            print(f"Here is {self.CURRENCY}{change} in change\n")
            self.profit+=cost
            self.money_received=0
            return True
        else:
            print("Sorry that is not enough money")
            self.money_received=0
            return False
