L1 = []

for i in range(10):
    L1.append(input(f"Enter a string({i + 1}/10): "))

print("L1 elements:")
for element in L1:
    print(element)

L2 = []

for i in L1:
    L2.append(len(i))

print("Lenghts in L2:")
for element in L2:
    print(element)

    for i in range(len(L2) - 1):
        for j in range(0, len(L2) - i - 1):
            if L2[j] > L2[j + 1]:
                L2[j], L2[j + 1] = L2[j + 1], L2[j]

print("Sorted L2:")
for element in L2:
    print(element)
