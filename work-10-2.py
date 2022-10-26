try:
    n = int(input("กรุณากรอกคะแนนไม่เกิน 10 คะแนน : "))
    if n < 10:
        while n <= 10:
            print(n,end= " ")
            n = n + 1
except ValueError:
    print("คุณป้อนข้อมูลไม่ถูกต้อง")