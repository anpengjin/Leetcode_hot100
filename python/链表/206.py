
"""
题目：反转链表
leetcode地址：https://leetcode-cn.com/problems/reverse-linked-list/

思路：
解法一：递归
1. 假设列表为：n1->n2->n3->...->n_k->n_k+1->...->n_m->null
2. 假设从n_k+1之后的链表已经反转：n1->n2->n3->...->n_k->n_k+1<-...<-n_m<-null
3. 我们希望n_k+1的下一个节点指向n_k，则：n_k.next.next = n_k
4. 要注意的是n_1的下一个必须指向null，如果你忽略了，可能会产生环

复杂度分析：
1. 时间复杂度：O(N),其中N是链表中的节点数。
2. 空间复杂度：O(N),由于使用递归，将会使用隐式栈空间，递归深度会达到n层。

解法二：迭代
1. 遍历列表时，将当前节点的next指向前一个元素，实现存储前一个元素，同时也要存储后一个

复杂度分析：
1. 时间复杂度：O(N),其中N是链表中的节点数。
2. 空间复杂度：O(1),只使用了2个指针的额外空间。

"""

# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一：递归
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur


# 解法二：迭代
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre