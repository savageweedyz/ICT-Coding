#universe
set_A = {3,5,7,8,8,9,9,10,11,14,14,19}
set_B = {4,4,6,7,9,12,21,22,23}
set_C = {5,6,10,24,25}

print("1.1) เซตของ A & B = ", set_A & set_B)
print("1.2) เซตของ A & C = ", set_B & set_C)
print("1.3) เซตของ B | C = ", set_B | set_C)
print("1.4) เซตของ A | C = ", set_A | set_C)
print("1.5) เซตของ A - C = ", set_A - set_C)
print("1.6) เซตของ B - A = ", set_B - set_A)
print("1.7) เซตของ A ^ B = ", set_A ^ set_B)
print("1.8) เซตของ B ^ C = ", set_B ^ set_C)
print("-----------------------------")
num = 0
for i in set_A:
    print(i)
    num = num + i
print("ผลรวม = ",num)