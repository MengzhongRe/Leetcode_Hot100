#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
# 双指针中心扩展法：当给定一个回文子串s[i:j]时，我们可以判断s[i - 1] 是否 == s[j + 1]，只要符合条件，则s[i-1:j+ 1]也是回文串，我们可以初始化左右指针，分别充当
# 待定回文串向左右拓展的检测指针，若符合条件则左右指针不停向两侧扩张，直到不是回文串为止。此时返回的就是以某个点为中心所形成的最长回文子串。回文子串可以是奇数、偶数
# 奇数时左右指针初始化为同一个下标；偶数时为相邻两个下标。若s长度为N，则一共有N个奇数中心店，N-1个偶数中心店，我们遍历完所有情况，取最大值即可，同时我们在while循环中
# 最后记录以该中心最长回文子串的起始点，从而返回目标子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 定义一个辅助函数，传入两个指针参数，left == right时表示以该指针为中心探测奇数回文子串，当right = left + 1时表示以二者为中心探测偶数回文子串
        def expandAroundCenter(left,right):
            # 只要左右指针不越界并且两个指针字符相等就再向左右两边扩展
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 在while循环结束时事实上多循环了一次。因此真实的回文子串起始点为left + 1,结束点为right - 1
            # 因此长度为right - 1 - (left + 1) + 1
            return left + 1,right - left - 1
        # 初始化全局变量用于记录当前最大回文子串
        start = 0
        max_len = 0
        # 遍历整个字符串下标
        for i in range(len(s)):
            # 搜索返回以i下标为中心的奇数最长回文子串
            l1,len1 = expandAroundCenter(i,i)
            # 搜索返回以i,i + 1下标为中心的偶数最长回文子串
            l2,len2 = expandAroundCenter(i,i + 1)
            # 若刷新了最大长度，旧更新最大长度及其起始点
            if len1 > max_len:
                max_len = len1
                start = l1
            # 若刷新了最大长度，旧更新最大长度及其起始点
            if len2 > max_len:
                max_len = len2
                start = l2
        
        return s[start:start + max_len]

# 时间复杂度o(n**2),外层循环N次，内层辅助函数循环最多也需要N次，因此是N**
# 空间复杂度o(1),只有常数个变量
# @lc code=end

# 动态规划版本:考虑二维动态规划数组定义为dp[i][j]表示s[i:j + 1]是回文子串，则考虑dp[i][j]若dp[i + 1][j - 1]且s[i] == s[j],则有dp[i][j] = True
# 考虑dp数组更新时需要左下角的值，因此外层行循环需要逆序遍历，内层则是正序遍历
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # 边界判断当s为空或只有一个时直接返回自身
        if n < 2:
            return s
        # 初始化全False的n*n dp数组
        dp = [[False] * n for _ in range(n)]
        # 初始化全局变量
        begin = 0
        max_length = 0
        # 主对角线上的当个字符肯定是回文子串
        for i in range(n):
            dp[i][i] = True
        # 行倒序遍历
        for i in range(n - 1,-1, -1):
            # 列正序遍历，只从i+ 1遍历
            for j in range(i + 1,n):
                if s[i] == s[j]:
                    # 如果s[i:j+1]为长度1,2,3则肯定是回文子串
                    if j - i <= 2:
                        dp[i][j] = True
                    # 否则需要看里面是不是回文子串
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    begin = i
        
        return s[begin:begin + max_length]

# 时间复杂度o(n**2),外层N次，内层最多需要N/2
# 空间复杂度O(N**2)


# 一维滚动数组优化：一维数组有两个注意点，一个是由于依赖于左下角的数据，因此我们内层必须倒序遍历，否则将会读取到本层的信息，另外，我们必须在s[i] != s[j]的时候dp[j] = False,否则dp[j]有可能带有
# 上一层留下来的旧信息为True,此时将会有问题。另外，当遍历到j == i时必须dp[j] = True
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # 边界判断当s为空或只有一个时直接返回自身
        if n < 2:
            return s
        
        dp = [False] * n

        begin = 0
        max_length = 1

        for i in range(n - 1,-1,-1):
            for j in range(n - 1,i - 1,-1):
                if j == i:
                    dp[j] = True
                elif s[i] == s[j]:
                    if j - i <= 2:
                        dp[j] = True
                    else:
                        dp[j] = dp[j - 1]
                if dp[j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    begin = i
        
        return s[begin:begin+max_length]
# 时间复杂度同上
# 空间复杂度o(n)
