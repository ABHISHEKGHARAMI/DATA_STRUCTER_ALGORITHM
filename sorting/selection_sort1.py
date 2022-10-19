# Selection sort in Python


def selectionSort(a,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if a[min_idx]>a[i]:
                min_idx=i
        a[step],a[min_idx]=a[min_idx],a[step]


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
