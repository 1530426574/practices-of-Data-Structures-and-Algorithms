def partition(array, low, high):
    # 8 9 7 6 5 4 3 2 1 5  i= -1
    # 5 9 7 6 8 4 3 2 1 5  i = 0
    # 5 4 7 6 8 9 3 2 1 5  i = 1
    # 5 4 3 6 8 9 7 2 1 5 i = 2
    # 5 4 3 2 8 9 7 6 1 5  i= 3
    # 5 4 3 2 1 9 7 6 8 5 i= 4
    # 5 4 3 2 1 5 7 6 8 9
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pivot_poistion = partition(array, low, high)
        quick_sort(array, low, pivot_poistion - 1  )
        quick_sort(array, pivot_poistion + 1, high)


data = [8, 9, 7, 6, 5, 4, 3, 2, 1, 5]
size = len(data)
quick_sort(data, 0, size - 1)
print(data)


# Quick sort in Python
# Function to partition the array on the basis of pivot element
def partition(array, low, high):
    """
      # 1 2 3 7 8 4 5
    1 # 1 2 3 7 8 4 5  i= 0
    2 #1 2 3 7 8 4 5   i = 1
    3 # 1 2 3 7 8 4 5  i = 2
    7 # 1 2 3 7 8 4 5  i = 2
    8 # 1 2 3 7 8 4 5  i =2
    4 # 1 2 3 4 8 7 5  i = 3
      # 1 2 3 4 5 7 8
    """
    # Select the pivot element
    pivot = array[high]
    i = low - 1
    # 1 2 3 4 5

    # Put the elements smaller than pivot on the left and greater
    # than pivot on the right of pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        # Select pivot position and put all the elements smaller
        # than pivot on left and greater than pivot on right
        pi = partition(array, low, high)

        # Sort the elements on the left of pivot
        quickSort(array, low, pi - 1)

        # Sort the elements on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
