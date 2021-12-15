import csv
import os
from tabulate import tabulate
os.chdir(r"C:\Users\User\Documents\python2")

file = csv.reader(open('tesuas.csv', 'r'))
rows = [row for row in file]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(1, n - i - 1):
            if arr[j][6] > arr[j + 1][6]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid][6] == x:
            return mid
        elif arr[mid][6] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

print("Data sebelum diurutkan: ")
for i in range(5):
    print(rows[i])

sorted_rows = bubble_sort(rows)

print("Data setelah diurutkan: ")
for i in range(5):
    print(sorted_rows[i])

while True:
    menu = int(input("1. Cari nilai tertentu dalam variabel sales\n2. Tulis hasil sort ke file baru\n3.Exit\n"))
    if menu == 1:
        cari = input("Nilai berapa yang ingin dicari: ")
        hasil = binary_search(sorted_rows, 1, len(sorted_rows)-1, cari)
        if hasil != -1:
            os.system('cls')
            print(f"Nilai {cari} ada pada variabel sales pada baris ke-{hasil}")
            print(sorted_rows[0])
            print(sorted_rows[hasil])
            input("Tekan ENTER untuk melanjutkan...")
    elif menu == 2:
        with open('outputtesuas.csv', 'w') as f:
            sorted_rows2 = [', '.join(row)+'\n' for row in bubble_sort(rows)]
            f.writelines(sorted_rows2)
            print("File hasil sort telah dibuat dengan nama outputtesuas.csv!")
            input("Tekan ENTER untuk melanjutkan")
    elif menu == 3:
        print("Keluar...")
        break
