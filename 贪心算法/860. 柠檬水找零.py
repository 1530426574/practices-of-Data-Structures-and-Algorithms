class Solution(object):  # aw
    def lemonadeChange(self, bills):
        five = ten = 0  # 这点没有想到
        for bill in bills:
            if bill == 5:
                five += 1  # 如果收到5元，就+1
            elif bill == 10:  # 如果是10元，没有5元，就return False,有5元，就找五元，相应的five -1 ，ten+1
                if not five: return False
                five -= 1
                ten += 1
            else:  # 如果是20元，如果有10和5，那么ten-1，five-1 ，如果只有5元，那么five-3，其他的false
                if ten and five:  # 这里用到了贪心，先找10，然后再整5
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
