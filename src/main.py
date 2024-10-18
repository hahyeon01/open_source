# 양수와 음수의 개수를 세는 프로그램

# a개의 정수를 입력받기
a = int(input("Enter the number of integers: "))

# 양수와 음수의 개수를 저장할 변수
positive_count = 0
negative_count = 0

# a개의 정수를 입력받아 양수인지 음수인지 판별
for i in range(a):
    x = int(input(f"Enter integer {i + 1}: "))

    if x < 0:
        negative_count += 1
    else:
        positive_count += 1

# 결과 출력
print(f"Positive integer: {positive_count}\nNegative integer: {negative_count}")
