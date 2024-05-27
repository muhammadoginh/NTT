# for generating file 16-point INTT

from ntt import *


def main():

    print("================== Start Read Data ======================")
    # hat_A was BO
    hat_A = [2415394632, 2885182895, 2454799486, 579623186, 1266560305, 3077892708, 3604369981, 2403754664, 191366503, 2121744335, 1102767478, 1467038560, 4197108775, 1239949925, 3790014788, 2205954673]

    print("================== End Read Data ========================")
    print("")


    q = 4294828033
    psi = 28157506
    psi_inverse = 4009503407


    n = len(hat_A)
    Y_table = psi_table(psi, n, q)
    Y_inv_table = psi_table(psi_inverse, n, q)
    print(Y_inv_table)
    # print(Y_table)


    print("================== Start NTT ======================")
    print("")

    # result = NTT(A, indexReverse(Y_table, int(math.log2(n))), q)
    # result_inv = iNTT(hat_A, indexReverse(Y_inv_table, int(math.log2(len(Y_inv_table)))), q)
    result_inv_DIV2 = iNTT_modified(hat_A, indexReverse(Y_inv_table, int(math.log2(len(Y_inv_table)))), q)
    # result_inv = NTT(hat_A, Y_inv_table, q)

    # modified_lines = '\n'.join(map(str, result))
    # print(data)
    # print(result)
    # print(result_inv)
    print("With DIV2:")
    print(result_inv_DIV2)

    # Write the modified content to the output file
    # with open("ntt_result.txt", 'w') as output_file:
    #     output_file.writelines(modified_lines)

    # Output should be the same as sub_in_ctilda_0.mem
        
    print("================== Finish NTT ======================")
    return 0





# test = nwc_ntt_sw(A, q, psi)
# print(test)

if __name__=="__main__": 
    main() 