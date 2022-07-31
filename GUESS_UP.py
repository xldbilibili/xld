def check_guess_bilibili(guess,answer):
    global score
    still_guessing = True
    times = 0
    while still_guessing and times < 1:
        if guess == answer:
            print('Correct!')
            score = score + 1
            still_guessing = False
        else:
            if times < 1:
                guess = input('打错了，再输一次答案吧')
            times = times + 1
    if times == 1:
        print('正确答案是' + answer)
score = 0
print('WELCOME TO 猜猜B站')
guess1 = input('粉丝量第一的UP主是谁')
check_guess_bilibili(guess1,'老番茄')
guess2 = input('拜访过TIM COOK的UP主是谁    写全名')
check_guess_bilibili(guess2,'老师好我叫何同学')
guess3 = input('我__你____!   答案用分号隔开')
check_guess_bilibili(guess3,'日；仙人')

print('你的分数是 ' + str(score))
