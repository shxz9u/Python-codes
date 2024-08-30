print("Korean score")
kor = int(input())
if kor > 100:
    print("Wrong Answer")
    exit()
print("Math score")
math = int(input())
if math > 100:
    print("Wrong Answer")
    exit()
print("English socre")
eng = int(input())
if eng > 100:
    print("Wrong Answer")
    exit()

total = kor+math+eng
avg = total/3

print("average :" , avg)