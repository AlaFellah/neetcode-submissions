class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        requenty_t = {}
        k_list = []
        for n in nums:
            requenty_t[n]= requenty_t.get(n, 0) + 1

        for i in range(k):
            max_key = max(requenty_t, key=requenty_t.get)
            max_value = requenty_t.pop(max_key)
            k_list.append(max_key)
        return k_list