# Sum of All Even Numbers Between 1-100

# Method 2
total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
        print(i)

print(total)

