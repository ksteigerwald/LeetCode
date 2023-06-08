class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        cache = {num: 0 for num in nums }
        output = []
        for item in nums:
            cache[item] += 1
        tups = list(cache.items())
        sorted_list = sorted(tups, key=lambda x: x[1])[-k:]
        print(sorted_list[-k:])
        return [t[0] for t in sorted_list]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))

