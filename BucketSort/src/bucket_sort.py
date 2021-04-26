
# sorting a list of integers length n_digits
def sort(list):
    n_digits = len(list[0])

    for i in reversed(range(n_digits)):
        buckets = [ [] for _ in range(10) ]

        for number in list:
            digit = int(number[i])
            buckets[digit].append(number)

        list.clear()
        for bucket in buckets:
            for num in bucket:
                list.append(num)

    return list
