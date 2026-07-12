import collections
def group_anagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))