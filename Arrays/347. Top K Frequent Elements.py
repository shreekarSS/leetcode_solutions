from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  build a counter for the numbers
        # create  list of mini lists for each numbers in the nums, it's index is the number of times numbers repeated:  ex: [1,1,1,2,3,3] --> [[2],[3],[1]] 1 is repeated 3 times

        counters = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        # counter the number occurrences

        for num in nums:
            counters[num] = 1 + counters.get(num, 0)

        # build mini list

        for number, counter in counters.items():
            freq[counter].append(number)

        # iterate freq in reverse ,stop it once it's length is k
        for counter in range(len(freq) - 1, 0, -1):
            for number in freq[counter]:
                res.append(number)

                if len(res) == k:
                    return res
