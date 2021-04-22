x = y = 0
z = 0


def sub1():
    global x
    global y
    z = 1
    print('sub1: %d%d%d' % (x, y, z))  # 0 0 1
    a = 1

    def sub2():
        nonlocal z
        a = 2
        print('sub2: %d%d%d' % (y, z, a))  # 0 1 2
        b = 2

        def sub3():
            nonlocal z
            b = 3
            print('sub3: %d%d%d' % (z, a, b))  # 1 2 3

        sub3()

    sub2()


sub1()

