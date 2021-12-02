# Migratory Birds
# TODO: Frequency of birds, highest frequency, if multiple have the same, choose the smallest

def migratoryBirds(myList):
    removeDuplicates = []
    frequency = []

    # Remove Duplicate Numbers
    for x in myList:
        if x not in removeDuplicates:
            removeDuplicates.append(x)

    # Prepare 2D List
    for x in removeDuplicates:
        frequency.append([x])

    for x in frequency:
        x.append(0)

    # Count Frequency
    for x in myList:
        for row in frequency:
            if x == row[0]:
                row[1] += 1

    # Find Highest Frequency and ID
    id = 0
    freq = 0
    multiple = []

    for x in frequency:
        if x[1] > freq:
            freq = x[1]
            id = x[0]

    for x in frequency:
        if x[1] == freq:
            multiple.append(x[0])

    for x in multiple:
        if x < id:
            id = x

    return id



print(migratoryBirds([1, 1, 2, 2, 3]))
print(migratoryBirds([2, 2, 1, 1, 3]))
print(migratoryBirds([4, 4, 2, 2, 3, 5]))
print(migratoryBirds([7, 7, 7, 3, 3, 3, 2, 5, 10, 1]))