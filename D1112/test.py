def sel_sort(a):
    n = len(a)

    for i in range(0, n - 1):

        min_idx = i

        for j in range(i + 1, n):

            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

        print(a)

def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        idx = i
        for j in range(i+1, n):
            if a[j] < a[idx]:
                idx = j
        a[i], a[idx] = a[idx], a[i]
        print(a)

d = [7, 4, 2, 11, 50]
selection_sort(d)
