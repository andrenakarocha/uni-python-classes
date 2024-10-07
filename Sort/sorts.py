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
    return


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
    return


