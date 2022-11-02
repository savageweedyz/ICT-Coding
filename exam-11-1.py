import csv
n = int(input("ต้องการบันทึกค่าใช้จ่ายทั้งหมดกี่ครั้ง : "))
#num = []
j = 0
days = input("วันที่ : ")
while j < n:
    list = str(input("รายการค่าใช้จ่าย : "))
    cost = int(input("จำนวนเงินที่ใช้จ่าย : "))
    #num.append(cost)
    #res = sum(num)
    with open(r"D:\work\expense.csv","a",encoding="utf-8",newline="") as file:
        csvfile = csv.writer(file)
        csvfile.writerow([days,list,cost])
    j += 1
print("END PROGRAM")