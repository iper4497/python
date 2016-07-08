def lib(a, b, v): 
    b = open(b, 'r')
    v = open(v, 'r') 
    a[3] = -1
    for a[2] in range(a[1]):
        if b.readline() == v.readline():
            a[3] = a[3] + 1
    v.close()
    b.close()
    if a[3] == a[2]:
        a[3] = True
    print(a[3], a[2])
class comprovar(object):
    
    def __init__(self, b, v):
        a = range(30)
        a[1] = 200
        #b = 'archivo2'
        # v = 'archivo1'
        a = lib(a, b, v)
        return(a)
comprovar('usarcomprovar.py', 'usarcomprovar.py')