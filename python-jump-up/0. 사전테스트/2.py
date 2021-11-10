import sys

def Input_Data():
    readl = sys.stdin.readline
    s = input().strip()
    return s


sol = -1

# 입력받는 부분
s = Input_Data()

# 여기서부터 작성

plates = list(s)
length_sum = 0
for i, current_plate in enumerate(plates):
    if i == 0:
        previous_plate = current_plate
        length_sum = 10
    else:
        if previous_plate == current_plate:
            length_sum += 5
        else:
            length_sum += 10

        previous_plate = current_plate

sol = length_sum

# 출력하는 부분
print(sol)