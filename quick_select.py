from typing import List


def partition(arr: List[int], l:int, r:int) -> int:
    pivot = arr[r]
    i = l
    for j in range(l, r+1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i-1


class Algo:
    def quick_select(self, arr:List[int], l: int, r:int, k:int) -> int:
        pivot_index = partition(arr, l, r)
        if pivot_index == k - 1:
            return arr[pivot_index]
        if pivot_index > k - 1:
            return self.quick_select(arr, l, pivot_index-1, k)
        else:
            return self.quick_select(arr, pivot_index+1, r, k)

print(partition([2,8,3,9,10,4], 0, 5))
algo = Algo()
print(algo.quick_select([1], 0, 0, 1))
