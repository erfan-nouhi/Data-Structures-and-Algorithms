#Erfan Nouhi
#W3schools

"""
for quicksort we use recursion.
we need a pivot which left side of this pivot is for -
elements less than that and right side for higher elements.

here pivot is the element in high index .

we recursively go trough each parts next to the pivot and do this again.
"""

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1 # this is used to keep track of elements less than pivot and -
    # where should pivot be settled

    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i] # we swap the lower elemnt than pivot with elemnts bigger
            # this brings lower elemnts all together .
        
    arr[high],arr[i+1] = arr[i+1],arr[high] # finally to bring pivot after lower elments
    # and before higher ones.
    return i+1


def quick_sort(arr,low=0,high=None):
    if high is None:#for first call in body. look below 
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr,low,high)

        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

array = [32,34,43,6,57,35,74,36]

print(array)
quick_sort(array)
print(array)

