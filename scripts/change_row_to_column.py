# Open the input file in read mode
with open('datain_4096.txt', 'r') as f:
    # Read the content of the file
    data = f.read()

# Replace spaces with newline characters
data = data.replace(' ', '\n')

# Open the output file in write mode
with open('datain_4096.mem', 'w') as f:
    # Write the modified content to the output file
    f.write(data)