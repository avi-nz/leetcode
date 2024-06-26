class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for number, count in count.items():
            freq[count].append(number) # the number has occured count amount of times
        
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
