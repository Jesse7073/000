import random

while True:
    start = input('請決定數字範圍開始值:')
    end = input('請決定數字範圍結束值:')
    count = 0
    enter = input('請猜' + start + '~' + end + '間的整數:')
    enter = int(enter)
    start = int(start)
    end = int(end)
    r = random.randint(start, end)
    if enter == r:
        print('恭喜猜對了')
        break
    while enter != r:
        count += 1
        if enter > r:
            print('答案比較小，這是你猜的第', count, '次')
        elif enter < r:
            print('答案比較大，這是你猜的第', count, '次')
        enter = input('再猜:')
        enter = int(enter)
        if enter == r:
            print('恭喜猜對了')
            break


