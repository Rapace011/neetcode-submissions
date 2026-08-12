# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        node = head

        while node:
            list.append(node.val)
            node = node.next

        l = 0
        r = len(list)-1

        while l <= r:
            if list[l] != list[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
