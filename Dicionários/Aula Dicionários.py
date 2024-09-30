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
        print("Not in dictonary")
    return


def phone_number_text_to_number():
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    full_number = ""
    try:
        for i in range(9):
            number = input(f"Digit the {i + 1}º digit of your number in text format: ")
            full_number += numbers[number]
        print(full_number)

    except KeyError:
        print("Not in dictionary")
    return


def text_to_emoji():
    dict_emojis = {
        "happy": "😀",
        'sad': "😢",
        "angry": "😠",
        "love": "😍",
        "scared": "😱",
        "think": "🤔",
        "laugh": "😂",
        "cool": "😎",
        "tired": "😴",
        "silly": "😜"
    }
    text = (input("How you feel? ")).split(" ")
    output = ""

    for i in range(len(text)):
        if text[i] in dict_emojis.keys():
            output += f" {dict_emojis[text[i]]}"
        else:
            output += f" {text[i]}"

    print(output)
    return output


def remove_accent(text):
    accents = {
        'á ã à â' : 'a',
        'ó ô õ' : 'o',
        'é ê' : 'e',
        'í î' : 'i',
        'ú ü' : 'u'
    }
    for key in accents.keys():
        for char in key:
            texto = texto.replace(char, accents[key])
    print(text)

    return

# dic_even_and_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Cria dicionário com pares e ímpares de números na lista

# return_polygon(5)
# Retorna o polígono conforme o número de lados informados

# phone_number_text_to_number()
# Escreva seu número por extenso e retorna os dígitos

# text_to_emoji()
# Transforma seu texto em emoji caso alguma palavra corresponda