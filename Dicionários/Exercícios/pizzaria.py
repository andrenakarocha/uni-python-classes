pizzas = {
    "Margherita": {
        "filling": "Mozzarella Cheese",
        "price": 8.99,
        "storage": 13
    },
    "Pepperoni": {
        "filling": "Pepperoni Slices",
        "price": 10.99,
        "storage": 6
    },
    "BBQ Chicken": {
        "filling": "Grilled Chicken, Red Onions",
        "price": 12.49,
        "storage": 3
    },
    "Veggie Supreme": {
        "filling": "Bell Peppers, Mushrooms, Olives",
        "price": 11.29,
        "storage": 20
    },
    "Hawaiian": {
        "filling": "Ham and Pineapple",
        "price": 9.49,
        "storage": 5
    },
    "Four Cheese": {
        "filling": "Mozzarella, Cheddar, Parmesan, Gorgonzola",
        "price": 13.99,
        "storage": 10
    }
}

cart = {
    'Pizzas' : {},
    'Total Price' : 0,
    'Address': {
        'Street' : '',
        'Number' : '',
        'State' : '',
        'City' : ''
    }
}


def force_option_in_dict(msg, dict, error_msg):
    option = input(msg)
    while not option in dict.keys():
        option = input(error_msg)
    return option

def force_option(msg, list, error_msg):
    option = input(msg)
    while not option in list:
        option = input(error_msg)
    return option

def force_number(msg, error_message):
    inpt = input(msg)
    while not inpt.isnumeric():
        inpt = input(error_message)

    inpt = int(inpt)
    return inpt


def show_pizzas():
    for pizza in pizzas.keys():
        print(f'-- {pizza} --')


def ask_pizza():
    while True:
        chosen_pizza = force_option_in_dict('What pizza would you like? ', pizzas, 'Sorry, we don´t have this pizza. Please select another one: ')

        print('Information about your chosen pizza: ')
        for key, value in pizzas[chosen_pizza].items():
            print(f'{key} - {value}')

        number_of_pizzas = force_number('How many pizzas would you like? ', 'That´s not a number!')
        remove_from_storage(chosen_pizza, number_of_pizzas)
        if chosen_pizza not in cart['Pizzas'].keys():
            cart['Pizzas'][chosen_pizza] = number_of_pizzas
        else:
            cart['Pizzas'][chosen_pizza] += number_of_pizzas

        cart['Total Price'] += pizzas[chosen_pizza]['price'] * number_of_pizzas

        choose = force_option('Would you like to ask for more pizzas? ', ['Yes', 'No'], 'That´s not an option! (Yes/No) ')
        if choose == 'Yes':
            continue
        else:
            checkout()
            break


def checkout():
    print('Cart: ')
    for pizza in cart['Pizzas'].keys():
        print(f'Pizza - {pizza} / Quantity - {cart['Pizzas'][pizza]}')

for option in cart['Address'].keys():
    inpt = input(f'Please, type your {option}: ')
    cart['Address'][option] = inpt



def remove_from_storage(chosen_pizza, number_of_pizzas):
    pizzas[chosen_pizza]['storage'] -= number_of_pizzas
    return


print('Welcome do MAMAMIA Pizzas! \nThis is our pizzas: ')
show_pizzas()
ask_pizza()