from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def Coffee_Machine():
    is_machine_off = False

    while is_machine_off == False:
        available_drinks = menu.get_items()
        order = input(f"What would you like? ({available_drinks}): ")

        if order == "off":
            is_machine_off = True
        elif order == "report":
            coffe_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(order)
            is_order_available = coffe_maker.is_resource_sufficient(drink)
            if is_order_available == True:
                is_payment_enough = money_machine.make_payment(drink.cost)
                if is_payment_enough == True:
                    coffe_maker.make_coffee(drink)
Coffee_Machine()