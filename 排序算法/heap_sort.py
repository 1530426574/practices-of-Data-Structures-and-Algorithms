# heap sort in python

def heapify(arr, n, i):
    """
    find the largest among root node and their children,
    and then swap the largest with root node,
    continue heapifying if root is not largest
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    elif r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # swap,


def heap_sort(arr: list):
    n = len(arr)

    # build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        # heap root element
        heapify(arr, i, 0)


arr = [1, 12, 9, 5, 6, 10]
heap_sort(arr)
print(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')
