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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
cash_reserve = 0


def is_resource_sufficient(customer_choice):
    for item in MENU[customer_choice]['ingredients']:
        if MENU[customer_choice]['ingredients'][item] <= resources[item]:
            continue
        else:
            print(f"Sorry there is no enough {item} 🙁.")
            return False
    return True


def deduct_resources(customer_choice):
    for item in MENU[customer_choice]['ingredients']:
        resources[item] -= MENU[customer_choice]['ingredients'][item]


def calculate_coins(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

while is_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Cash Reserve: {cash_reserve}")
    elif customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        is_available = is_resource_sufficient(customer_choice)
        if is_available:
            quarters = int(input("How many Quarters? "))
            dimes = int(input("How many Dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total_sum = calculate_coins(quarters, dimes, nickles, pennies)
            if total_sum >= MENU[customer_choice]['cost']:
                deduct_resources(customer_choice)
                change_amount = round(total_sum - MENU[customer_choice]['cost'], 2)
                cash_reserve += MENU[customer_choice]['cost']
                print(f"Here is your ${change_amount} in change.")
                print(f"Here is your {customer_choice} ☕️. Enjoy!")
            else:
                print("Sorry! Money is not sufficient, And your money is refunded")
                is_on = False
        else:
            is_on = False




