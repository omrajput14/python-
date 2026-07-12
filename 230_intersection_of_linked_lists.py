class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_intersection_node(headA, headB):
    if not headA or not headB: return None
    pa, pb = headA, headB
    while pa != pb:
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next
    return pa

if __name__ == "__main__":
    head = ListNode(1)
    print(get_intersection_node(head, head))