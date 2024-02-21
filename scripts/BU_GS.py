# Gentleman-Sandle Butterfly Structure
# A0,A1: input coefficients
# W: twiddle factor
# q: modulus
# B0,B1: output coefficients
def GS_Butterfly(A0,A1,W,q):
    """
    A0 --\--|+|------- B0
          \/
          /\
    A1 --/--|-|--|x|-- B1
    """
    M0 = (A0 + A1) % q
    M1 = (A0 - A1) % q

    B0 = M0
    B1 = (M1 * W) % q

    return B0,B1

# test case 1
A0 = 130455573527732
A1 = 121359353590460
Y = 78055169708279     # w = 281474976710128
q = 281474976710129
mu = 2251799813689464

print(GS_Butterfly(A0,A1,Y,q))

    
# test case 2
A0 = 61653229515297
A1 = 83779149426712

print(GS_Butterfly(A0,A1,Y,q))

    
# test case 3
A0 = 58715082317424
A1 = 32981941352407

print(GS_Butterfly(A0,A1,Y,q))

    
# test case 4
A0 = 127508142199635
A1 = 72578270035991

print(GS_Butterfly(A0,A1,Y,q))