"""
CS1026a 2023
Assignment 01 Project 01 - Part A
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
    comma_value = "{:,}".format(a)
    print(f"{position}: {a} {comma_value}")
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
