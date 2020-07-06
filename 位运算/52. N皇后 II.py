class Solution:
    def totalNQueens(self, n):
        if n < 1:return []
        self.count = 0
        path, cols, pie, na, = 0, 0, 0, 0
        self.traceback(0,n,cols,pie,na)
        return self.count
    def traceback(self,i,n ,cols,pie,na):
        if i >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1) # ==> if j not in cols or i+j not in pie or j -i not in na
        while bits:
            p = bits & (-bits)  #取最低位1       0b1111   #for i in range(n) 选列  选择
            bits = bits & (bits -1) #去除最低位1  0b1110
            self.traceback(i+1, n , cols|p ,(pie|p)<<1,(na|p)>>1)
                                #   0001     0010        0000

#(pie|p)<<1 p的左
#(na|p)>>1 p的右
#将 x 最高位至第 n 位（含）清零：x & ((1 << n) - 1)
#((1 << n) - 1)  ->前n位全为1
# x&(-x)
# x&(x-1)
#x >> 1
#x<< 1
#x&1
#x&-x=0