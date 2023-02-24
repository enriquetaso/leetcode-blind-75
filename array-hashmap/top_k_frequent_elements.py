from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """Using Bucket Sort"""
    if k == len(nums):
        return nums

    result = []
    # {number of occurency: numer}
    frequent = Counter(nums)
    total_top = list(frequent.keys())
    total_top.sort(reverse=True)

    for element in total_top[:k]:
        result.append(frequent[element])
    return result


def topKFrequent2(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums

    result = []
    ocurrencies = {}
    for num in nums:
        ocurrencies[num] = 1 + ocurrencies.get(num, 0)

    # items() returns dict_items([(1, 3), (2, 2), (3, 1)])
    # key=lambda item: item[1] will sort the nested list based on
    # the second position of the tuple
    mylistSort = sorted(ocurrencies.items(), key=lambda item: item[1], reverse=True)
    for element_tuple in mylistSort:
        num, _ = element_tuple
        result.append(num)
    return result[:k]


def topKFrequent_neetcode(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

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
    print(topKFrequent(nums, k))
    print(topKFrequent(nums2, k))
    print(topKFrequent2(nums, k))
