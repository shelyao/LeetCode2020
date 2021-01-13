class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append((d, c))
        heap = []
        heappush(heap, (0, src, K))
        while heap:
            #print(heap)
            cost, city, connecting = heappop(heap)
            if city == dst: return cost
            if connecting >= 0:
                for neighbor, price in graph[city]:
                    heappush(heap, (cost + price, neighbor, connecting-1))
        return -1