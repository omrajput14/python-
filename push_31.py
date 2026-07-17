import os
import subprocess

directory = '/Users/0mrajput/Desktop/python'
os.chdir(directory)

files = {
    '216_two_sum.py': '''def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map: return [num_map[diff], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))''',

    '217_three_sum.py': '''def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: l += 1
            elif s > 0: r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
    return res

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))''',

    '218_four_sum.py': '''def four_sum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]: continue
            l, r = j+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < target: l += 1
                else: r -= 1
    return res

if __name__ == "__main__":
    print(four_sum([1,0,-1,0,-2,2], 0))''',

    '219_group_anagrams.py': '''import collections
def group_anagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))''',

    '220_remove_element.py': '''def remove_element(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

if __name__ == "__main__":
    arr = [3,2,2,3]
    print(remove_element(arr, 3), arr)''',

    '221_search_insert_position.py': '''def search_insert(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target: return mid
        if nums[mid] < target: l = mid + 1
        else: r = mid - 1
    return l

if __name__ == "__main__":
    print(search_insert([1,3,5,6], 5))''',

    '222_plus_one.py': '''def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

if __name__ == "__main__":
    print(plus_one([1,2,3]))''',

    '223_climbing_stairs.py': '''def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b

if __name__ == "__main__":
    print(climb_stairs(5))''',

    '224_merge_sorted_array.py': '''def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    merge(nums1, 3, [2,5,6], 3)
    print(nums1)''',

    '225_pascals_triangle.py': '''def generate(numRows):
    res = [[1]]
    for i in range(1, numRows):
        temp1 = res[-1] + [0]
        temp2 = [0] + res[-1]
        res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
    return res

if __name__ == "__main__":
    print(generate(5))''',

    '226_buy_and_sell_stock.py': '''def max_profit(prices):
    if not prices: return 0
    min_price = prices[0]
    max_prof = 0
    for price in prices:
        if price < min_price: min_price = price
        elif price - min_price > max_prof: max_prof = price - min_price
    return max_prof

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))''',

    '227_valid_palindrome_ii.py': '''def valid_palindrome(s):
    def is_pali_range(i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))
    for i in range(len(s)//2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)
    return True

if __name__ == "__main__":
    print(valid_palindrome("abca"))''',

    '228_single_number.py': '''def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

if __name__ == "__main__":
    print(single_number([4,1,2,1,2]))''',

    '229_linked_list_cycle.py': '''class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print(has_cycle(head))''',

    '230_intersection_of_linked_lists.py': '''class ListNode:
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
    print(get_intersection_node(head, head))''',

    '231_reverse_linked_list.py': '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    head = ListNode(1, ListNode(2))
    print(reverse_list(head).val)''',

    '232_contains_duplicate.py': '''def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))''',

    '233_power_of_two.py': '''def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    print(is_power_of_two(16))''',

    '234_power_of_three.py': '''def is_power_of_three(n):
    if n < 1: return False
    while n % 3 == 0: n //= 3
    return n == 1

if __name__ == "__main__":
    print(is_power_of_three(27))''',

    '235_power_of_four.py': '''def is_power_of_four(n):
    return n > 0 and (n & (n-1)) == 0 and (n & 0x55555555) != 0

if __name__ == "__main__":
    print(is_power_of_four(16))''',

    '236_number_of_1_bits.py': '''def hamming_weight(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res

if __name__ == "__main__":
    print(hamming_weight(11))''',

    '237_reverse_bits.py': '''def reverse_bits(n):
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

if __name__ == "__main__":
    print(reverse_bits(43261596))''',

    '238_missing_number.py': '''def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == "__main__":
    print(missing_number([3,0,1]))''',

    '239_move_zeroes.py': '''def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

if __name__ == "__main__":
    arr = [0,1,0,3,12]
    move_zeroes(arr)
    print(arr)''',

    '240_first_unique_character.py': '''def first_uniq_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(first_uniq_char("leetcode"))''',

    '241_valid_perfect_square.py': '''def is_perfect_square(num):
    r = num
    while r*r > num:
        r = (r + num//r) // 2
    return r*r == num

if __name__ == "__main__":
    print(is_perfect_square(16))''',

    '242_find_the_difference.py': '''def find_the_difference(s, t):
    res = 0
    for c in s + t:
        res ^= ord(c)
    return chr(res)

if __name__ == "__main__":
    print(find_the_difference("abcd", "abcde"))''',

    '243_is_subsequence.py': '''def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]: i += 1
        j += 1
    return i == len(s)

if __name__ == "__main__":
    print(is_subsequence("abc", "ahbgdc"))''',

    '244_add_strings.py': '''def add_strings(num1, num2):
    res = []
    carry = 0
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1 >= 0 or p2 >= 0 or carry:
        x1 = int(num1[p1]) if p1 >= 0 else 0
        x2 = int(num2[p2]) if p2 >= 0 else 0
        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        res.append(str(value))
        p1 -= 1; p2 -= 1
    return "".join(res[::-1])

if __name__ == "__main__":
    print(add_strings("11", "123"))''',

    '245_third_maximum_number.py': '''def third_max(nums):
    s = set(nums)
    if len(s) < 3: return max(s)
    s.remove(max(s))
    s.remove(max(s))
    return max(s)

if __name__ == "__main__":
    print(third_max([3,2,1]))''',

    '246_arranging_coins.py': '''def arrange_coins(n):
    l, r = 0, n
    while l <= r:
        k = (r + l) // 2
        curr = k * (k + 1) // 2
        if curr == n: return k
        if n < curr: r = k - 1
        else: l = k + 1
    return r

if __name__ == "__main__":
    print(arrange_coins(5))'''
}

sorted_files = sorted(files.keys())

for filename in sorted_files:
    content = files[filename]
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Adding, committing, and pushing {filename}...")
    subprocess.run(['git', 'add', filename])
    subprocess.run(['git', 'commit', '-m', f"Add {filename} (algorithm)"])
    subprocess.run(['git', 'push'])

print("All 31 files pushed successfully!")
