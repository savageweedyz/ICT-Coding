import math

print("--------------------โปรแกรมคำนวณค่า BMI--------------------")
name = input("Please Enter your name : ")
Height = int(input("Please input Height (cm.) : "))
Weight = int(input("Please input Weight (kg.) : "))

Height1 = Height / 100
res = (Weight/(math.pow(Height1,2)))

if res >= 30: 
    detail = "โรคอ้วนอันตราย"
elif 25.0 >= res <= 29.9:
    detail =  "โรคอ้วน"
elif 23.0 >= res <= 24.9:
    detail = "น้ำหนักเกิน"
elif 18.5 >= res <= 22.9:
    detail = "สมส่วน"
else:
    18.5 <= res
    detail = "น้ำหนักต่ำกว่าเกณฑ์"

print("-------------------สรุปผลค่า BMI--------------------")
print("Name","     Height","  Weight","  BMI","     Detail")
print("--------------------------------------------------")
print(name,"     ",Height,"    ",Weight,"   ",format(res,'.2f'),"    ",detail)
print("--------------------------------------------------")