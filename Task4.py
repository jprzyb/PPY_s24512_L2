def rowCount(buildings, k):
    rows = 1
    actualBuilding = 0
    for soldiersCount in buildings:
        if actualBuilding + soldiersCount <= k:
            actualBuilding += soldiersCount
        else:
            rows += 1
            actualBuilding = soldiersCount
    return rows

def findMinRowsCount(buildings):
    lowerBorder = max(buildings)
    upperBorder = sum(buildings)
    while lowerBorder < upperBorder:
        middle = (lowerBorder + upperBorder) // 2
        if rowCount(buildings, middle) <= middle:
            upperBorder = middle
        else:
            lowerBorder = middle + 1
    return lowerBorder

def validateBuildingsCount(buildings):
    if buildings < 1:
        print("Too few buildings. Minimum is one. Changed to 1.")
        buildings = 1
    elif buildings > 500000:
        print("Too many buildings. Maximum is 500 000. Changed to 500 000.")
        buildings = 500000
    return buildings

def validateSoldiersCount(builings):
    for x in builings:
        if x < 1:
            print("Too few soldiers. Minimum is 1. Changed to 1.")
            x = 1
        elif x > 10 ** 9:
            print("Too many soldiers. Maximum is 10**9. Changed to 10**9.")
            x = 10 ** 9
    return builings


# Input
n = int(input("How many buildings do you want?: "))
n = validateBuildingsCount(n)
buildings = [int(input(f"Enter number of soldiers in {_+1}. building: ")) for _ in range(n)]
buildings = validateSoldiersCount(buildings)

# Output
print("Minimal row count is ", findMinRowsCount(buildings))
