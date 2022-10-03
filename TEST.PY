def separarComposto2(composto, prof=0, atomo=["", ""], atomos=[], nums="123456789"):
    if prof+1 >= len(composto):
        atomo[1] += composto[prof]
        atomos.append(atomo)
        return atomos

    if composto[prof] in nums:
        atomo[1] += composto[prof]
        if composto[prof+1] not in nums:
            atomos.append(atomo)
            return separarComposto2(composto, prof+1, atomo=["", ""], atomos=atomos)
        return separarComposto2(composto, prof+1, atomo=atomo, atomos=atomos)
    else:
        atomo[0] += composto[prof]
        return separarComposto2(composto, prof+1, atomo=atomo, atomos=atomos)

def gerarMatriz(r, p):
    P = []
    R = []

    for i in p:
        P.append(separarComposto2(i, atomo=["", ""], atomos=[]))
    for i in r:
        R.append(separarComposto2(i, atomo=["", ""], atomos=[]))

    eq = [R, P]

    return eq
    

r = ["O2", "H2"]
p = ["H2O1"]



eq = gerarMatriz(r, p)

print(eq)
