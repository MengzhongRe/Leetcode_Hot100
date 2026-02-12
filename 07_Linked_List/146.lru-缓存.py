#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存
#

# @lc code=start
# 哈希表 + 双向链表实现O(1)的get 和 put操作
class DLinkedNode:
    """
    手动实现双向链表节点类
    """
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.capacity = capacity
        self.size = 0

        # 使用伪头部节点和伪尾部节点
        # 这样在添加和删除接节点的时候就不需要检查相邻节点是否存在
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head   

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
          # 如果 key 存在，通过哈希表定位节点
        node = self.cache[key]
         # 【关键步骤】因为被访问了，所以要移动到链表头部
        self.moveToHead(node)
        return node.value # 返回值

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            # 先初始化节点
            node = DLinkedNode(key,value)
            # 再把节点添加到链表开头
            self.addToHead(node)
            # 再把(key,node)键值对添加到内存当中
            self.cache[key] = node
            # 由于有新缓存加入，当前缓存规模+1
            self.size += 1
            
            # 核心逻辑：处理当添加完新键值对后，缓存爆满，需要把最久未用的节点删除，并删除其对应的哈希表的键值对
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key) # 删除节点对应的再哈希表中的键值对
                self.size -= 1 # 删除了之后也需要相应地减少缓存大小
        else:# 如果key已经存在，则先通过哈希表定位，再修改value,并移动到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
  
    def addToHead(self,node):
        """
        将节点添加到伪头部的后面
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self,node):
        """
        从链表中删除一个节点（断开指针）
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self,node):
        """
        将已存在节点移动到链表头部:先删除再，添加
        """
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        """
        淘汰最久未使用的节点，即删除链表尾部元素,同时返回删除的节点
        """
        node = self.tail.prev
        self.removeNode(node)
        return node 
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

# 用Python的collections 的 OrderedDict类简洁实现
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self,capacity):
        # 初始化父类
        super().__init__()
        self.capacity = capacity
    
    def get(self,key):
        if key not in self:
            return -1
        # 核心：因为被访问了，所以要变成最近使用的
        # 将key移动到有序字典的最右端（末尾）
        self.move_to_end(key)
        return self[key]
    
    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        
        # 更新或插入新的值（被插入的新值会自动追加在末尾）
        self[key] = value

        # 核心：检查容量
        if len(self) > self.capacity:
            # 容量超了，把最左端（开头）的那个删掉
            # last=False 表示弹出第一个被插入的（也就是最老的）
            self.popitem(last=False)
