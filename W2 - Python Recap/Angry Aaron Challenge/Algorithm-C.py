# T = Threshold
# A = Arrival Times of Students

def angryAaron(T, A):
    late = 0

    for x in A:
        if x <= 0:
            late += 1

    if late > T:
        return "Yes"
    else:
        return "No"


print(angryAaron(3, [-2, -1, 0, 1, 2]))
print(angryAaron(1, [-1, -1, 0, 1, 2, 3, 4, 5, 6]))
print(angryAaron(5, [5, 6, 7, 8, 9, 10, -1]))
print(angryAaron(4, [-3, -4, -1, -5, 1, 2]))
print(angryAaron(4, [-3, -4, -1, -5, 1, 2, -1]))
