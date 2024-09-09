def dic_even_and_odds(numbers):
    dict = {
        'evens': [],
        'odds': []
    }

    for num in numbers:
        if num % 2 == 0:
            dict['evens'].append(num)
        else:
            dict['odds'].append(num)
    print(dict)
    return


def return_polygon(number_of_sides):
    polygons = {
        3: "Triangle",
        4: "Square",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon"
    }
    try:
        print(polygons[number_of_sides])
        return polygons[number_of_sides]
    except KeyError:
        print("ta querendo demais")
    return


def phone_number_text_to_number():
    numbers = {
        "um": "1",
        "dois": "2",
        "três": "3",
        "quatro": "4",
        "cinco": "5",
        "seis": "6",
        "meia": "6",
        "sete": "7",
        "oito": "8",
        "nove": "9"
    }
    full_number = ""
    for i in range(9):
        number = input(f"Digit the {i + 1}º digit of your number in text format: ")
        full_number += numbers[number]

    print(full_number)
    return


# dic_even_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Cria dicionário com pares e ímpares de números na lista

# return_polygon(5)
# Retorna o polígono conforme o número de lados informados

phone_number_text_to_number()
# Escreva seu número por extenso e retorna os dígitos
