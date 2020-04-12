# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')


# Fonction qui valide le TP2
def ctp2(f):
    test=True
    for i in range(100):
        for j in range(100):
            if i<j and f(i,j)!=i:
                test=False
    affrep(test)

# Fonction qui valide le TP3
def ctp3(f):
    test=True
    for i in range(1,10):
        if i<8:
            m=11*i+10
        else:
            m=11*i
        if m!=f(i):
            test=False
    affrep(test)
        
# Fonction qui valide le TP4
def ctp4(f):
    test=True
    for i in range(1,300):
        if i<=80:
            m=i
        else: 
            if i<150 :
                m=0.94*i
            else:
                m=0.85*i
        if m!=f(i):
            test=False
    affrep(test)
