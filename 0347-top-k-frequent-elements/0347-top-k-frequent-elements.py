class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for i in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
"""class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = []
        nam = {}
        for i in nums:
            f1 = nums.count(i)
            if i not in nam :
                nam[i]= f1
        
        nam = dict(sorted(nam.items(), key=lambda item: item[1], reverse = True))
        for i,j in nam.items():
            if len(new) < k:
                new.append(i)
        return new""" # Time limit Exceeded 😓
            
        

        