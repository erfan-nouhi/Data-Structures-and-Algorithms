#Erfan Nouhi
#W3schools

# counting sort

"""
For counting sort we should track the number of each element's occurance .
We create a counter which indices represent the element itself and the values-
for these indices are number of occurance for that specific element.
This slgorithm works only with posetive Integers .
"""

def counting_sort(arr):
    # find out how many indices we need.
    maximum = max(arr)
    counter = [0]*(maximum+1)

    # increase the number of occurance for each element. 
    while len(arr) > 0:
        popped = arr.pop(0)
        counter[popped] += 1

    # we write back index(element) for number of occurance times.
    # indices are sorted so elements will be sorted too.

    for i in range(len(counter)):
        while counter[i] > 0:
            arr.append(i)
            counter[i] -= 1

    return arr

array = [132,235,34,34,4,346,356,55,57]
print(array)
print(counting_sort(arr=array))