# Fonction qui valide le TP1
def ctp1(f):
    test=0
    for i in range(100):
        for j in range(100):
            if i<j and f(i,j)!=i:
                test=1
    if test==0:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')

# Fonction qui valide le TP2
def ctp2(f):
    test=0
    for i in range(1,10):
        if i<8:
            m=11*i+10
        else:
            m=11*i
        if m!=f(i):
            test=1
    if test==0:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')
