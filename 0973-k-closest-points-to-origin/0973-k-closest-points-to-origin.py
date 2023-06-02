class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        
        for pt in points:
            heappush(heap,(pt[0] ** 2 + pt[1] ** 2, pt))
            
        
        res = []
        
        for _ in range(k):
            _, pt = heappop(heap)
            res.append(pt)
        return res