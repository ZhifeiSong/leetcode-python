import functools
from typing import List
def comparator(s1: int, s2:int) -> int:
    s1Lead = str(s1) + str(s2)
    s2Lead = str(s2) + str(s1)
    if int(s1Lead) < int(s2Lead):
        return 1
    elif int(s1Lead) > int(s2Lead):
        return -1
    return 0

def largestNumber(nums:List[int]) -> str:
    sorted_nums = sorted(nums, key=functools.cmp_to_key(comparator))
    return ''.join(str(i) for i in sorted_nums)