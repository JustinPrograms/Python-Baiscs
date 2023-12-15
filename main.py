"""
CS1026a 2023
2023-10-05
"""

# Part A: Fibonacci Sequence
print("Project One (01) - Part A: Fibonacci Sequence")

# Get the user's input for the end of the Fibonacci sequence
e = int(input("Sequence ends at: "))

# Initialize variables for the Fibonacci sequence
a = 0
b = 1
position = 0

# Loop to generate and print Fibonacci numbers
while position <= e:
    commaValue = "{:,}".format(a)
    print(f"{position}: {a} {commaValue}")
    a, b = b, a + b
    position += 1

print("\nEND: Project One (01) - Part A\nJustin Dhillon JDHILL94 251348823")
"""
CS1026a 2023
END: Project 01 - Part A
Justin Dhillon
251348823
JDHILL94
2023-10-05
"""
# Part B: Prime Numbers
print("Part One - Project B: Prime Choice")

# Get the user's input for the range of prime numbers
start = int(input("Prime Numbers starting with: "))
end = int(input("and ending with: "))

# Check if the start is greater than the end and swap them if necessary
if start > end:
    start, end = end, start
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
# Part C: Moore's Law
print("Project One (01) - Part B: The Moore the Merrier")


# Function to format FLOPS (Floating Point Operations Per Second)
def format_flops(flops):
    units = ["", "kilo", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta"]
    unit_index = 0
    while flops >= 1000 and unit_index < len(units) - 1:
        flops /= 1000.0
        unit_index += 1
    unit = units[unit_index]
    return f"{flops:.2f} {unit}FLOPS"


# Get user input for initial values
startNum = int(input("Starting Number of transistors: "))
startYear = int(input("Starting Year: "))
startTotal = int(input("Total Number of Years: "))

# Initialize variables
transistors = startNum
year = startYear

print("YEAR  : TRANSISTORS  : FLOPS")

# Calculate and print values for each two-year cycle
total_cycles = startTotal // 2
for _ in range(total_cycles + 1):
    flops = transistors * 50
    formatted_flops = format_flops(flops)
    formatted_transistors = f"{transistors:,}"  # Format transistors with thousands separators
    print(f"{year}  {formatted_transistors} {formatted_flops} {int(flops):,}")

    # Update values for the next two-year cycle
    transistors *= 2
    year += 2

# Check if there is an additional year to calculate
if startTotal % 2 == 1:
    flops = transistors * 50
    formatted_flops = format_flops(flops)
    formatted_transistors = f"{transistors:,}"  # Format transistors with thousands separators
    print(f"{year}  {formatted_transistors} {formatted_flops} {int(flops):,}")

print("\nEND: Project One (01) - Part C\nJustin Dhillon JDHILL94 251348823")
"""
CS1026a 2023
END: Project 01 - Part C
Justin Dhillon
251348823
JDHILL94
2023-10-05
"""