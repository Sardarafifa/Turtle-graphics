MENU= {
    "espresso": {
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte": {
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "capuchino": {
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print("Sorry,can't process ur order")
            return False
    return True


def process_coins():
    """returns total coins payed by user"""
    print("insert coins")
    total= int(input("how many quarters?"))*0.25
    total+=int(input("how many dimes?"))*0.1
    total+=int(input("how many nickles?"))*0.05
    total+=int(input("how many pennies?"))*0.01
    return total



def is_transcation_successful(money_received,cost_of_drink):
    '''return true if order is accepted and return false if money is not sufficeint'''
    if money_received>=cost_of_drink:
        change=round(money_received-cost_of_drink,2)
        print(f"here is  ${change} change")
        global profit
        profit +=cost_of_drink 
        return True
    else:
        print("NOT ENOUGH MONEY")
        return False
    

def make_coffee(drink_name,order_ingredients):
    """if coffee is made then resources must be deducted accordingly from resources dict"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print("here is your order! enjoy!")
    

       
profit=0
resources= {
    "water":300,
    "milk":200,
    "coffee":100,
}  
machineison = True
while machineison:
    userorder = input("What do you like? (/espresso/latte/cappuccino/): ")
    print(userorder)
    if userorder == "off":
        machineison = False
    elif userorder == "report":
        print(f"""Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}""")
    else:
        drink= MENU[userorder]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            print(payment)
            if is_transcation_successful(payment,drink["cost"]): #if true then make coffee
                make_coffee(userorder,drink["ingredients"])


           
 

       
        


 

