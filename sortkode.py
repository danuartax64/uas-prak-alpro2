import csv
file = csv.reader(open('tesuas.csv', 'r'))
rows = [row for row in file]

# Python program for implementation of Bubble Sort
# from: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# modified to sort by the third element in the row per SO question
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(1, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][6] > arr[j + 1][6]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
print("Data sebelum diurutkan: ")

for i in range(5):
    print(rows[i])

sorted_rows = bubble_sort(rows)

print("Data setelah diurutkan: ")
for i in range(5):
    print(sorted_rows[i])
    
#with open('outputtesuas.csv', 'w') as f:
       #sorted_rows2 = [', '.join(row)+'\n' for row in bubble_sort(rows)]
       #f.writelines(sorted_rows2)
