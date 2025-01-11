# Function to calculate factorial
def factorial(n):
    # Step 3: Check if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        # Step 5: Loop from 1 to n
        for i in range(1, n + 1):
            result *= i
        return result

# Step 2: Input a number
n = int(input("Enter a number: "))

# Step 6: Output the result
print(f"The factorial of {n} is {factorial(n)}")
