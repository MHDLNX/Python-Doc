def double (f):
    f()
    f()

def four (f):
    double(f)
    double(f)

def p1 () : 
    print("+-----",end="");
def p2 () :
    print("|     ",end="");

def p3 () :
    double(p1)
    print("+");

def p4 () : 
    double(p2)
    print("|")

def p5 () : 
    p3()
    four(p4)
    p3()
    four(p4)
    p3()

p5()