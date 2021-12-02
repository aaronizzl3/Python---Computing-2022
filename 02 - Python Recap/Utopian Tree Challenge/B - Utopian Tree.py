# TODO: +1, *2

def utopianTree(n):
    height = 1
    Spring = True

    while n > 0:
        if Spring:
            height *= 2
            Spring = False
            n -= 1
        else:
            height += 1
            n -= 1
            Spring = True

    return height


print(utopianTree(5))
print(utopianTree(10))
print(utopianTree(3))
print(utopianTree(4))