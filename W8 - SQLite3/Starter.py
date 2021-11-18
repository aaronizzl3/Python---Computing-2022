# TODO: Create a function which checks if all nums in list are equal
# TODO: Must use a parameter and a return

# My Function
def all_equal(my_list):
    comparison = my_list[0]
    for x in my_list:
        if x != comparison:
            return False

    return True


# Test Cases
print(all_equal([1, 1, 1]))
print(all_equal([2, 2, 0]))
print(all_equal([1, 2, 1]))
print(all_equal([4, 4, 4, 5, 1, 4, 4, 1, 4]))
print(all_equal([3, 3, 3, 3, 3, 3]))