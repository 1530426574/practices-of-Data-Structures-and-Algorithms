def select_sort(arrs):
    length = len(arrs)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arrs[j] < arrs[min_index]:
                min_index = j
        arrs[i], arrs[min_index] = arrs[min_index], arrs[i]
    print(arrs)

A = [64, 25, 12, 22, 11]
select_sort(A)


