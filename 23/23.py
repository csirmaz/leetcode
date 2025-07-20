
# https://leetcode.com/problems/merge-k-sorted-lists/description/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out = None
        lastn = None
        while True:
            minv = None
            minix = None
            for ix, n in enumerate(lists):
                if n is not None:
                    if minix is None or minv > n.val:
                        minix = ix
                        minv = n.val

            # print(f"{minix}:{minv}")
            if minix is None:
                return out
            
            newn = ListNode(minv)
            lists[minix] = lists[minix].next
            if out is None:
                out = newn
                lastn = newn
            else:
                lastn.next = newn
                lastn = newn
