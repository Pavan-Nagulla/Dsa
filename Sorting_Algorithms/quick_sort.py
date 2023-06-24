"""

Example 1:
Input:  N = 5  , Arr[] = {4,1,7,9,3}
Output: 1 3 4 7 9 

Explanation: After sorting the array becomes 1, 3, 4, 7, 9

Example 2:
Input: N = 8 , Arr[] = {4,6,2,5,7,9,1,3}
Output: 1 2 3 4 5 6 7 9
Explanation: After sorting the array becomes 1, 3, 4, 7, 9

"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [9, 5, 1, 3, 10, 6, 2, 4, 8, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)


"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) - 1
    pivot = arr[pivot_index]
    i = 0

    for j in range(len(arr)):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    left = quick_sort(arr[:i-1])
    right = quick_sort(arr[i:])
    
    return left + [pivot] + right

# Example usage:
arr = [9, 5, 1, 3, 10, 6, 2, 4, 8, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)

"""

"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left = 0
    right = len(arr) - 1
    pivot = arr[left]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr[:left])
    quick_sort(arr[left:])

    return arr

# Example usage:
arr = [9, 5, 1, 3, 10, 6, 2, 4, 8, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)

"""