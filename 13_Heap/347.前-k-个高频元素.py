#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
# 哈希表 + 最小堆：用python的defalutdict哈希表统计数字出现频率，再维护一个最小堆遍历所有（数字，频率）对，将（频率，数字）对加入到最小堆
# 中，堆会自动根据元组中的第一个元素调整堆结构，最后返回堆中的第二个元素即可
from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        nums_freq = defaultdict(int) # 不存在的键，其值就是0
        for num in nums: # O(N)
            nums_freq[num] += 1
        
        min_heap = []
        for key,value in nums_freq.items(): # O(M)
            if len(min_heap) < k:
                heapq.heappush(min_heap,(value,key)) # O(logk)
            else:
                if value > min_heap[0][0]:
                    heapq.heapreplace(min_heap,(value,key)) # O(logk)
        answer = [k for v,k in min_heap] # O(k)
        return answer
# 时间复杂度O(N * logK),哈希表统计频率O(N),设M为唯一数字集合大小，则维护最小堆需要O(M),每次堆调整最多需要O(logk),合计O(N * logk)
# 空间复杂度O(N),哈希表O(M).堆O(K),最坏情况下合计O(N)
# @lc code=end

# 用python内置计数器Counter,Counter经过了底层C语言的优化，因此尽管其理论复杂度与手写堆一致，但其实际执行效率更优
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_freq = Counter(nums) # 用python的Counter计数器统计数字频率，O(N)
        answer = [k for k,v in nums_freq.most_common(k)]
        return answer
# 时间复杂度O(N * logK)
# 空间复杂度O(N)

# 桶排序(Bucket sort)，由于数组长度为n,这意味着一个数字最多仅能出现n次，我们可以建立一个长度为n + 1的桶，
# 桶的每个位置初始化为空数组，桶的索引代表数字出现的频率，每个索引位置用于存储出现频率为该索引的数字
# 最后我们从后向前遍历桶，即可找出出现频率最高的数字了！
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1.统计频率
        n = len(nums)
        nums_freq = defaultdict(int) 
        for num in nums: # O(N)
            nums_freq[num] += 1
        # # 2. 创建“频率桶”，索引代表频率，值代表具有该频率的数字集合
        # 频率最大不会超过 len(nums)，所以建 len(nums) + 1 个空列表
        bucket = [[] for _ in range(n + 1)]
        # 3.把数字放到对应的桶里面去
        for num,freq in nums_freq.items(): # O(M)
            bucket[freq].append(num)

        # 3.从后往前遍历桶数组，取出前k个数
        answer = []
        for i in range(n,0,-1): # O(N)
            if bucket[i]:
                answer.extend(bucket[i])
            if len(answer) >= k:
                break # 长度一旦超过，直接break掉整个循环
        
        return answer[:k] # 返回前k个数字，防止数字数量超标 # O(K)
# 时间复杂度O(N),频率统计O(N),把数字放入桶中，O(M),倒序遍历桶O(N)，最坏O(N)
# 空间复杂度O(N),哈希表O(M),桶O(N)

# 方法四：快速选择（Quick select）
from collections import Counter
import random
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_freq = Counter(nums)
        unique_nums = list(nums_freq.keys())
        # 定义核心分区函数，函数接受分割区间[left,right],以及基准索引pivot_index，以pivot为基准进行
        # 划分，把大于等于pivot的值放在左边，否则放在右边，最后返回pivot基准值所在的位置索引
        def partition(left,right,pivot_index):
            # 先获取基准索引的频率值
            pivot_freq = nums_freq[unique_nums[pivot_index]]
            # 把基准值调换到数组最后面去，防止在后续调整过程中误伤到基准值
            unique_nums[pivot_index],unique_nums[right] = unique_nums[right],unique_nums[pivot_index]
            store_index = 0 # 用于存放下一个比pivot大的索引应该防止的位置
            for i in range(left,right): # 最后一个right不遍历，因为最后一个是基准值
                if nums_freq[unique_nums[i]] >= pivot_freq:
                    unique_nums[store_index],unique_nums[i] = unique_nums[i],unique_nums[store_index]
                    store_index += 1
            # 遍历结束，分割完成后，把基准值请回它应该在的位置，也就是store_index,因为此时(left,store_index）都是
            # 比pivot大的，而(store_index,right-1)都是比pivot小的
            unique_nums[store_index],unique_nums[right] = unique_nums[right],unique_nums[store_index]
            return store_index
        # 快速选择主干函数
        def quickselect(left,right,k_smallest):
            # 递归终止条件，如果区间只有一个元素，则它就是我们要找的元素
            if left == right:
                return 
            # 在(left,right)范围内随机选取基准值，避免每次选到极端最小\最大值，导致退化为O(N**2)
            pivot_index = random.randint(left,right)
            # 将刚刚选取好的基准索引传入partition函数进行分割操作，对数组排序
            pivot_index = partition(left,right,pivot_index)

            if pivot_index == k: # 当返回索引是k时，意味着前k个数一定比后面的数都大，也就是我们已经找到了前k个高频元素
                return
            if pivot_index < k: # 说明k的理想索引点在后面，对右半区进行排序
                quickselect(pivot_index + 1,right,k_smallest)
            if pivot_index > k: # 对左半区进行排序
                quickselect(left,pivot_index - 1,k_smallest)
        n = len(unique_nums)
        # 将（0,n - 1）传入参数，启动快速选择函数，递归对整个unique_nums数组作排序
        quickselect(0,n - 1,k - 1)
        # 数组前k个元素就是出现频率最高的k个元素
        return unique_nums[:k]
# 平均时间复杂度O(N)，由于我们进行了随机基准选取，假设每次我们索引取的是中点，调用一次partition之后，就会至少排除掉一个半区的元素
# 第一次调用需要进行N,然后是N/2,N/4,...1，等比数列求和最后为T(N) = 2N
# 最坏时间复杂度O(N**2)，每次pivot选取的是极小或极大值，则每次只能排除一个元素，则最坏情况下需要N,N-1,N-2,..1总共
# T(N) = N(N + 1)/2，也就是O(N**2)
# 最好情况下:每次pivot刚好选取的就是k - 1，此时一次遍历就找到答案，也就是O(N)
# 平均空间复杂度O(logN),每次pivot均匀切分，递归函数只调用logN 层
# 最坏空间复杂度O(N),每次只排除一个值，递归层数会达到N层




