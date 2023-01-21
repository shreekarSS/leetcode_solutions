import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = collections.defaultdict(list)

        for s in strs:
            mini_list_for_each_word = [0]*26
            for c in s:
                mini_list_for_each_word[ord(c)-ord('a')]+=1

            lookup[tuple(mini_list_for_each_word)].append(s)

        return lookup.values()
