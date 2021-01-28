
"""
题目：判断链表是否有环
leetcode地址：https://leetcode-cn.com/problems/linked-list-cycle/

思路：快慢指针法
1. 定义两个指针，一快一慢；
2. 慢指针每次只移动一步，快指针移动两步；
3. 若存在环，则快指针一定会追上慢指针，就说明存在环；

复杂度分析：
1. 时间复杂度：O(N),其中N是链表中的节点数。
    - 当链表中不存在环时，快指针到达链表尾部，结束；
    - 当链表中存在环时，快慢指针肯定都会走到环上，每一轮移动后，快慢指针的距离将减1，而初始距离为环的长度，因此最多移动N轮；
2. 空间复杂度：O(1),只使用了2个指针的额外空间。

思考：如何判断环的长度？
"""

# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        slow, fast = head, head
        if not head: # 确保列表不为空
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False