#65701976 นายธนกร พันธมาศ
from ast import Pass

class PassTestError(Exception):
    pass
class FailTestError(Exception):
    pass
class WrongTestError(Exception):
    pass

try:
    n = int(input("กรุณากรอกคะแนน : "))
    if n <= 20:
        raise WrongTestError
    elif n > 20 and n <= 50:
        raise FailTestError
    else:
        raise PassTestError
        
except FailTestError:
    print("คุณไม่ผ่านเกณฑ์ 50 คะแนน คะแนนที่คุณได้คือ %d คะแนน" %n)
except WrongTestError:
    print("คุณสอบไม่ผ่านเนื่องจากคะแนนต่ำไป ต้องสอบใหม่")
except PassTestError:
    print("ยินดีด้วยคุณสอบผ่าน คะแนนที่คุณได้คือ %d คะแนน" %n)
except ValueError:
    print("คุณป้อนข้อมูลไม่ถูกต้อง")

