class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            
            ttime=0
            for p in piles:
                ttime+=math.ceil(p/mid)

            if ttime<=h:
                r=mid
            else:
                l=mid+1
            
        return l


