# MyNumber.py
# 함수를 직접 만들어 써봅시다.
import random

# 단계를 선택합니다.
level=input("숫자 맞추기 게임을 시작합니다. 단계를 골라주세요.\n 상:h 중:m 하:e")
while level !="e" and level !="m" and level !="h":
    level = input("죄송하지만 다시 입력해주세요. 상:h 중:m 하:e \n h/m/e:")

# 숫자를 골라봅시다.
if level == 'e':
    computer_number = random.randint(1, 10)
    highest_number = 10
if level == 'm':
   computer_number = random.randint(1,20)
   highest_number = 20
if level == 'h':
    computer_number = random.randint(1, 100)
    highest_number = 100

# is_same() 함수를 만듭니다.
def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
    return result

# 게임을 시작합니다.
print("안녕,\n난 1부터", highest_number, "중 숫자 하나를 골랐어요.")

# 사용자가 추측한 숫자를 인수로 받아옵니다.
guess = int(input("뭔지 쓰고 엔터키를 누르세요"))
# is_same() 함수를 사용합니다.
higher_or_lower = is_same(computer_number, guess)

# 사용자가 맞출때까지 게임을 합니다.
counter = 1
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("그것보단 높습니다. 다시 생각해보세요."))
        counter = counter + 1
    else:
        guess = int(input("그것보단 낮습니다. 다시 생각해보세요."))
        counter = counter + 1

    higher_or_lower = is_same(computer_number, guess)

# 게임을 끝냅니다.
input("정답!\n잘했어요.\n\n마치려면 엔터키를 누르세요.")

# 맞출때까지 몇 번 추측하였는지 알려줍니다.
print(counter, "번 추측하였습니다.")