# 1. Basic
for x in range(51):
    print(x)

#2. Multiples of Five
for x in range(5, 1005, 5):
    print(x)

#3. Counting, the Dojo Way
for x in range(1, 101, 1):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Dojo")

#4.Whoa. That Sucker's Huge
final_sum = 0
for x in range(1, 500000, 2):
    final_sum += x
print(final_sum)

#5. Countdown by Fours
for x in range(2018, 0, -4):
    print(x)

#6. Flexible Counter
def flexible_counter(low_num, high_num, mult):
    for x in range(low_num, high_num +1):
        if x % mult == 0:
            print(x)

flexible_counter(2, 9, 3)

 