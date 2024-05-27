from helper import *

# input_filename = "table_rootOfUnity.txt"
# output_filename = "table_rootOfUnity_hex.mem"

input_filename = "in_rns_ntt_4096.mem"
output_filename = "in_rns_ntt_4096_hex.mem"

# # Read the content of the input file
# with open(input_filename, 'r') as input_file:
#     lines = input_file.readlines()

# # Modify the data as needed
# # Convert each number to hexadecimal format
# modified_lines = []
# for line in lines:
#     number = int(line.strip())
#     hex_number = hex(number)[2:]  # [2:] is used to remove the '0x' prefix from hex() output
#     modified_lines.append(hex_number + '\n')

# # Write the modified content to the output file
# with open(output_filename, 'w') as output_file:
#     output_file.writelines(modified_lines)

def convert_to_hex(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read the lines from the file
        lines = f.readlines()

    # Convert each number in each line to hexadecimal
    hex_lines = []
    for line in lines:
        numbers = line.split()
        hex_numbers = [hex(int(num)) for num in numbers]
        hex_lines.append(hex_numbers)
    # print("number of rows", len(hex_lines))

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write the hexadecimal numbers to the output file
        for i in range(len(hex_lines)):
            for hex_line in hex_lines[i]:
                f.write(hex_line[2:] + ' ')
            f.write('\n')

# Paths to input and output files
input_file = 'datain_4096.mem'
output_file = 'datain_4096_hex.mem'

# Convert numbers to hexadecimal and write to output file
convert_to_hex(input_file, output_file)

print("Conversion completed!")
