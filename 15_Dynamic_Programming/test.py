class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 边界判断：如果字符串s为空，则没有有效括号，返回0
        if not s:
            return 0
        n = len(s)
        max_length = 0
        cur_length = 0

        count = 0
        for i in range(0,n):
            if s[i] == '(':
                count += 1
                
            elif s[i] == ')':
                if count < 1:
                    count = 0
                    cur_length = 0
                else:
                    count -= 1
                    cur_length += 2
                    max_length = max(max_length,cur_length)
        
        return max_length

solution = Solution()
s1 = '(()'
s2 = ')()())'
s = '()(()'
s4 = ')())(()))()'
# result1 = solution.longestValidParentheses(s1)
# result2 = solution.longestValidParentheses(s2)
# result3 = solution.longestValidParentheses(s)
# result4 = solution.longestValidParentheses(s4)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 边界判断：如果字符串s为空，则没有有效括号，返回0
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        cur_length = 0

        count = 0
        for i in range(0,n):
            if s[i] == '(':
                count += 1
                cur_length = 0
                dp[i + 1] = 0
            elif s[i] == ')':
                if count < 1:
                    count = 0
                    cur_length = 0
                    dp[i + 1] = 0
                else:
                    count -= 1
                    cur_length += 2
                    dp[i + 1] = cur_length + dp[i + 1 - cur_length]
        
        return max(dp)
    
solution1 = Solution1()
result1 = solution1.longestValidParentheses(s1)
result2 = solution1.longestValidParentheses(s2)
result3 = solution1.longestValidParentheses(s)
result4 = solution1.longestValidParentheses(s4)
print(result1)
print(result2)
print(result3)
print(result4)