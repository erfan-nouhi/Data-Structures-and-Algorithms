#Erfan Nouhi
#W3schools

"""
For merge sort which is a divide and conqeur algorithm is better to use recursion.

here we divide the given array from center to two subarrays and we continue till -
we have only one element which is obviously sorted .

then we should stick these divided parts back together ,but this time sorted.

"""

def merge(left,right):
    merge_result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:#here we append the lower value at each momment then
            # if it is for left i+=1 otherwise j+=1
            merge_result.append(left[i])
            i+=1
        else:
            merge_result.append(right[j])
            j+=1
    
    merge_result.extend(left[i:])# one of these two right or left is completly traversed
    merge_result.extend(right[j:])# so we extend empty array.
    return merge_result


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    else:

        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        return merge(left_sorted,right_sorted)
    

array = [23,34,35,4,6,56,5,7,6,8,7,24324]
print(array)
print(merge_sort(array))