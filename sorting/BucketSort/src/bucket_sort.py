
# sorting a list of integers length n_digits
def sort(list, n_digits):

    for i in range(n_digits,0):
        buckets = [ [] for _ in range(10) ]

        for number in list:
            digit = int(number[i])
            buckets[i].append(number)

        list.append(buckets[i] for i in range(n_digits))

    print(list)
