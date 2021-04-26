def sort(list):
    n_swaps = -1
    while n_swaps != 0:
        n_swaps = 0
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                n_swaps += 1

    return list
