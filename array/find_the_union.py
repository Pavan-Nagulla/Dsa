"""
Union of Two Sorted Arrays
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

"""

#bruteforce

def find_union(arr1, arr2):
    union = []
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    
    # Traverse both arrays
    while i < n and j < m:
        # Check if arr1[i] is smaller
        if arr1[i] < arr2[j]:
            # Add arr1[i] to the union if it is not already present
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        # Check if arr2[j] is smaller
        elif arr1[i] > arr2[j]:
            # Add arr2[j] to the union if it is not already present
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        # Both elements are equal
        else:
            # Add either element to the union if it is not already present
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1
    
    # Add remaining elements from arr1
    while i < n:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < m:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    
    return union

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
union = find_union(arr1, arr2)
print(union)


# 2-pointer approach

"""
def find_union(arr1, arr2):
    union = []
    i = j = 0
    n = len(arr1)
    m = len(arr2)
    
    # Traverse both arrays simultaneously
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
            j += 1
    
    # Add remaining elements from arr1
    while i < n:
        union.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < m:
        union.append(arr2[j])
        j += 1
    
    return union

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
union = find_union(arr1, arr2)
print(union)


"""