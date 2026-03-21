#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        # 栈中同时存储当前元素和截止目前为止的最小值两个状态
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 如果栈里已经有元素了，当前的最小值 = min(进来的值, 之前的历史最小值)
        # self.stack[-1][1] 拿到的就是上一个元素的“历史最小值存档”
        if not self.stack:
            self.stack.append((val,val))
        else:
            current_min = min(val,self.stack[-1][-1])
            self.stack.append((val,current_min))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
     

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][-1]   

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # 新的栈中元素的最小值由旧的最小值和新push值的最小值决定
        self.min = min(self.min,val)
        

    def pop(self):
        """
        :rtype: None
        """
        poped_val = self.stack.pop()
        # 剪枝：1.如果poped_val > self.min，则说明栈中的最小值没有变化
        # 2.因此只有在二者相等时，才需要更新最小值
        if poped_val == self.min:
            self.min = min(self.stack) if self.stack else float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min