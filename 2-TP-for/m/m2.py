# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')
        
# Fonction qui valide le TP01-for
def c1(f):
    test=True
    liste1=[round(400*1.016**i,2) for i in range(1,15)]
    liste2=[f(i) for i in range(2020,2034)]
    test=(liste1==liste2)
    affrep(test)
    
# Fonction qui valide le TP02-for
def c2(f):
    test=(f()==1230)
    affrep(test) 
        
# Fonction qui valide le TP03-for
def c3(f):
    liste=[13*i for i in range(0,20)]
    test=(liste==f(20))
    affrep(test)
    
# Fonction qui valide le TP04-for
def c4(f):
    liste=[3**i for i in range(0,10)]
    test=(liste==f())
    affrep(test)
    
# Fonction qui valide le TP05-for
def c5(f):
    test=(f()==26917.37)
    affrep(test)
    
# Fonction qui valide le TP06-for
def c6(f):
    test=(f()==28656.28)
    affrep(test)  