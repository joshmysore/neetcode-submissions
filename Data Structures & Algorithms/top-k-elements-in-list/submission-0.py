from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # only one sol
        # track each element of array nums
        # for each el, store in dictionary and update count
        # at the end, will have 1: 1, 2: 2, 3: 3
        # sort dict to have highest count at the start
        # return the keys in desc order of whatever k is
        
        # dict 
        freq = defaultdict(int)
        
        # count apperances
        for num in nums: 
            freq[num] += 1

        # sort els by freq in desc order
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # take first k elements 
        top_k = sorted_freq[:k]

        # return numbers, not freq
        return [num for num, count in top_k]
        
        
        