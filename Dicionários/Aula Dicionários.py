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


# dic_even_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Cria dicionário com pares e ímpares de números na lista

# return_polygon(5)
# Retorna o polígono conforme o número de lados informados