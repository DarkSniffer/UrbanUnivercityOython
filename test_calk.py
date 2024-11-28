import calk


def test_add():
    if calk.add(1, 2) != 3:
        print("Test add(a, b) failed")
    else:
        print("Test add(a, b) passed")


def test_sub():
    if calk.sub(3, 2) != 1:
        print("Test sub (a, b) failed")
    else:
        print("Test sub (a, b) passed")


def test_mul():
    if calk.mul(2, 2) != 4:
        print("Test mul (a, b) failed")
    else:
        print("Test mul (a, b) passed")

def test_div():
    if calk.div(6, 2) != 3:
        print("Test div (a, b) failed")
    else:
        print("Test div (a, b) passed")



test_add()
test_sub()
test_mul()
test_div()