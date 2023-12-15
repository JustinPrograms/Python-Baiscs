"""
CS1026a 2023
Assignment 01 Project 01 - Part B
2023-10-05
"""
# Part B: Prime Numbers
print("Part One - Project B: Prime Choice")

# Get the user's input for the range of prime numbers
start = int(input("Prime Numbers starting with: "))
end = int(input("and ending with: "))

# Check if the start is greater than the end and swap them if necessary
if start > end:
    start, end = end, start  # Swapping variables
    print(f"Incorrect Input: {end} is greater than {start}\nThe numbers have been automatically switched.\n")


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        # If the number is less than or equal to 1, it's not prime
        return False
    if num <= 3:
        # If the number is 2 or 3, it's prime
        return True
    if num % 2 == 0 or num % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= num:
        # Check if divisible starting from 5 up to the square root of the number
        if num % i == 0 or num % (i + 2) == 0:
            # If the number is divisible by i or i+2, it's not prime
            return False
        i += 6
    # If none of the above conditions are met, the number is prime
    return True


# Print prime numbers within the specified range
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(f"{num} is prime")

print("\nEND Part One - Project B\nJustin Dhillon JDHILL94 251348823")
"""
CS1026a 2023
END: Project 01 - Part B
Justin Dhillon
251348823
JDHILL94
2023-10-05
"""
