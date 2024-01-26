import os

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
# print("Current Working Directory:", current_directory)

rns_modulo = os.path.join(current_directory, "keyswitching/ks/rns_modulo.mem")

# These data will be compared to output of dyadic multiplication
ks_in_c0 = os.path.join(current_directory, "keyswitching/ks/input/ks_in_c0.mem")
ks_in_c1 = os.path.join(current_directory, "keyswitching/ks/input/ks_in_c1.mem")
ks_in_c2 = os.path.join(current_directory, "keyswitching/ks/input/ks_in_c2.mem")

ks_out_c0 = os.path.join(current_directory, "keyswitching/ks/output/ks_out_c0.mem")
ks_out_c1 = os.path.join(current_directory, "keyswitching/ks/output/ks_out_c1.mem")

# These data will be used as input for dyadic multiplication
mult_in_x0 = os.path.join(current_directory, "keyswitching/mult/input/mult_in_x0.mem")
mult_in_x1 = os.path.join(current_directory, "keyswitching/mult/input/mult_in_x1.mem")
mult_in_y0 = os.path.join(current_directory, "keyswitching/mult/input/mult_in_y0.mem")
mult_in_y1 = os.path.join(current_directory, "keyswitching/mult/input/mult_in_y1.mem")

# These data will be used as modulus
rns_modulo = os.path.join(current_directory, "keyswitching/ks/rns_modulo.mem")


def dyadic(data_in_x, data_in_y, q):
    """The output is cv which have three elements
    x and y is cihpertext in polynomial form
    cv[0] = x[0]*y[0] mod q
    cv[1] = x[0]*y[1] + x[1]*y[0] mod q
    cv[2] = x[1]*y[1] mod q
    """

    cv0 = [x * y % q[0] for x, y in zip(data_in_x[0], data_in_y[0])]
    cv1 = [(x0 * y1 + x1 * y0) % q[0] for x0, x1, y0, y1 in zip(data_in_x[0], data_in_x[1], data_in_y[0], data_in_y[1])]
    cv2 = [x * y % q[0] for x, y in zip(data_in_x[1], data_in_y[1])]

    cv = [cv0, cv1, cv2]    # this value will compared to ks_in

    return cv

def keySwitchCore():
    return 0

# Open file for reading
with open(mult_in_x0, 'r') as f_mult_in_x0, open(mult_in_x1, 'r') as f_mult_in_x1, open(mult_in_y0, 'r') as f_mult_in_y0, open(mult_in_y1, 'r') as f_mult_in_y1, open(rns_modulo, 'r') as f_rns_modulo:
    # Read the file line by line
    for line_in_x0, line_in_x1, line_in_y0, line_in_y1, line_rns_modulo in zip(f_mult_in_x0, f_mult_in_x1, f_mult_in_y0, f_mult_in_y1, f_rns_modulo):
        # print(line.strip())  # strip() removes trailing newline characters

        # parse the data
        parsed_data_in_x0 = [int(num) for num in line_in_x0.strip().split()]
        parsed_data_in_x1 = [int(num) for num in line_in_x1.strip().split()]
        parsed_data_in_y0 = [int(num) for num in line_in_y0.strip().split()]
        parsed_data_in_y1 = [int(num) for num in line_in_y1.strip().split()]
        parsed_data_rns_modulo = [int(num) for num in line_rns_modulo.strip().split()]

        # print the parsed data
        # print(parsed_data_in_x0)
        # print(parsed_data_in_x1)
        # print(parsed_data_in_y0)
        # print(parsed_data_in_y1)
        # print(parsed_data_rns_modulo)

        # print([x for x in parsed_data_in_x0])

        parsed_data_in_x = parsed_data_in_x0, parsed_data_in_x1
        parsed_data_in_y = parsed_data_in_y0, parsed_data_in_y1


        data_in_x = [x * y % parsed_data_rns_modulo[0] for x, y in zip(parsed_data_in_x[0], parsed_data_in_y[0])]
        data_in_y = parsed_data_in_y0 + parsed_data_in_y1
        # print(data_in_x)

        # print(line_in_x0[0], line_in_x1)
        cv = dyadic(parsed_data_in_x, parsed_data_in_y, parsed_data_rns_modulo)
        print(cv[1])

        # print(parsed_data_rns_modulo[0])

