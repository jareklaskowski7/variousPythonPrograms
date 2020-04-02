#

def calculateReports(ranks):
    uniqueRanks = set(ranks)
    reports = 0

    for uniqueRank in uniqueRanks:
        for rank in ranks:
            if rank + 1 == uniqueRank:
                reports += 1

    return reports


ranks = [3, 4, 3, 0, 2, 2, 3, 0, 0]
reports = calculateReports(ranks)
print(reports)
