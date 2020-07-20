"""
我们也可以用下面的表格来表示这个自动机：

          ' '	+/-	number	other
start	start	signed	in_number	end
signed	end	end	in_number	end
in_number	end	end	in_number	end
end	end	end	end	end
"""

INT_MAX = 2 ** 31 -1
INT_MIN = -2 ** 31

class Automation:
    def __init__(self):
        self.state = 'start'
        self.sign =  1
        self. ans = 0
        self.table = {
            'start':['start', 'signed','in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c:str):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state =='in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else
            min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if 'c' == '+' else -1
#-12345
class  Solution:
    def my_atoi(self, str: str):

        automation = Automation()

        for c in str:
            automation.get(c)
        return  automation.sign * automation.ans


import re
class Solution1:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[+-]?\d+', s.lstrip())), 2**31 - 1), -2**31)




