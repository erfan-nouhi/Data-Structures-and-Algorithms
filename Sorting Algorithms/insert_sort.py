#Erfan Nouhi
#W3schools : this is my source for learning DSA


def insert_sort(arr):
    length = len(arr)
    for i in range(1,length):#traverse forward to bring arr[i] to correct position
        for j in range(i,0,-1):#find correct position , 0 is exclusive
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break #left side element is lower than this element

array = [23,35,3,24,36,646,34,3,36,363,363,36]

print(array)
insert_sort(array)
print(array)
