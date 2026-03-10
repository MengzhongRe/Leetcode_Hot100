#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start
# 广度优先搜索 + 入度 + 邻接表
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 初始化入度数组和邻接表
        indegrees = [0] * numCourses  # 表示课程i 还需要几门先修课程，当入度为0时，表示课可以上了
        adjacency = [[] for _ in range(numCourses)] # 表示课程i 是哪些课程的先修课程，即课程i的后续课程有哪些

        # 填充入度数组和邻接表
        for cur,pre in prerequisites: # O（E）
            indegrees[cur] += 1
            adjacency[pre].append(cur) # pre是cur的先修课程，所以pre的后续课程有cur

        # 初始化队列，队列中的课程表示已经可以上（且未上过）的课程(即入度为0的课程)
        queue = deque()
        # 将所有入度为0的课程入队
        for i in range(numCourses): # O（V）
            if indegrees[i] == 0:
                queue.append(i)
        
        learned_courses = 0 # 记录已经上过的课程

        # 广度优先搜索：从可以上的课程开始上课(即入度为0的课程)
        while queue: # 队列不为空表示仍有可以上课的课程未上 O（V）
            course = queue.popleft() # 取出队列课程上课
            learned_courses += 1 # 已经上过的课程数加1

            for cur in adjacency[course]: # 因为已经上了该课程，所以遍历后续课程将后续课程的入度 - 1
                indegrees[cur] -= 1 # 同时如果某后续课程入度为0，即代表已经可以上课了，将其加入队列
                if indegrees[cur] == 0:
                    queue.append(cur)

        return learned_courses == numCourses
# 时间复杂度O（V+E）,所有节点（课程）最多入队出队即学习一次，且在初始化入度数组和邻接表时需要遍历所有的边（先修课程关系）
# 空间复杂度O(V + E)，入度数组和邻接表需要O(V)的空间，队列在最坏情况下需要O(V)的空间，邻接表中所有边需要O(E)的空间
# @lc code=end
# 用哈希表表示邻接表
from collections import deque,defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 初始化入度数组和邻接表
        indegrees = [0] * numCourses  # 表示课程i 还需要几门先修课程，当入度为0时，表示课可以上了
        adjacency = defaultdict(list) # 表示课程i 是哪些课程的先修课程，即课程i的后续课程有哪些

        # 填充入度数组和邻接表
        for cur,pre in prerequisites: # O（E）
            indegrees[cur] += 1
            adjacency[pre].append(cur) # pre是cur的先修课程，所以pre的后续课程有cur

        # 初始化队列，队列中的课程表示已经可以上（且未上过）的课程(即入度为0的课程)
        queue = deque()
        # 将所有入度为0的课程入队
        for i in range(numCourses): # O（V）
            if indegrees[i] == 0:
                queue.append(i)
        
        learned_courses = 0 # 记录已经上过的课程

        # 广度优先搜索：从可以上的课程开始上课(即入度为0的课程)
        while queue: # 队列不为空表示仍有可以上课的课程未上 O（V）
            course = queue.popleft() # 取出队列课程上课
            learned_courses += 1 # 已经上过的课程数加1

            for cur in adjacency[course]: # 因为已经上了该课程，所以遍历后续课程将后续课程的入度 - 1
                indegrees[cur] -= 1 # 同时如果某后续课程入度为0，即代表已经可以上课了，将其加入队列
                if indegrees[cur] == 0:
                    queue.append(cur)

        return learned_courses == numCourses
# 时间复杂度O（V+E）,所有节点（课程）最多入队出队即学习一次，且在初始化入度数组和邻接表时需要遍历所有的边（先修课程关系）
# 空间复杂度O(V + E)，入度数组和邻接表需要O(V)的空间，队列在最坏情况下需要O(V)的空间，邻接表中所有边需要O(E)的空间