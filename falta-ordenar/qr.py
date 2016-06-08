import commands
def cam():
    a = commands.getoutput('zbarcam')
    return a
a = cam()
print('Esta es tu password ', a)