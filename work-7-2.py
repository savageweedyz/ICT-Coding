
enterscore = int(input("กรอกคะแนนเข้าเรียน (*คะแนนเต็ม 10 คะแนน*) = "))
exscore = int(input("กรอกคะแนนแบบฝึกหัด (*คะแนนเต็ม 30 คะแนน) = "))
midscore = int(input("กรอกคะแนนสอบกลางภาค (*คะแนนเต็ม 20 คะแนน*) = "))
finalscore = int(input("กรอกคะแนนสอบปลายภาค (*คะแนนเต็ม 40 คะแนน) = "))

allscore = enterscore+exscore+midscore+finalscore

if allscore >= 80 and allscore <= 100:
    grade = "A"
elif allscore >= 70 and allscore <= 79:
    grade = "B"
elif allscore >= 60 and allscore <= 69:
    grade = "C"
elif allscore >= 50 and allscore <= 59:
    grade = "D"
else: 
    allscore >= 0 and allscore <= 49
    grade = "F"

print("คะแนนที่ได้ทั้งหมด : ",allscore)
print("คุณได้เกรด : ",grade)
