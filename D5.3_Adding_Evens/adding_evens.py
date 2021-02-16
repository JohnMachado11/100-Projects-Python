# Sum of All Even Numbers Between 1-100

# Method 1
total = 0
for i in range(2,101,2):
    total += i

print(total)

# Method 2
total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
        print(i)

print(total)