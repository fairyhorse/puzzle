import random
   
def buttons():
    lst = []
    for i in range(0, 4):
        n = random.randint(0, 1)
        if n == 1:
            lst.append(True)
        else:
            lst.append(False)
    return lst

btns = buttons()

def press_1():
    i = 0
    while True in btns:
        n = random.randint(0,3)
        btns[n] = not btns[n]
        i += 1
        print(i)
        print(btns)
    return btns

def press_2():
    i = 0
    while True in btns:
        n = random.randint(0,3)
        m = random.randint(0,3)
        rep_check(m, n)
        btns[n] = not btns[n]
        btns[m] = not btns[m]
        i += 1
        print(i)
        print(btns)
    return btns

def press_3():
    i = 0
    while True in btns:
        n = random.randint(0,3)
        m = random.randint(0,3)
        rep_check(m, n)
        l = random.randint(0,3)
        rep_check(l, n, m)
        btns[n] = not btns[n]
        btns[m] = not btns[m]
        btns[l] = not btns[l]
        i += 1
        print(i)
        print(btns)
    return btns


def rep_check(x, n, m = 5):
    while x == n or x == m:
        x = random.randint(0,3)

print(btns)
# print(press_1())
# print(press_2())
print(press_3())


