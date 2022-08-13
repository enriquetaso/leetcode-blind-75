# i.e: arr =  [1,2,3,4,5,6] and x = 7
from typing import List


def dynamic_sliding_window(arr: List[int], x: int) -> int:
    # Track our min value
    min_length = float('inf')
    
    # The current range and sum of our sliding window
    start = 0 
    end = 0
    current_sum = 0
    
    # Extend the sliding window until our criteria is met
    while end < len(arr):
        current_sum = current_sum + arr[end]
        end = end + 1 
        
        # Then contract the sliding window until it
        # no longer meets our condition
        while start < end and current_sum >=x:
            current_sum = current_sum - arr[start]
            start = start + 1
            
            # Update the min_length if this is shorter
            # than the current min
            min_length = min(min_length, end-start+1)
    return min_length