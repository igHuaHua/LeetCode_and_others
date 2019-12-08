class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resHead = ListNode(0)
        curNode = resHead
        flag = 0
        while l1 or l2 or flag:
            tmp1 = l1.val if l1 else 0      # 最主要的就是对空的情况进行补零，减少额外的判断，更好的封装函数功能
            tmp2 = l2.val if l2 else 0
            ret = tmp1 + tmp2 + flag
            units = ret % 10
            flag = ret // 10
            curNode.next = ListNode(units)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curNode = curNode.next
        return resHead.next

a = ListNode(3)
# a.next = ListNode(4)
# a.next.next = ListNode(5)

b = ListNode(7)
b.next = ListNode(6)
# b.next.next = ListNode(5)
# b.next.next.next = ListNode(4)







