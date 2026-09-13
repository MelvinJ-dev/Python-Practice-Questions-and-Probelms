## add the cost of the total elements in the cart

def calculator(cart):
    total_cost = 0
    for items in cart:
        total_cost+= items['price']*items['quantity']

    print(f'total cost in your cart is {total_cost}')


cart = [{'Name':'apple','price':100,'quantity':4},
        {'Name':'orange','price':300,'quantity':6},
        {'Name':'pineapple','price':200,'quantity':3},
        {'Name':'grapes','price':200,'quantity':5}
        ]
calculator(cart)