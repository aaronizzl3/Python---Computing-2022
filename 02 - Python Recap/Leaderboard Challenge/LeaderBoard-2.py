def leaderboard(r, p):
    ranks = []

    for x in p:
        r.append(x)
        r.sort()
        r.reverse()

        removeDuplicates = []

        for y in r:
            if y not in removeDuplicates:
                removeDuplicates.append(y)

        ranks.append(removeDuplicates.index(x) + 1)
        r.remove(x)

    return ranks

ranked = [100, 90, 90, 80]
player = [85, 70, 105]

print(leaderboard(ranked, player))