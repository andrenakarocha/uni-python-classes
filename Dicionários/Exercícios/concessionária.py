import requests

cars = {
    'Honda Civic': {
        'power': '155 hp',
        'fuel_efficiency (km/l)': 11.5,
        'color': 'Silver',
        'year': 2022,
        'stock': 5,
        'price (R$)': 125000
    },
    'Toyota Corolla': {
        'power': '177 hp',
        'fuel_efficiency (km/l)': 12.0,
        'color': 'Black',
        'year': 2023,
        'stock': 3,
        'price (R$)': 145000
    },
    'Ford EcoSport': {
        'power': '137 hp',
        'fuel_efficiency (km/l)': 9.5,
        'color': 'White',
        'year': 2021,
        'stock': 4,
        'price (R$)': 99000
    },
    'Chevrolet Onix': {
        'power': '116 hp',
        'fuel_efficiency (km/l)': 14.0,
        'color': 'Red',
        'year': 2022,
        'stock': 7,
        'price (R$)': 75000
    },
    'Volkswagen Golf': {
        'power': '150 hp',
        'fuel_efficiency (km/l)': 10.5,
        'color': 'Blue',
        'year': 2023,
        'stock': 2,
        'price (R$)': 135000
    }
}

cart = {
    'Cars': {},
    'Total value': 0,
    'Information': {
        'Street': '',
        'Number': '',
        'ZIP': '',
        'Complement': ''
    }
}

YES_OR_NO = ['Yes', 'No']
USERS = ['Customer', 'Employee']


def force_option(msg, list, error_msg):
    user_input = input(msg)
    while user_input not in list:
        user_input = input(error_msg)
    return user_input


def verify_number(msg, error_msg):
    user_input = input(msg)
    while not user_input.isnumeric():
        user_input = input(error_msg)
    return int(user_input)


def list_cars():
    for elem in cars.keys():
        print(f"{elem} - Stock: {cars[elem]['stock']} - Value: {cars[elem]['price (R$)']}")


def register_address():
    while True:
        zip_code = input('Enter your ZIP code: ')
        url = f'https://viacep.com.br/ws/{zip_code}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            print(response)
            confirm = force_option('\nIs this your information? ', YES_OR_NO, '\nInvalid response! (Yes/No)')
            if confirm == 'Yes':
                cart['Information'] = response
            else:
                print('\nIncorrectly entered!')
                continue
        else:
            print('\nIncorrect ZIP code!')


def buy():
    while True:
        list_cars()
        choice = force_option('\nWhich car do you want? ', cars.keys(), '\nThis car is not in the catalog! ')
        if cars[choice]['stock'] == 0:
            print(f'\nWe no longer have {choice} in our stock! Please choose another car! ')
            continue

        qty = verify_number(f'\nHow many units of {choice} do you want? ', '\nInvalid response, enter a number! ')
        while qty > cars[choice]['stock']:
            print(f'\nWe don\'t have that quantity in our stock! ')
            qty = verify_number(f'\nHow many units of {choice} do you want? ', '\nInvalid response, enter a number! ')

        if choice in cart['Cars'].keys():
            cart['Cars'][choice] += qty
        else:
            cart['Cars'][choice] = qty

        cars[choice]['stock'] -= qty
        cart['Total value'] += cars[choice]['price (R$)'] * qty

        print('\nAdded to cart!')
        continue_shopping = force_option('\nDo you want to continue shopping? ', YES_OR_NO,'\nInvalid response! (Yes/No)')

        if continue_shopping == 'Yes':
            continue
        else:
            register_address()

            print(f'------------- \nYour cart:')
            for car in cart['Cars'].keys():
                print(f'{car} - Quantity : {cart["Cars"][car]}\n')
            print(f'\nTotal value: {cart["Total value"]}')
            print(
                f'\nThe delivery will be made to the address below: \nStreet: {cart["Information"]["Street"]}\nNumber: {cart["Information"]["Number"]}\nZIP: {cart["Information"]["ZIP"]}')
            break


def remove_car_admin():
    list_cars()
    car = force_option('\nWhich car do you want to remove? ', cars.keys(),'\nThis car doesn\'t exist!, enter a valid car: ')
    cars.pop(car, None)
    print('\nCar removed!')


def add_car_admin():
    name = input('\nEnter the car name: ')
    cars[name] = {}
    for info in cars['Chevrolet Onix'].keys():
        inpt = input(f'\nEnter the {info} of the car: ')
        if inpt.isnumeric():
            cars[name][info] = int(inpt)
        cars[name][info] = inpt
    print('\nCar added!')


def update_car_admin():
    list_cars()
    car = force_option('\nWhich car do you want to update? ', cars.keys(), '\nThis car is not in the catalog!')

    print('\nCurrent car information: ')
    for info in cars[car].keys():
        print(f'\n{info} = {cars[car][info]}')

    chosen_infos = []
    while True:
        chosen_info = force_option('\nWhich information do you want to change? ', cars[car].keys(),
                                   '\nThis is not valid information! Enter again: ')
        chosen_infos.append(chosen_info)
        continue_update = force_option('\nDo you want to change any more information? ', YES_OR_NO,'\nInvalid Response! (Yes/No)')
        if continue_update == 'Yes':
            continue
        else:
            break

    for info in chosen_infos:
        inpt = input(f'\nWhat will be the new {info}: ')
        if inpt.isnumeric():
            cars[car][info] = int(inpt)
        cars[car][info] = inpt

    print('\nCar updated!')


def admin():
    while True:
        print('''
Admin Menu:
    1 - Remove Car
    2 - Add Car
    3 - Update Car
''')

        choice = force_option('\nWhich option do you want? ', ['1', '2', '3'], '\nNot in the list, enter the correct number')

        match choice:
            case "1":
                remove_car_admin()
                continue
            case "2":
                add_car_admin()
                continue
            case "3":
                update_car_admin()
                continue


def main():
    user = force_option('What are you? (Customer / Employee): ', USERS, 'Invalid response! Choose a user: ')
    if user == 'Customer':
        buy()
    else:
        admin()


if __name__ == '__main__':
    main()
