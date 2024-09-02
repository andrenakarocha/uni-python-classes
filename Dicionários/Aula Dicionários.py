def dic_odd_and_evens(numbers):
    dic = {
        'odds': [],
        'evens': []
    }

    for num in numbers:
        if num % 2 == 0:
            dic['evens'].append(num)
        else:
            dic['odds'].append(num)
    print(dic)
    return

dic_odd_and_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])