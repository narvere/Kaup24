import csv
import ok

arr = []
text = "TV Juhtimispult "
text2 = "ТВ пульт "
with open('D:\Kaup24\Samsung121022.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # row[0] = text + row[0]
        # row[0] = text2
        arr.append(row)
        # print(row)
# for i in arr:
#     print(i)

for i in range(len(arr)):
    arr[i].append(text+str(arr[i][0]))
    arr[i].append(text2 + str(arr[i][0]))
    # print(arr[i])
print(arr[0][5])