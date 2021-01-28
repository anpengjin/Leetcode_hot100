
"""
题目：排序链表
leetcode地址：https://leetcode-cn.com/problems/sort-list/

思路：
解法一：
1. 题目中要求时间复杂度是nlogn，因而我们可以想到归并排序，首先得找到链表的中点；
2. 快慢指针，当快指针到末尾的时候，慢指针就到中间了，进行分割；
3. 对分割后的left和right进行递归排序；
4. 合并左右两边，首先创建一个头节点，各自遍历左右两边，哪边小，就加入到头节点的next里；
5. 最后判断左右两边，看哪边还有数据，加到next里；
6. 返回合并后的链表；

复杂度分析：
1. 时间复杂度：O(nlogn)
2. 空间复杂度：O(logn)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next
        



