class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_c = sorted(counter.items(), key=lambda c: c[1], reverse=True
        )
        return [sorted_c[i][0] for i in range(k)]
        