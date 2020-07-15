#radix sort
#121
def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    #caculate count of elements
    for i in range(0, size):
        index = array[i]//place % 10
        count[index] += 1

    # caculate cummulatice count
    for i in range(1, 10):
        count[i] += count[i - 1]
    #place the elements sorted order

    i = size - 1
    while i >= 0:
        index = (array[i] // place) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
    # return array


#main function to implement radix sort
def radix_sort(array):
    #get maximum element
    max_element = max(array)
    #apply counting sort to sort elentment based on place value
    place = 1
    print(counting_sort(array, 1))
    print(counting_sort(array, 10) )
    print(counting_sort(array, 100))
    # while max_element // place > 0:
    #     counting_sort(array, place)
    #     place *= 10
data = [121, 432, 569, 23, 9, 45, 788]
radix_sort(data)
# print(data)