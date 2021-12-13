import csv
file = csv.reader(open('tesuas.csv', 'r'))
rows = ['sales']


# Python program for implementation of Bubble Sort
# from: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# modified to sort by the third element in the row per SO question
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][2] > arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


sorted_rows = [', '.join(row)+'\n' for row in bubble_sort(rows)]
with open('outputtesuas.csv', 'w') as f:
    f.writelines(sorted_rows)
