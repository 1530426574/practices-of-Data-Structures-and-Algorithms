nums = [4,3,2,1]
# 封装，
# 复用，
# 实现某个功能？

def add(nums,x =5):
    nums.sort()
    x +=1
    return x


print(add(nums,6))
print(nums)
