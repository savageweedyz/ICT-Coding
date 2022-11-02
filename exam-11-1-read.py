import csv
header = ("{:<10} {:<10}{:<10}\n".format("วันที่","รายการ","จำนวนเงิน"))
print(header)
file = csv.reader(open("D:\work\expense.csv","r", encoding="UTF-8"))
for data in file:
    print("{} {} {}".format(data[0], data[1], data[2] ))
