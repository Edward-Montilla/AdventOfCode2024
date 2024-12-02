# get the list from another input file

# break up the list into two different list
big = []
with open('input.txt', 'r') as file:
    for line in file:
        # Split the line by '    ' and strip any trailing newline or whitespace
        split_line = line.strip().split('    ')
        big.append(split_line[0])

left = []
right = []


for row in big:
    for element in row:
        parts = element.split('    ')  # Split the element into parts
        left.append(int(parts[0]))    # Convert and append the left part
        right.append(int(parts[1]))   # Convert and append the right part

print("Left:", left)
print("Right:", right)# sort by ascending order

# compare each element in both list to each other and find the difference, compile them into another list

# add up each element of the list of differences