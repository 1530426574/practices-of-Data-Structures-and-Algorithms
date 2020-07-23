

class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0                #这点没有想到
        for bill in bills:
            if bill == 5:
                five += 1                  #如果收到5元，就+1
            elif bill == 10:               #如果是10元，没有5元，就return False,有5元，就找五元，相应的five -1 ，ten+1
                if  not five :return False
                five -= 1
                ten += 1
            else :                         #如果是20元，如果有10和5，那么ten-1，five-1 ，如果只有5元，那么five-3，其他的false
                if ten and five :          #这里用到了贪心，先找10，然后再整5
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else :
                    return False
        return True
"""
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lemonade-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""