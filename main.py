from menu import Menu
from money_machine import MoneyMachine
from refill import Refiller
from coffee_maker import CoffeeMaker

menu=Menu()
money=MoneyMachine()
refill=Refiller()
coffee_maker=CoffeeMaker()
is_on=True
while is_on:
    options=menu.get_items()
    drink=input(f"What would you like to drink? {options}\n").lower()
    if drink=="report":
        coffee_maker.report()
        money.report()
    elif drink=="off":
        is_on=False
    elif drink=="refill":
        coffee_maker.refill(refill.resources)
    else:
        choice=menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(choice):
            money.make_payment(choice.cost)
            coffee_maker.make_coffee(choice)
