# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]

# a = [[1,3],[2,6],[8,10],[15,18]]
# for x, y in a[1:]:
#     print(x, y )

class Solution:
    def merge(self, intervals:list) ->list:
        if not intervals:return []
        intervals.sort() #[[1, 3], [2, 6], [8, 10], [15, 18]]
        res = [intervals[0]]
        for x, y in intervals[1:]: #只要跟前面的区间比较就行。
            if res[-1][1] < x:     #右区间<左区间
                res.append([x,y])
            else:                  #右区间>= 左区间
                res[-1][1] = max(y, res[-1][-1])
        return res


def merge( intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][-1]:
            out[-1][-1] = max(out[-1][-1], i[1])
        else:
            print(out)
            out += i,
            print(out)
    return out
print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print([[1,3],[2,6],[8,10],[15,18]])
# print(a[1:])
# b = [1,2]
# x, y  = b
# print(x, y)

# a = [1,2],
# b = [3,4]
# print(b +a )

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
    if p1 < m:
        nums1[k:] = nums_copy[p1:]
    if p2 < n:
        nums1[k:] = nums2[p2:]

def merge1(nums1, m,nums2, n):
    nums_copy = nums1[:m]
    p1 = 0
    p2 = 0
    k  =  0
    while p1 < m and p2 < n :
        if nums_copy[p1] < nums2[p2]:
            nums1[k] = nums_copy[p1]
            p1 += 1
        else:
            nums1[k] = nums2[p2]
            p2 += 1
        k += 1  # k = p1 + p2
    if p1 < m:
        nums1[k:] = nums_copy[p1:]
    if p2 < n:
        nums1[k:] = nums2[p2:]
a = []
for i in range(9):
    a += i,
print(a)