

# input()
xs = list(map(int, input().split(' ')))

i = 0
entropy = 0
for x in xs:
    for j in range(i + 1, len(xs)):
        if xs[i] > xs[j]:
            entropy = entropy + 1
    i += 1

print(entropy)
