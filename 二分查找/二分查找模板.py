array = [1,2,3,4,5,6,7,8,]         #001 单调
print(7>>1)
target = 6.6 #3.2
left,right = 0,len(array)-1       #002 边界
while left <= right:
    mid = left+ (right-left)>>2
    if array[mid] == target:      #003 可以通过索引访问
          break #or  return array[mid]
    elif target > array[mid]:    #夹逼
        left = mid + 1
    else:
        right = mid - 1


