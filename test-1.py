
collectscore = int(input("กรอกคะแนนเก็บ(สูงสุด 40 คะแนน*) : "))
midscore = int(input("กรอกคะแนนสอบกลางภาค(สูงสุด 20 คะแนน*) : "))
finalscore = int(input("กรอกคะแนนสอบปลายภาค(สูงสุด 40 คะแนน*) : "))

allscore = collectscore+midscore+finalscore

if allscore >= 80:
    grade = "A"
elif allscore >= 75 and allscore <= 79:
    grade = "B+"
elif allscore >= 70 and allscore <= 74:
    grade = "B"
elif allscore >= 65 and allscore <= 69:
    grade = "C+"
elif allscore >= 60 and allscore <= 64:
    grade = "C"
elif allscore >= 55 and allscore <= 59:
    grade = "D+"
elif allscore >= 50 and allscore <= 54:
    grade = "D"
else: 
    allscore <= 50 
    grade = "F"

print("----------โปรแกรมตัดเกรด----------")
print("คะแนนเก็บ(40 คะแนน) : ",collectscore)
print("คะแนนสอบกลางภาค(20 คะแนน) : ",midscore)
print("คะแนนสอบปลายภาค(40 คะแนน) : ",finalscore)
print("----------สรุปคะแนน----------")
print("คะแนนรวมทั้งหมด : ",allscore)
print("ได้เกรด : ",grade)