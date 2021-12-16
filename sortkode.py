import csv
import os
from timeit import default_timer as timer

os.chdir(r"C:\Users\User\Documents\python2")        #direktori file csv

file = csv.reader(open('tesuas.csv', 'r'))
rows = [row for row in file]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(1, n - i - 1):
            if float(arr[j][6]) > float(arr[j + 1][6]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if float(arr[mid][6]) == x:
            return mid
        elif float(arr[mid][6]) > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
        
def clear():
    os.system('cls')		#kalo di linux clear kalo di windows cls
    
print("Sampel data sebelum diurutkan: ")
for i in range(5):
    print(rows[i])

start = timer()
sorted_rows = bubble_sort(rows)
end = timer()
elapsedtime = end - start
lewat = "{:.2f}".format(elapsedtime)

print("\nSampel data setelah diurutkan: ")
for i in range(5):
    print(sorted_rows[i])
print(f"\nWaktu sort: {lewat} detik")

while True:
    print("="*35)
    menu = int(input("MENU\n1. Cari nilai tertentu dalam variabel sales\n2. Tulis hasil sort ke file baru\n3.Exit\n"))

    if menu == 1:
        cari = float(input("Nilai berapa yang ingin dicari: "))
        start = timer()
        hasil = binary_search(sorted_rows, 1, len(sorted_rows)-1, cari)
        end = timer()
        elapsedtime = end - start
        lewat = "{:.5f}".format(elapsedtime)
        
        if hasil != -1:
            clear()	
            print(f"Nilai {cari} ada pada variabel sales pada baris ke-{hasil} atau ke-{hasil+1} jika dengan header\n")
            print(sorted_rows[0])
            print(sorted_rows[hasil])
            print(f"\nWaktu search: {lewat} detik")
            input("Tekan ENTER untuk melanjutkan...")
            clear()

        else:
            print(f"\nNilai {cari} tidak ditemukan pada variabel sales")
            input("Tekan ENTER untuk melanjutkan...")
            clear()

    elif menu == 2:
        start = timer()
        with open('outputtesuas.csv', 'w+') as f:
            sorted_rows2 = [', '.join(row)+'\n' for row in sorted_rows]
            f.writelines(sorted_rows2)
            end = timer()
            elapsedtime = end - start
            lewat = "{:.2f}".format(elapsedtime)
            print("File hasil sort telah dibuat dengan nama outputtesuas.csv!")
            print(f"Dengan waktu proses selama {lewat} detik")
            input("Tekan ENTER untuk melanjutkan")
            clear()

    elif menu == 3:
        print("Keluar...")
        break

    else:
        print("Masukan pilihan yang sudah diberikan!")
