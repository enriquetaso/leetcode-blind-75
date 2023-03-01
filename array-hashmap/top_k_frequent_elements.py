from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums

    result = []
    # {number of occurency: numer}
    frequent = Counter(nums)
    topk_keys = sorted(frequent.keys(), reverse=True)[:k]
    for element in topk_keys:
        result.append(frequent[element])
    return result


def topKFrequent3(nums: List[int], k: int) -> List[int]:
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    return [
        n for n, _ in sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]
    ]


def topKFrequent_neetcode(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
        # [[2,3], [3]]
    print(freq)
    res = []
    # reverse traversin
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    nums2 = [1, 3, 3, 2, 2, 3]
    print(topKFrequent_neetcode(nums, k))
    # print(topKFrequent(nums2, k))
    # print(topKFrequent2(nums, k))
