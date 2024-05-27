# This project contain implementation of ciphertext multiplication. It includes two steps: dyadic multiplication and relinearization
# or key switching


import os
import math
import RNS
from helper import *

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
# print("Current Working Directory:", current_directory)

# Get the OpenFHE IO directory
ofhe_io = os.path.join(current_directory, "../simulation_data/ofhe_io/")

################################################################################
################# File preparation for ciphertext multiplication ###############
################################################################################
# These data will be used as input for dyadic multiplication
mult_in_x0 = os.path.join(ofhe_io, "mult/input/mult_in_x0.mem")
mult_in_x1 = os.path.join(ofhe_io, "mult/input/mult_in_x1.mem")
mult_in_y0 = os.path.join(ofhe_io, "mult/input/mult_in_y0.mem")
mult_in_y1 = os.path.join(ofhe_io, "mult/input/mult_in_y1.mem")


# These data will be used as modulus
rns_modulo = os.path.join(ofhe_io, "ks/rns_modulo.mem")
rns_rootOfUnity = os.path.join(ofhe_io, "ks/rns_rootOfUnity.mem")

# These data will be compared to output of dyadic multiplication
# These data will be used as input for relinearization
ks_in_c0 = os.path.join(ofhe_io, "ks/input/ks_in_c0.mem")
ks_in_c1 = os.path.join(ofhe_io, "ks/input/ks_in_c1.mem")
ks_in_c2 = os.path.join(ofhe_io, "ks/input/ks_in_c2.mem")

# These data will be compared to output of relinearization
ks_out_c0 = os.path.join(ofhe_io, "ks/output/ks_out_c0.mem")
ks_out_c1 = os.path.join(ofhe_io, "ks/output/ks_out_c1.mem")

# These data will be used for polynomial addition after modulus down
md_out_ctilda_0 = os.path.join(ofhe_io, "mod_down/output/md_out_ctilda_0.mem")
md_out_ctilda_1 = os.path.join(ofhe_io, "mod_down/output/md_out_ctilda_1.mem")


################################################################################
################# File preparation for Relinearization #########################
################################################################################



#################################################################
################# Dyadic Multiplication #########################
def dyadic(data_in_x, data_in_y, q):
    """
    dyadic(data_in_x, data_in_y, q) implement dyadic multiplication
    The output is cv which have three elements
    x and y is cihpertext in polynomial form
    cv[0] = x[0]*y[0] mod q
    cv[1] = x[0]*y[1] + x[1]*y[0] mod q
    cv[2] = x[1]*y[1] mod q

    data_in_x and data_in_y, have two elements, and each element are data 2 dimension
    """

    cv0 = [[x * y % q[i] for x, y in zip(data_in_x[0][i], data_in_y[0][i])] for i in range(len(data_in_x[0]))]
    cv1 = [[(x0 * y1 + x1 * y0) % q[i] for x0, x1, y0, y1 in zip(data_in_x[0][i], data_in_x[1][i], data_in_y[0][i], data_in_y[1][i])] for i in range(len(data_in_x[0]))]
    cv2 = [[x * y % q[i] for x, y in zip(data_in_x[1][i], data_in_y[1][i])] for i in range(len(data_in_x[0]))]

    cv = [cv0, cv1, cv2]    # this value will compared to ks_in

    return cv

#################################################################
################# Dyadic Multiplication #########################
def RNSDecompose():
    """
    L : Maximum multiplicative depth level
    l : current multiplicative level
    """
    beta = math.ceil(l / k)
    return 0

#################################################################
################# Dyadic Multiplication #########################
def BCONV():
    return 0


#################################################################
################# Modulus Raising ###############################
def ModUp():
    return 0

#################################################################
################# Key Multiplication ############################
def KeyMult():
    return 0

#################################################################
################# Modulus Reduction #############################
def ModDown():
    return 0

#################################################################
################# Keyswitching core #############################
def keySwitchCore(cv2, evk, q):
    cHat0 = evk[0]
    cHat1 = evk[1]
    cHat = [cHat0, cHat1]
    return cHat

