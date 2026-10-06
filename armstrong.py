num = int(input("Enter a number: "))

temp = num
digits = 0
while temp > 0:
    digits += 1
    temp = temp // 10

temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")