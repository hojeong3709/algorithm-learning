'''

최근에 개발된 지능형 기차가 1번역(출발역)부터 4번역(종착역)까지 4개의 정차역이 있는 노선에서 운행되고 있다. 이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다. 이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산하려고 한다. 단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여, 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.
  


 
예를 들어, 위와 같은 경우를 살펴보자. 이 경우, 기차 안에 사람이 가장 많은 때는 2번역에서 3명의 사람이 기차에서 내리고, 13명의 사람이 기차에 탔을 때로, 총 42명의 사람이 기차 안에 있다.
 
이 기차는 다음 조건을 만족하면서 운행된다고 가정한다.
(1) 기차는 역 번호 순서대로 운행한다.
(2) 출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0이다.
(3) 각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
(4) 기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다.
 
4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

0 32
3 13
28 25
39 0

42

'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    list_inout = [list(map(int,readl().split())) for _ in range(4)]
    return list_inout


sol = -1
#입력받는 부분
list_inout = Input_Data()

#여기서 부터 작성

# print(list_inout)

max_person_in_train = 0
current_person_in_train = 0
for station in list_inout:
    current_person_in_train = current_person_in_train - station[0] + station[1]
    if max_person_in_train < current_person_in_train:
        max_person_in_train = current_person_in_train

sol = max_person_in_train
# print(max_person_in_train)
    
#출력 하는 부분
print(sol)