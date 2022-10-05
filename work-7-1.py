
total = int(input("จำนวนเงินที่ลงทุน = "))

if total >= 150000:
    res = total * (10/100)
    percent = 10
elif total >= 100000:
    res = total * (7/100)
    percent = 7
elif total >= 50000:
    res = total * (5/100)
    percent = 5
elif total >= 10000:
    res = total * (4/100)
    percent = 4
else:
    total <= 10000
    res = 0
    percent = 0

sum = total+res

print("รับยอดเงินลงทุน : ",total)
print("*****โปรแกรมคำนวณเงินปันผลจากการลงทุนใน 1 ปี*****")
print("เงินลงทุน : ",total)
print("ได้ผลตอบแทน : ",percent,"%","เป็นจำนวนเงิน : ",res,"บาท")
print("ยอดเงินลงทุนรวมผลตอบแทน : ",sum,"บาท")