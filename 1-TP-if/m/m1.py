# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')     
        
# Fonction qui valide le TP01-if
def c1(f):
    test=True
    for i in range(100):
        for j in range(100):
            if i<j and f(i,j)!=i:
                test=False
    affrep(test)
    
# Fonction qui valide le TP02-if
def c2(f):
    test=True
    for i in range(1,10):
        if f(i) or f(-i)==False:
            test=False
    affrep(test)
    
# Fonction qui valide le TP03-if
def c3(f):
    test=True
    for i in range(50,110):
        if i<80:
            m=i
        else:
            m=0.93*i
        if m!=f(i):
            test=False
    affrep(test)
    
# Fonction qui valide le TP04-if
def c4(f):
    test=True
    for i in range(1,30):
        if 11*i<60:
            m=11*i+8
        else:
            m=11*i
        if m!=f(i):
            test=False
    affrep(test)
    
# Fonction qui valide le TP05-if
def c5(f):
    test=True
    for i in range(40,100):
        if i<70:
            m=0.75*i
        else:
            m=0.55*i
        if m!=f(i):
            test=False
    affrep(test)
    
# Fonction qui valide le TP06-if
def c6(f):
    test=True
    for i in range(1500,1700):
        if i<1600:
            m=1.06*i
        else:
            m=1.04*i
        if m!=f(i):
            test=False
    affrep(test)
    
# Fonction qui valide le TP07-if
def c7(f):
    if [f(1200),f(1500),f(1800),f(2000)]==[108.0,135.0,198.0,220.0]:
        test=True
    else:
        test=False
    affrep(test)    
    


