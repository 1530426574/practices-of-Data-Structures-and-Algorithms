def merge(nums1, m,nums2, n):
    nums_copy = nums1[:m]
    p1 = 0
    p2 = 0
    k  =  0
    while p1 < m and p2 < n :
        if nums_copy[p1] < nums2[p2]:
            nums1[k] = nums_copy[p1]
            p1 += 1
            k += 1
        else:
            nums1[k] = nums2[p2]
            p2 += 1
            k += 1
    if p1 < m:    #k 这个位置是下一位，没有填，同理，p1,p2 也是
        nums1[k:] = nums_copy[p1:]
    if p2 < n:
        nums1[k:] = nums2[p2:]








