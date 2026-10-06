n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for j in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()