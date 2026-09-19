class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurences
        # we can use a maxheap
        freqs = defaultdict(int)
        max_freq = 0
        for num in nums:
            freqs[num] += 1
            if freqs[num] > max_freq:
                max_freq = freqs[num]
        index_arr = [[] for _ in range(max_freq + 1)]
        for key, val in freqs.items():
            index_arr[val].append(key)
        return_arr = []
        for i in range(max_freq, 0, -1):
            for num in index_arr[i]:
                return_arr.append(num)
                if len(return_arr) == k:
                    return return_arr

