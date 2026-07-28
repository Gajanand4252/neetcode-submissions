class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        res = []
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        l = list(dict(sorted(h.items(), key = lambda item:item[1])))
        for i in range(1, k+1):
            res.append(l[-i])
            
        return res