class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        km = - float("infinity")
        for i in piles:
            if i>km:
                km = i
        
        l, r = 1, km
        while l<=r:
            mi = l + (r-l) // 2
            h1 = 0
            for i in piles:
                time = i // mi
                h1 += time if i % mi == 0 else time + 1
            if h1 > h:
                l = mi + 1
            else:
                print(km)
                km = mi
                r = mi - 1

        return km
