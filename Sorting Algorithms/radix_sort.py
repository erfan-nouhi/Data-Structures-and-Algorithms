#Erfan Nouhi
#W3schools

#radix_sort

"""
To implement radix sort we need to sort numbers according to their digits.
Numbers are non negetive integers .

"""

def radix_sort(arr:list):
    # we will have 10 buckets for digits 0 to 9.
    buckets = [[] for _ in range(10)]

    # we have to continue to sort untill last digit of maximum is checked ,because it has the maximum digits.

    exp = 1
    maximum = max(arr)

    while maximum // exp > 0:

        while len(arr) > 0:
            position = (arr[0] // exp) % 10
            buckets[position].append(arr.pop(0))

        # return numbers back to array but sorted with respect to this time digit.
        for bucket in buckets:
            while len(bucket) > 0:
                arr.append(bucket.pop(0))
        
        # each time we will need the left digit that is not checked.
        exp *= 10

    

array = [12,4,4,32,325,47,346,3,645,54,75,7,58,5,8,5,8]
print(array)
radix_sort(array)
print(array)

