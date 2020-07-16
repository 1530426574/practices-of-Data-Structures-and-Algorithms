# insert sort gap = 1

def shell_sort(arr):
    length = len(arr)

    gap = length // 1

    while gap > 0:

        for i in range(gap, length):
            card = arr[i]
            j = i - gap  # 间隔gap 的上一个
            while j >= 0 and card < arr[j]:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = card
        gap //= 2
