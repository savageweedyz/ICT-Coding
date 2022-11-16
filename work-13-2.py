class Currency:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def multiply(self):
        return self.num1 * self.num2

nationnal = ("กด 1 ค่าเงินดอลลาร์สหรัฐ | กด 2 ค่าเงินยูโร | กด 3 ค่าเงินวอนเกาหลีใต้ | กด N จบโปรแกรม")

while(True):
    print("++++++++++ โปรแกรมคำนวณอัตรแลกเปลี่ยนค่าเงินบาท เลือกเมานูที่ต้องการ ++++++++++")
    print(nationnal)
    i = input("กรุณาเลือกเมนูที่ต้องการ : ")
    if(i == "N" or i == "n"):
        print("---------- End Program ----------")
        break
    elif(i == "1"):
        cur = 0.028
        baht = int(input("ป้อนค่าเงินบาทไทย : "))
        b = Currency(cur,baht)
        print("จำนวนเงิน : ",baht," บาท"," = ",b.multiply(), "ดอลลาร์")
    
    elif(i == "2"):
        cur = 0.027
        baht = int(input("ป้อนค่าเงินบาทไทย : "))
        b = Currency(cur,baht)
        print("จำนวนเงิน : ",baht," บาท"," = ",b.multiply(), "ยูโร")

    elif(i == "3"):
        cur = 36.94
        baht = int(input("ป้อนค่าเงินบาทไทย : "))
        b = Currency(cur,baht)
        print("จำนวนเงิน : ",baht," บาท"," = ",b.multiply(), "วอน")