p = [False, True, False, True]
q = [False, False, True, True]


def firstTheMorganLaw(p, q):
    print(f"First the Morgan law for p={p} and q={q} is {isTheTAOT(not (p and q), (not p) or (not q))}")
    return 0


def secondTheMorganLaw(p, q):
    print(f"Second the Morgan law for p={p} and q={q} is {isTheTAOT(not (p or q), (not p) and (not q))}")
    return 0


def isTheTAOT(p, q):
    if p == q:
        return True
    return False


for i in range(len(p)):
    firstTheMorganLaw(p[i], q[i])
    secondTheMorganLaw(p[i], q[i])
