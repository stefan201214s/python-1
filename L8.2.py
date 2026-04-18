def bitwiseOp():
    print(bin(14)) #1110
    print(bin(6)) #110
    print((14&6)) # bits that are in 14 and 6 too
    print(bin(14&6)) 
    print((14|6)) # bits that are in 14 or 6 both
    print(bin(14|6)) 
    print((14^6)) # bits that are in 14 or 6 but not both
    print(bin(14^6)) 
    print((~14)) # -(1110+1) = -1110 = -15


    print((14 >> 2)) # shift 14 right by 2: 1110 -> 11 = 3
    print(bin(14 >> 2)) 
    print((14 << 2)) # shift 14 left by 2: 1110 -> 111000 = 56
    print(bin(14 << 2)) 
    
