class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=defaultdict(int)
        for i in nums:
            h[i]+=1
        sorted_list=sorted(h.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_list[i][0])
        return res 
