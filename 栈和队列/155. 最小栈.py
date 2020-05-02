class MinStack:
    """
    关键在哪呢???最小值如何保存，上一个最小值，与当前最小值。
    use the tuple to store the current data and curMin is really amazing
    """

    def __init__(self):
        self.stack = []

    def push(self, x):
        curmin = self.getmin()
        if curmin == None or x < curmin:
            curmin = x
        self.stack.append((x, curmin))

    def pop(self):
        self.stack.pop()

    def top(self):
        length = len(self.stack)
        if length == 0:
            return None
        else:
            return self.stack[length - 1][0]

    def getmin(self):
        length = len(self.stack)
        if length == 0:
            return None
        else:
            return self.stack[length - 1][1]

#
# class MinStack2:
#     """
#     关键在哪呢
#     use the tuple to store the current data and curMin is really amazing
#     """
#
#     def __init__(self):
#         self.stack = []
#         self.min = None
#
#     def push(self,x):
#         self.curmin = self.getmin()
#         if self.curmin == None:
#             self.min = x
#         elif x< self.min:
#             self.stack.append(self.min)
#             self.min = x
#         self.stack.append(x)
#
#
#     def pop(self):
#         item = self.stack.pop()
#         if item == self.min:
#             self.min = self.stack.pop()
#
#     def top(self):
#         return  self.stack[-1]
#
#     def getmin(self):
#         return self.min
#
