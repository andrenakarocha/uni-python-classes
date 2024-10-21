import math

def find_min (list):
    index_min = 0
    min = list[index_min]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            index_min = i
    return index_min

def very_bad_selection_sort(list):
    sorted_list = []
    while list:
        min = find_min(list)
        element = list.pop(min)
        sorted_list.append(element)
    return sorted_list


def bad_selection_sort(list):
    for i in range(len(list)):
        index_min = find_min(list[i:]) + i
        aux = list[i]
        list[i] = list[index_min]
        list[index_min] = aux
    return list


def bubble_sort(list):
    for j in range(len(list)):
        num_of_changes = 0
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                aux = list[i]
                list[i] = list[i + 1]
                list[i + 1] = aux
                num_of_changes += 1
        if num_of_changes == 0:
            break
    return list


def binary_sqrt_iterative(number):
    init = 0
    end = number
    while True:
        attempt = (init + end) / 2
        if attempt ** 2 > number:
            end = attempt
        else:
            init = attempt
        if end - init < 0.001:
            return attempt


def binary_sqrt_recursive(num, init, end):
    attempt = (init + end) / 2
    if attempt ** 2 > num:
        end = attempt
    else:
        init = attempt
    if end - init > 0.001:
        attempt = binary_sqrt_recursive(num, init, end)
    return attempt


def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    higher_numbers_list = [num for num in list if num > pivot]
    lower_numbers_list = [num for num in list if num < pivot]

    lower_numbers_sorted = quick_sort(lower_numbers_list)
    higher_numbers_sorted = quick_sort(higher_numbers_list)

    return lower_numbers_sorted + [pivot] + higher_numbers_sorted

def binary_search(list, number):
    if len(list) <= 1:
        print("NAO TA NA LISTA DAHHNNNN rOblOx eDgE")
        return

    init = 0
    end = len(list) - 1
    attempt = (init + end) // 2

    if list[attempt] == number:
        return attempt
    if list[attempt] < number:
        return binary_search(list[attempt + 1:], number)
    else:
        return binary_search(list[:attempt - 1], number)

