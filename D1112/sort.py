def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        while i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
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

def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        pivot = a[n-1]
        left, mid, right = [],[],[] #임시 리스트
        for i in range(n-1):
            if a[i] < pivot:
                left.append(a[i])
            elif a[i] > pivot:
                right.append(a[i])
            else:
                mid.append(a[i])
        mid.append(pivot)
        return quick_sort(left) + mid + quick_sort(right)


def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(a)



a = [7, 4, 2, 11, 50, 1, 55, 34, 12, 53, 6, 15, 87, 31, 22, 89, 56, 71, 24]
print('insertion sort')
insertion_sort(a)
print()
print('selection sort')
selection_sort(a)
