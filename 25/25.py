
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

def p(n):
    if n is None: return 'None'
    return n.val

class Solution:


    def rev1group(self, head: ListNode, k: int):
        n1 = head
        n2 = head.next
        # print(f"R1 {p(n1)} -> {p(n2)}")
        if n2 is None: return {'reversed':1, 'new_first':n1, 'after_last':None}
        for i in range(k-1):
            n3 = n2.next
            n2.next = n1
            if n3 is None: return {'reversed':i+2, 'new_first':n2, 'after_last':None}
            n1 = n2
            n2 = n3
        return {'reversed':k, 'new_first':n1, 'after_last':n3}


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        if k == 1: return head
        list_first = None
        prev_end = None
        a = head
        while True:
            new_last = a
            data = self.rev1group(a, k)
            # print(f"R1R k={k} rev={data['reversed']} nf={p(data['new_first'])} al={p(data['after_last'])}")
            new_first = data['new_first']
            after_last = data['after_last']
            new_last.next = after_last
            if data['reversed'] < k:
                self.rev1group(new_first, k)
                new_first.next = None
                if list_first is None: list_first = a
                return list_first
            if list_first is None:
                list_first = new_first
            else:
                prev_end.next = new_first
            prev_end = new_last
            a = after_last
            if a is None: return list_first

