import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
}

def print_report(money):
    for key in resources:
        print(f"{key}: {resources[key][0]}{resources[key][1]}")
    print(f"Money: ${money}", end="")

def process_coins(order, money):
    print("Please insert coins.")
    nr_of_quarters = int(input("How many quarters?: "))
    nr_of_dimes = int(input("How many dimes?: "))
    nr_of_nickels = int(input("How many nickels?: "))
    nr_of_pennies = int(input("How many pennies?: "))
    coins = nr_of_quarters * 0.25 + nr_of_dimes * 0.10 + nr_of_nickels * 0.05 + nr_of_pennies * 0.01
    required_price = MENU[order]["cost"]

    if coins < required_price:
        print("Sorry that's not enough money. Money refunded.", end="")
        money -= required_price
    else:
        make_coffee(order)
        change = coins - required_price
        rounded_change = math.floor(change * 100) / 100
        print(f"Here is your ${rounded_change} in change.")
        print(f"Here is your {order}˗ˏˋ☕ˎˊ˗. Enjoy!", end="")
    return money

def make_coffee(order):
    if order == "espresso":
        resources["water"][0] -= MENU[order]["ingredients"]["water"]
        resources["coffee"][0] -= MENU[order]["ingredients"]["coffee"]
    elif order == "latte" or order == "cappuccino":
        resources["water"][0] -= MENU[order]["ingredients"]["water"]
        resources["coffee"][0] -= MENU[order]["ingredients"]["coffee"]
        resources["milk"][0] -= MENU[order]["ingredients"]["milk"]

def check_resources(order, money):
    if order == "espresso":
        if resources["water"][0] - MENU[order]["ingredients"]["water"] > 0 and \
                resources["coffee"][0] - MENU[order]["ingredients"]["coffee"] > 0:
            money += MENU[order]["cost"]
            money = process_coins(order, money)
        else:
            print("Sorry there is not enough ", end="")
            if resources["water"][0] - MENU[order]["ingredients"]["water"] <= 0:
                print("water", end="")
            if resources["coffee"][0] - MENU[order]["ingredients"]["coffee"] <= 0:
                print(", coffee")
    elif order == "latte" or order == "cappuccino":
        if resources["water"][0] - MENU[order]["ingredients"]["water"] > 0 and \
                resources["coffee"][0] -  MENU[order]["ingredients"]["coffee"] > 0 and \
                    resources["milk"][0] -  MENU[order]["ingredients"]["milk"] > 0:
            money += MENU[order]["cost"]
            money = process_coins(order, money)
        else:
            print("Sorry there is not enough ", end="")
            if resources["water"][0] - MENU[order]["ingredients"]["water"] <= 0:
                print("water", end="")
            if resources["milk"][0] - MENU[order]["ingredients"]["milk"] <= 0:
                print(", milk", end="")
            if resources["coffee"][0] - MENU[order]["ingredients"]["coffee"] <= 0:
                print(", coffee")

    return money

def coffee_machine(money):
    order = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if order == "report":
        print_report(money)
        coffee_machine(money)
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        money = check_resources(order, money)
        coffee_machine(money)
    elif order == "off":
        return
    else:
        print("Invalid input.")

money = 0
coffee_machine(money)

