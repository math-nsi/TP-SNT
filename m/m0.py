# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')

# Fonction qui valide le TP03
def c3(f):
    test=True
    for i in range(100):
        for j in range(100):
            if f(i,j)!=i-j:
                test=False
    affrep(test)