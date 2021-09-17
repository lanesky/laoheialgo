# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Time O(k*n^2) | Space O(n)
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        distance = [float('inf')] * n
        distance[src] = 0
        
        # Forcily run Bellman-Ford in worst case
        for _ in range(k+1):            
            curr = distance[:]           
            for i,j,price in flights:
                if distance[i] + price < curr[j]:
                    curr[j] = distance[i] + price 
            distance = curr
                                        
        return distance[dst] if distance[dst] != float('inf') else -1