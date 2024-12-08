L = [1, 2]

for i in range(2, 48):
    difference = L[i-1] - L[i-2]
    if difference == 0:
        L.append(0)
    else:
        new_element = (L[i-1] + L[i-2]) / difference
        L.append(new_element)

average = sum(L) / len(L)

L_sorted = sorted(L)
n = len(L)
if n % 2 == 0:
    median = (L_sorted[n // 2 - 1] + L_sorted[n // 2]) / 2
else:
    median = L_sorted[n // 2]

unique = set()
duplicates = set()
for val in L:
    if val in unique:
        duplicates.add(val)
    else:
        unique.add(val)

print("List L:", L)
print("Average:", average)
print("Median:", median)
if duplicates:
    print("Repeated values:", duplicates)
else:
    print("No repeated values")
