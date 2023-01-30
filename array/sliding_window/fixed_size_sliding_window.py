# Given an array, find all subarrays of length k
# i.e arr = [1,2,3,4,5,6] and k=3
# result_array = [6, 9, ..]

from typing import List


def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    # Sum up the first subarray and add it to the result
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    # To get each subsequent subarray, add the next value
    # in the list and remove the first value
    for i in range(1, len(arr) - k + 1):
        curr_subarray = curr_subarray - arr[i - 1]
        curr_subarray = curr_subarray + arr[i + k - 1]

        result.append(curr_subarray)
    return result
