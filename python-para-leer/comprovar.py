import keys2
def comprovar(a, b, v): 
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
    return(a[3], a[2])
a = range(30)
a[1] = 200
b = '/home/anon/Escritorio/virtual/btcmail.asc'
v = '/home/anon/Escritorio/virtual/btcmail1.asc'
a = comprovar(a, b, v)
print(a)
a = keys('/home/anon/.gnupg')
a.listkeys()