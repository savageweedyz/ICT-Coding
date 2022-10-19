#ข้อ 4
i = 1
name =[]
price = []
while i <= 3:
    x = input("กรุณากรอกชื่อสิ้นค้า : ")
    name.append(x)
    y = int(input("กรุณากรอกราคาสินค้า : "))
    price.append(y)
    i += 1
for (x,y) in zip(name,price):
    print("ชื่อสินค้า :",x,"ราคาสินค้า :",y)
print("ราคารวมทั้งหมด : ",sum(price))
print("Good Bye !!")
