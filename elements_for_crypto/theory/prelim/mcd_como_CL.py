def mcd_y_cocientes(a, b):
    """INPUTS: 
            a (int), b (int) positivos
        OUTPUTS: tuple (b1 (int), cocientes (list)) 
             b1 = MCD(a,b). cocientes en algoritmo Euclides
            """
    a1 = max(abs(a), abs(b))
    b1 = min(abs(a), abs(b))
    r1 = a1 % b1
    q1 = a1 // b1
    cocientes = [q1]
    if r1 > 0:
        r2 = 1
        while r2 != 0:
            r2 = b1 % r1
            q2 = b1 // r1
            cocientes.append(q2)
            b1 = r1
            r1 = r2
        return b1, cocientes
    else:
        return b1, cocientes
    
def mcd(a,b):
    return mcd_y_cocientes(a,b)[0]

def escalares_para_mcd_como_CL(a,b):
    """
    INPUTS: 
             a (int), b (int)
    OUTPUTS: 
            tuple (x1,y1) floats o escalares 
        tales que  mcd(a,b) = a x1 + b y1
    """
    x0 = 0
    x1 = 1
    y0 = 1
    if a > b:
        cocientes = mcd_y_cocientes(a,b)[1]
    else:
        cocientes = mcd_y_cocientes(b,a)[1]
    y1 = -cocientes[0]
    n = len(cocientes)
    for i in range(1,n-1):
        x2 = x0 - x1 * cocientes[i]
        y2 = y0 - y1 * cocientes[i]
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
    if a > b:
        return x1, y1
    else:
        return y1, x1

def imprimir_mcd_como_CL(a,b):
    print(f"El mcd({a}, {b}) es {mcd(a,b)}")
    x1, y1 = escalares_para_mcd_como_CL(a,b)
    print(f"Dicho valor {mcd(a,b)} resulta de {a} * {x1} + {b} * {y1}")
    return 0

if __name__ == "__main__":
    # a = 2947
    # a = 329
    # b = 3997
    # b = 1005
    a, b = 2947, 3997
     
    print(imprimir_mcd_como_CL(a,b))