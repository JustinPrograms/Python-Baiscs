# Part C: Moore's Law
print("Project One (01) - Part B: The Moore the Merrier")


# Function to format FLOPS (Floating Point Operations Per Second)
def format_flops(flops):
    units = ["", "kilo", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta"]  # Setting the type of unit for output
    unit_index = 0  # Pre setting index to 0 to just print out "FLOPS" if its not big enough
    # Checks which unit the output should be printed in
    while flops >= 1000 and unit_index < len(units) - 1:
        flops /= 1000.0
        unit_index += 1
    unit = units[unit_index]
    return f"{flops:.2f} {unit}FLOPS"


# Get user input for initial values
transistors = int(input("Starting Number of transistors: "))
year = int(input("Starting Year: "))
start_total = int(input("Total Number of Years: "))

print("YEAR  : TRANSISTORS  : FLOPS")

# Calculate and print values for each two-year cycle
total_cycles = start_total // 2  # Because its every two years we do integer division of 2
for _ in range(total_cycles + 1):
    flops = transistors * 50  # Formula given in the assignment to calculate the flops
    formatted_flops = format_flops(flops)  # Adding commas to bigger numbers and the units
    formatted_transistors = f"{transistors:,}"  # Format transistors with commas
    print(f"{year}  {formatted_transistors} {formatted_flops} {int(flops):,}")

    # Update values for the next two-year cycle
    transistors *= 2
    year += 2

# Check if there is an additional year to calculate
if start_total % 2 == 1:
    flops = transistors * 50  # Formula given in the assignment to calculate the flops
    formatted_flops = format_flops(flops)  # Adding commas to bigger numbers and the units
    formatted_transistors = f"{transistors:,}"  # Format transistors with commas
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
