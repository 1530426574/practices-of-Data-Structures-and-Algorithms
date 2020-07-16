# counting sort


def counting_sort(array):
    length = len(array)
    output = [0] * length

    # initialize count array
    count = [0] * 256
    # store the count of each elements in count array
    # [4, 2, 2, 8, 3, 3, 1]
    for i in range(0, length):
        count[array[i]] = count[array[i]] + 1

    # find the index of each element of the original array
    # place the elements in output array

    # store the cummulative count
    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in range(length):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1  # 个数-1

    # i = length - 1
    # while i >= 0:   #关键在于理解 count[array[i]] ,值的个数
    #     output[count[array[i]] - 1] = array[i]
    #     count[array[i]] -= 1    #个数-1
    #     i = i - 1

    # copy the original array
    for i in range(0, length):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)
