count = 0
for x in range(1, 40):
    for y in range(1, 20):
        if (y < x * 3 ** 0.5) and (y > (x - 8) * 3 ** 0.5) and (y < (64 - 16)**(1/2)):
            count += 1
print(count)
