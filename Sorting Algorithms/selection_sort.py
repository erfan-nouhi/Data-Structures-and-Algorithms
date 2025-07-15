#Erfan Nouhi
#W3schools

def selection_sort(arr):
    length = len(arr)

    for i in range(length):
        minimum = arr[i]
        minimumIndex = i

        for j in range(i,length):#find minimum number from index i to end of array

            if arr[j] < minimum:
                minimum = arr[j]
                minimumIndex = j
                
        #bring minimum to begining (i)        
        arr[minimumIndex],arr[i] = arr[i],arr[minimumIndex]

array = [12,24,34,435,4363,34,24,3,6,3]

print(array)
selection_sort(array)
print(array)



        
