class CoffeeMaker:

    def __init__(self):
        self.resources={
            "water":300,
            "milk":200,
            "coffee":100
        }
#coffee maker report function
    def report(self):
        '''prints out quantity of resources '''
        for item in self.resources:
            print(f"{item.title()}: {self.resources[item]}")

    def is_resource_sufficient(self,drink):
        '''checks and returns if resources are sufficient to make drink'''
        can_make=True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make=False
        return can_make

    def refill(self,refill_resources):
        '''refills resources'''
        for item in self.resources:
            self.resources[item]+=refill_resources[item]

    def make_coffee(self,drink):
        '''makes coffee. essentially just removes the ingredients of the drink from the store resources'''
        for item in drink.ingredients:
            self.resources[item]-=drink.ingredients[item]
        print("Here is your coffee\nSee you tomorrow!!")