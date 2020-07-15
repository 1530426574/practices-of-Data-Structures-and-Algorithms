#bucket sort

def bucket_sort(array):
    """
    关键在哪？？？每个buckets是有序的（一开始原始值和对应着索引来进行存储，），buckets里面的元素也是有序的
    [[1,2,3],[4,5,6],[7]]
    相当于把一堆无序的数字，放到固定有序的放数字的洞里面
    """

    bucket = []
    length = len(array)
    #create emepty buckets
    for i in range(length):
        bucket.append([])

    # array = [.42, .32, .33, .52, .37, .47, .51]
    # insert elements into their respective buckets
    for j in array:
        index = int(10 * j)
        bucket[index].append(j)

    #sort the elements of each bucket
    for i in range(length):
        bucket[i] = sorted(bucket[i])

    #get the sorted elements
    k = 0
    for i in range(length):   #总共有length个buckets,每个buckets是有序的，每个buckets的元素也是有序的，
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return  array






## Bucket Sort in Python


# def bucketSort(array):
#     bucket = []
#
#     # Create empty buckets
#     for i in range(len(array)):
#         bucket.append([])
#
#     # Insert elements into their respective buckets
#     for j in array:
#         index_b = int(10 * j)
#         bucket[index_b].append(j)
#
#     # Sort the elements of each bucket
#     for i in range(len(array)):
#         bucket[i] = sorted(bucket[i])
#
#     # Get the sorted elements
#     k = 0
#     for i in range(len(array)):
#         for j in range(len(bucket[i])):
#             array[k] = bucket[i][j]
#             k += 1
#     return array








