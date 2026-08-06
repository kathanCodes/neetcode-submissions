class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countDict = defaultdict(int)

        for num in nums :
            countDict[num] += 1

        heap = []

        for num in countDict.keys() :
            heapq.heappush(heap, (countDict[num],num))

            if len(heap) > k :
                heapq.heappop(heap)

        # res = []
        # for i in range(k) :
        #     res.append(heapq.heappop(heap)[1])

        res = [row[1] for row in heap]

        return res
