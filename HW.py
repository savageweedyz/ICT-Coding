#ข้อ 4 (65701976 ธนกร พันธมาศ)
num = int(input("ตำแหน่งที่ 1 คือ : "))
num2 = int(input("ตำแหน่งที่ 2 คือ : "))
num3 = int(input("ตำแหน่งที่ 3 คือ : "))
num4 = int(input("ตำแหน่งที่ 4 คือ : "))
num5 = int(input("ตำแหน่งที่ 5 คือ : "))
Number = [num,num2,num3,num4,num5]
i = 0
for n in Number:
    print("ตำแหน่งที่ ",i,"คือ",n)
    i += 1
else:
    print("ค่าสูงสุดคือ ", max(Number))
    print("ค่าตำสุดคือ ", min(Number))
    print("ผลรวมคือ ", sum(Number))