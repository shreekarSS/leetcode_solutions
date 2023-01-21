# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the size of the LL, have a counter which is needed to remove the node
        # get the index where to remove the element from the rear of the LL
        # have a dummy node for the prev, iterate the curr head, if counter which acts as index, when
        # it is == to the to_remove index, remove it

        size = 0
        counter = 0
        tmp = head

        while tmp:
            size+=1
            tmp = tmp.next

        to_remove_index = size-n


        dummy = ListNode()
        dummy.next = head

        prev, curr = dummy, head

        while curr:
            if counter == to_remove_index:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            counter+=1


        return dummy.next

