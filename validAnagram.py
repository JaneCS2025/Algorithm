'''
s = "anagram", t = "nagaram"  →  True
s = "rat",     t = "car"      →  False

'''
# Way1
def checkAnagram(s,t):
  if len(s) !=len(t):
    return False
  return sorted(s) == sorted(t)

# Time O(nlogn) Space O(1)
print(checkAnagram("anagram", "nagaram")) 
print(checkAnagram("rat", "car")) 

from collections import Counter

# Way2
def checkAnagram2(s,t):
   if len(s) != len(t):
      return False
   return Counter(s) == Counter(t)

print(checkAnagram2("anagram", "nagaram")) 
print(checkAnagram2("rat", "car")) 

print(Counter("anagram"))
print(Counter("nagaram"))

# Time O(n) Space O(1)

# # Way3
def checkAnagram3(s, t):
  if len(s) !=len(t):
      return False

  count = {}
  for s_char, t_char in zip(s,t):
     count[s_char] = count.get(s_char, 0) + 1
     count[t_char] = count.get(t_char, 0) - 1

  return all(v==0 for v in count.values())


print(checkAnagram3("anagram", "nagaram")) 
print(checkAnagram3("rat", "car")) 


  
