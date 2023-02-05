import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)

        for word in strs:
            mini_list = [0]*26

            for w in word:
                mini_list[ord(w)-ord('a')]+=1

            lookup[tuple(mini_list)].append(word)

        return lookup.values()