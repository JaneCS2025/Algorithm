'''
input:["eat", "tea", "tan", "ate", "nat", "bat"]
output:[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

review default dict: https://www.geeksforgeeks.org/python/defaultdict-in-python/
'''

from collections import defaultdict

def group_anagrams(strs):
  groups = defaultdict(list)
  for s in strs:
    groups[''.join(sorted(s))].append(s)
  return list(groups.values())

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
