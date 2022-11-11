from prettytable import PrettyTable


class jadwalPertandingan(object):
    def __init__(self, data=""):
        f = open(data, "r")
        self.jadwal = []
        for x in f.read().split("\n"):
            obj = x.split(",")
            if len(obj) > 1:
                self.jadwal.append(
                    {'pertandingan': obj[1], 'tempat': obj[2], 'waktu': obj[3], 'jam': obj[4]})

    def merge(self, order_by, order, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = self.jadwal[l + i]

        for j in range(0, n2):
            R[j] = self.jadwal[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if order == "asc":
                if L[i][order_by] <= R[j][order_by]:
                    self.jadwal[k] = L[i]
                    i += 1
                else:
                    self.jadwal[k] = R[j]
                    j += 1
            elif order == "desc":
                if L[i][order_by] >= R[j][order_by]:
                    self.jadwal[k] = L[i]
                    i += 1
                else:
                    self.jadwal[k] = R[j]
                    j += 1
            else:
                pass

            k += 1

        while i < n1:
            self.jadwal[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            self.jadwal[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, order_by, order, l, r):
        if l < r:
            m = l+(r-l)//2
            self.mergeSort(order_by, order, l, m)
            self.mergeSort(order_by, order, m+1, r)
            self.merge(order_by, order, l, m, r)

    def __str__(self):
        tampil = ""
        tampil += "----------------------------------------------------------------------\n"
        for x in self.jadwal:
            tampil += x["pertandingan"] + " di " + \
                x["tempat"] + " pada " + x["waktu"] + "\n"
        return tampil


data = jadwalPertandingan("jadwalpertandinganpialadunia2018.csv")
print("Data sebelum diolah")
print("Array Data")
print('----------------------------------------------------------------------')
print(data.jadwal)
print("")
print("Nama tempat pertandingan Ascending")
data.mergeSort("pertandingan", "asc", 0, len(data.jadwal)-1)
tabel = PrettyTable(["Match", "Venue", "Time", "Jam"])
for x in data.jadwal:
    tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"], x["jam"]])
print(tabel)
print("\n")
print("Nama waktu pertandingan Ascending")
data.mergeSort("waktu", "asc", 0, len(data.jadwal)-1)
tabel = PrettyTable(["Match", "Venue", "Time", "Jam"])
for x in data.jadwal:
    tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"], x["jam"]])
print(tabel)
print()
# data.mergeSort("waktu", "asc", 0, len(data.jadwal)-1)
# print(data)
print("Nama waktu pertandingan Descending")
data.mergeSort("waktu", "desc", 0, len(data.jadwal)-1)
tabel = PrettyTable(["Match", "Venue", "Time", "Jam"])
for x in data.jadwal:
    tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"], x["jam"]])
print(tabel)
# data.mergeSort("waktu", "desc", 0, len(data.jadwal)-1)
# print(data)

# print("Nama tempat pertandingan Descending")
# data.selectionSort("tempat","DESC")
# print(data)
# print("Waktu pertandingan Ascending")
# data.selectionSort("waktu")
# print(data)
# print("Waktu pertandingan Descending")
# data.selectionSort("waktu","DESC")
# print(data)


# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")
#
# mergeSort(arr)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")
