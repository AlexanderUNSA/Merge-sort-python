import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

sizes = [100, 1000, 2000, 3000, 4000, 5000]

for size in sizes:
    # Generate a random list
    lst = [random.randint(0, 1000) for _ in range(size)]

    # Measure the time taken to sort
    start_time = time.time()
    _ = merge_sort(lst)
    elapsed_time = time.time() - start_time

    print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

