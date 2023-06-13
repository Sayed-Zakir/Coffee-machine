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

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, we dont have enough {item}")
            return False
        else:
            return True
        
def process_coins():
    print("Please insert coins:")
    total = int(input("Enter your quarters: "))*0.25
    total += int(input("Enter your dimes: "))*0.1
    total += int(input("Enter your nickles: "))*0.05
    total += int(input("Enter your pennies: "))*0.01
    return total

def check_payment(payment, drink_cost):
    if payment<drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment>=drink_cost:
        change= round(payment-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name} ☕")

is_on=True
profit=0

while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g") 
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if check_resources(drink["ingredients"]):
            payments = process_coins()
            if check_payment(payments, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





