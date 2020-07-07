def bubble_sort(arrs: list):
    length = len(arrs)

    for i in range(length):
        for j in range(length-i-1):                     #traverse
            if arrs[j] > arrs[j+1]:                     #compare
                arrs[j], arrs[j+1] = arrs[j+1], arrs[j] #swap
    return arrs


arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))

