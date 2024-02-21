# Cooley-Tukey Butterfly Structure
# A0,A1: input coefficients
# W: twiddle factor
# q: modulus
# B0,B1: output coefficients
def CT_Butterfly(A0,A1,W,q):
    """
    A0 -------\--|+|-- B0
               \/
               /\
    A1 --|x|--/--|-|-- B1
    """
    M = (A1 * W) % q

    B0 = (A0 + M) % q
    B1 = (A0 - M) % q

    return B0,B1


# test case 1
A0 = 130455573527732
A1 = 121359353590460
Y = 78055169708279     # w = 281474976710128
q = 281474976710129
mu = 2251799813689464

A0 = 1
A1 = 3
Y = 281474976710128 
q = 281474976710129

B0, B1 = CT_Butterfly(A0,A1,Y,q)
print(CT_Butterfly(A0,A1,Y,q))

# # test case antara 1 dan 2
# A0 = 61653229515297
# A1 = 121359353590460

# print(CT_Butterfly(A0,A1,Y,q))
    
# test case 2
A0 = 61653229515297
A1 = 83779149426712

A0 = 2
A1 = 4
Y = 281474976710128 
q = 281474976710129

print(CT_Butterfly(A0,A1,Y,q))
B2, B3 = CT_Butterfly(A0,A1,Y,q)

# # test case antara 2 dan 3
# A0 = 58715082317424
# A1 = 83779149426712

# print(CT_Butterfly(A0,A1,Y,q))
    
# test case 3
A0 = 58715082317424
A1 = 32981941352407

A0 = B0
A1 = B1
Y = 78055169708279
q = 281474976710129

print(CT_Butterfly(A0,A1,Y,q))

# # test case antara 3 dan 4
# A0 = 127508142199635
# A1 = 32981941352407

# print(CT_Butterfly(A0,A1,Y,q))
    
# test case 4
A0 = 127508142199635
A1 = 72578270035991

A0 = B2
A1 = B3
Y = 203419807001850
q = 281474976710129

print(CT_Butterfly(A0,A1,Y,q))