def f(*args, **kwargs):
     print('Named: ', kwargs)
     
f(galleons = 100, sickles = 50, knuts = 25)

# def f(*args, **kwargs):
#     print('Positional: ', args)
    
# f(100, 50, 25)

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), 'knuts')
# * is to pass all value individual to the function (dict should use ** instead)
# *=args, **=kwargs
'''