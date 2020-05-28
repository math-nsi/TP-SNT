# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')
        
# Fonction qui valide le TP01-while
def c1(f):
    liste1=[2028,2036,2044,2050]
    liste2=[f(i) for i in range(600,1000,100)]
    test=(liste1==liste2)
    affrep(test)
    
# Fonction qui valide le TP02-while
def c2(f):
    liste1=[2026,2036,2046]
    liste2=[f(i) for i in range(2020,2050,10)]
    test=(liste1==liste2)
    affrep(test)
    
# Fonction qui valide le TP03-while
def c3(f):
    liste1=[-246000,-181000,-126000,-78000,-36000]
    liste2=[f(i) for i in range(50,100,10) ]
    test=(liste1==liste2)
    affrep(test)
    
# Fonction qui valide le TP04-while
def c4(f):
    liste1=[3**i for i in range(0,9)]
    liste2=f()
    test=(liste1==liste2)
    affrep(test)
    
# Fonction qui valide le TP05-while
def c5(f):
    test=(f()==100000)
    affrep(test)
    
# Fonction qui valide le TP05-while
def c6(f):
    test=(f()==5776)
    affrep(test)