def Insertion_Sort(ls):
    for i in range(1,len(ls)):
        key = ls[i]
        j = i - 1 
        while j >= 0 and key < ls[j]:
            ls[j + 1 ] =ls[j]
            j = j-1 
        ls[j + 1] = key


data = [4,2,6,9,1,2]

Insertion_Sort(data)
print('Sorted array:',data) 
