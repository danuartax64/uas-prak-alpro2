import csv
import os

os.chdir(r"C:\Users\User\Documents\python2")
Dataku = list()

with open("tesuas.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        Dataku.append(row)

print ("data sebelum disorting")
for i in range(5):
    print(Dataku[i])

def bubbleSort(Dataku):
    n = len(Dataku)
    for i in range(n):
        for j in range(1, n-i-1):
            if Dataku[j][6] > Dataku[j+1][6] :
                Dataku[j], Dataku[j+1] = Dataku[j+1], Dataku[j]

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

print ("\ndata setelah disorting")
for i in range(5):
    print(Dataku[i])

with open('hasilsort.txt','w+') as f:
    f.writelines(str(Dataku))

csv_file.close()

'''while True:
    menu = int(input("1. Cari nilai dalam variabel sales\n2.Tulis hasil sort ke file baru\n3.Keluar"))
    if menu == 1:
        cari = (input("Nilai berapakah yang ingin anda cari di variabel sales:? "))
        hasil = binary_search(Dataku, 1, len(Dataku)-1, cari)
        if hasil != -1:
            print("Ada")
        else:
            print("Tidak ada")
    elif menu == 2:
        with open('outputtesuas.csv', 'w') as f:
            f.writelines(Dataku)
    elif menu == 3:
        break
    else:
        print("Masukan pilihan yang sesuai")'''
