class Solution:
    def plusOne(self, digits: list) :
        """
        关键在哪呢？？？ 用r 来确定从尾巴到前面一直连续的9的位置在哪结束。
        如果最后一位是9，如何处理，赋值为0，并向前递进
        # [9,9,9,9]
        # [8,9,9,9]
        # [8,8,9,9]
        # [8,8,8,9]
        https://leetcode-cn.com/problems/plus-one/
        """
        length = len(digits)
        r = length -1       #r = 3
        while digits[r] == 9:# [9,9,9,9]
            digits[r] = 0# [9,9,9,0]
            r -= 1        #r = 2
        if r < 0: # [9,9,9,9]
            digits[0]=1
            digits.append(0)  #32ms
            # digits = [1] + digits #44ms
        else: ## [8,9,9,9]  [8,8,9,9] [8,8,8,9] [8,8,8,8]
            digits[r] += 1
        return digits
