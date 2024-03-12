
# A code to convert a list into a linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

lst2link([1,4,53,2,9])
