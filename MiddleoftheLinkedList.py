class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr = head
        length = 0
        while ptr != None:
            length += 1
            ptr = ptr.next
        length = (length//2)
        ptr = head
        for i in range(length):
            ptr = ptr.next
        return ptr