#################################################################
################# Ciphetext Multiplication ######################
def CMult(data_in_x, data_in_y, evk, q):

    # Dyadic multiplication
    cv = dyadic(data_in_x, data_in_y, q)

    # Keyswitching core
    cHat = keySwitchCore(cv[2], evk, q)

    cTilde0 = [[x + y % q[i] for x, y in zip(cv[0][i], cHat[0][i])] for i in range(len(data_in_x[0]))]
    cTilde1 = [[x + y % q[i] for x, y in zip(cv[1][i], cHat[1][i])] for i in range(len(data_in_x[0]))]

    cTilde = [cTilde0, cTilde1]
    return cTilde

a = [281474976317441, 140737466204161, 140737522302977, 140737468170241, 140737518764033, 140737470791681, 140737513783297, 140737471578113, 140737513259009, 140737471971329, 140737509851137, 140737480359937, 140737509457921, 140737481801729, 140737508671489, 140737482981377, 140737506705409, 140737483898881, 140737504608257, 140737484685313, 140737499496449, 140737485864961, 140737493729281, 140737486520321, 140737490976769, 140737487306753, 140737488486401, 281474975662081, 281474974482433, 281474966880257]


def main():

    # print(read_1d_data(rns_rootOfUnity))

    x0 = read_2d_data(mult_in_x0)
    x1 = read_2d_data(mult_in_x1)
    y0 = read_2d_data(mult_in_y0)
    y1 = read_2d_data(mult_in_y1)

    evk0 = read_2d_data(md_out_ctilda_0)
    evk1 = read_2d_data(md_out_ctilda_1)

    moduli = read_1d_data(rns_modulo)

    # print(len([evk0][0][1]))



    print(CMult([x0, x1], [y0, y1], [evk0, evk1], moduli)[1][26][0])

    # Compare output generated by OpenFHE and the output from algorithm that have been implemented
    # if read_1d_data(rns_modulo_t) == a:
    #     print("Data valid")
    # else:
    #     print("Logical error")


    



    # # Open file for reading
    # with open(mult_in_x0, 'r') as f_mult_in_x0, open(mult_in_x1, 'r') as f_mult_in_x1, open(mult_in_y0, 'r') as f_mult_in_y0, open(mult_in_y1, 'r') as f_mult_in_y1, open(rns_modulo, 'r') as f_rns_modulo:
    #     # Read the file line by line
    #     for line_in_x0, line_in_x1, line_in_y0, line_in_y1, line_rns_modulo in zip(f_mult_in_x0, f_mult_in_x1, f_mult_in_y0, f_mult_in_y1, f_rns_modulo):
    #         # print(line.strip())  # strip() removes trailing newline characters

    #         # parse the data
    #         parsed_data_in_x0 = [int(num) for num in line_in_x0.strip().split()]
    #         parsed_data_in_x1 = [int(num) for num in line_in_x1.strip().split()]
    #         parsed_data_in_y0 = [int(num) for num in line_in_y0.strip().split()]
    #         parsed_data_in_y1 = [int(num) for num in line_in_y1.strip().split()]
    #         parsed_data_rns_modulo = [int(num) for num in line_rns_modulo.strip().split()]

    #         # print the parsed data
    #         # print(parsed_data_in_x0)
    #         # print(parsed_data_in_x1)
    #         # print(parsed_data_in_y0)
    #         # print(parsed_data_in_y1)
    #         # print(parsed_data_rns_modulo)

    #         # print([x for x in parsed_data_in_x0])

    #         parsed_data_in_x = parsed_data_in_x0, parsed_data_in_x1
    #         parsed_data_in_y = parsed_data_in_y0, parsed_data_in_y1


    #         data_in_x = [x * y % parsed_data_rns_modulo[0] for x, y in zip(parsed_data_in_x[0], parsed_data_in_y[0])]
    #         data_in_y = parsed_data_in_y0 + parsed_data_in_y1
    #         # print(data_in_x)

    #         # print(line_in_x0[0], line_in_x1)
    #         # cv = dyadic(parsed_data_in_x, parsed_data_in_y, parsed_data_rns_modulo)
    #         # print(cv[0])

    #         # print(parsed_data_rns_modulo[0])

if __name__ == '__main__':
    """
    check if the Python script is being run directly by the interpreter, rather than being imported as a module into another script.
    """
    main()