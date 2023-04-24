arr = [8,1,5,3,2,0]*1000

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        #print("\n", "*"*80, "\n", "index", i, "value", arr[i])
        for i in range(len(arr)-1-j):
        #print("comparing", arr[i], arr[i+1])

        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1]. arr[i]
            #print("swapped", arr[i], arr[i+1])
            #print("array is now", arr)
        #else:
            #print("no need to swap", arr[i], arr[i+1])

    print('# of evaluation', count)
    return arr
bubbleSort(arr)