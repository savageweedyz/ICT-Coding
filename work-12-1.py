import math

while(True):
    print("+++++++++ โปรแกรมคำนวณหาพื้นที่ต่างๆ เลือกเมนูที่ต้องการทำงาน +++++++++")
    print("กด 1 หาพื้นที่สามเหลี่ยมไม่เท่ากัน | กด 2 หาพื้นที่สามเหลี่ยมรูปว่าว | กด 3 หาพื้นที่ปริมาตรทรงกลม | กด N เพื่อหยุดการทำงาน")
    i = input("กรุณาเลือกเมนู : ")
    if(i == "N" or i == "n"):
        print("-------- End Program ---------")
        break
    elif(i == '1'):
        angle = int(input("เส้นทแยงมุม : "))
        result = int(input("ผลบวกของเส้นกิ่ง : "))
        def notrectangle():
            n1 = 0.5 * angle * result
            return n1
        print("พื้นที่สี่เหลี่ยมไม่เท่ากัน : ",notrectangle())
    elif(i == '2'):
        multiply = float(input("เส้นทแยงมุมเส้นที่ 1 : "))
        multiplys = float(input("เส้นทแยงมุมเส้นที่ 2 : "))
        def kiterectangle():
            n2 = 0.5 * (multiply * multiplys)
            return n2
        print("พื้นที่สี่เหลี่ยมรูปว่าว : ",kiterectangle())
    elif(i == '3'):
        r = float(input("ค่าของ r : "))
        def circle():
            n3 = 4/3 * 3.14 * math.pow(r,3)
            return n3
        print("พื้นที่ปริมาตรทรงกลม : ",circle())
    


