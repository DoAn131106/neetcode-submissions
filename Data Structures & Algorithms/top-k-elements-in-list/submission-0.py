class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for i in nums:
            hash_map[i] += 1
        heap = []
        for num, count in hash_map.items():
            heapq.heappush(heap, (-count, num))
        ret = []
        for j in range(k):
            count, num = heapq.heappop(heap)
            ret.append(num)
        return ret