def merge_sort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        merge(arr, l, r)

        # i = j = k = 0
        # m, n  = len(l), len(r)
        # while i < m and j < n :
        #     if l[i] < r[j]:
        #         arr[k] = l[i]  # 谁小就先填谁
        #         i += 1  # 填完之后+1,为了比较后面的
        #     else:
        #         arr[k] = r[j]
        #         j += 1
        #     k += 1  # 往arr里填空 k = i +j     #k 这个位置是下一位，没有填，同理，i, j也是
        #
        # if i < m:
        #     arr[k:] = l[i:]
        # if j < n:
        #     arr[k:] = r[j:]


def merge(nums, nums1, nums2):
    i = j = k = 0
    m, n = len(nums1), len(nums2)
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums[k] = nums1[i]  # 谁小就先填谁
            i += 1  # 填完之后+1,为了比较后面的
        else:
            nums[k] = nums2[j]
            j += 1
        k += 1  # 往arr里填空 k = i +j     #k 这个位置是下一位，没有填，同理，i, j也是
    if i < m:
        nums[k:] = nums1[i:]
    if j < n:
        nums[k:] = nums2[j:]

        # while i < len(l):  # 填后面剩余的
        #     arr[k] = l[i]
        #     i += 1
        #     k += 1

        # while j < len(r):
        #     arr[k] = r[j]
        #     j += 1
        #     k += 1


# # Python program for implementation of MergeSort
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2  # Finding the mid of the array
#         L = arr[:mid]  # Dividing the array elements
#         R = arr[mid:]  # into 2 halves
#
#         mergeSort(L)  # Sorting the first half
#         mergeSort(R)  # Sorting the second half
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# MergeSort(A, p, r):
# if p > r
#     return
# q = (p + r) / 2
# mergeSort(A, p, q)
# mergeSort(A, q + 1, r)
# merge(A, p, q)
#
#
# # Code to print the list
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # driver code to test the above code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     mergeSort(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)

# This code is contributed by Mayank Khanna
