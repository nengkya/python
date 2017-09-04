import os, scipy, sys

os.system('tput reset')

bookrate = { 'amy' : {'snow' : 5, 'girl' : 5} }
bookrate['bill'] =   {'snow' : 2, 'girl' : 5}
bookrate['jim' ] =   {'snow' : 1, 'girl' : 4}

MsX =                {'snow' : 4, 'girl' : 2}

print('                    y          x')
print('-------------------------------------')
print('Book rate Amy ',  bookrate['amy' ])
print('Book rate Bill',  bookrate['bill'])
print('Book rate Jim ',  bookrate['jim' ])
print('Book rate MsX ',  MsX)
print()

print('Manhattan distance Amy to MsX :')
print('                    y          x')
print('-------------------------------------')
print('Book rate Amy ',  bookrate['amy' ])
print('Book rate MsX ',  MsX)
print()

print('Rumus manhattan distance = |x1 - x2| + |y1 - y2|')
print('')
print('Manhattan dist = |',  bookrate['amy']['snow'], '-', MsX['snow'], '| + |', bookrate['amy']['girl'], '-', MsX['girl'], '|')
print('               ='  ,  bookrate['amy']['snow'] - MsX['snow'], '+', bookrate['amy']['girl'] - MsX['girl'])
print('               ='  , (bookrate['amy']['girl'] - MsX['girl']) + (bookrate['amy']['snow'] - MsX['snow']) )
print()

def distX(name):
    x1 = bookrate[name]['girl']
    x2 = MsX['girl']
    y1 = bookrate[name]['snow']
    y2 = MsX['snow']
    print('         y          x')
    print('--------------------------')
    if name == 'amy':
        print(name, bookrate['amy'])
        print('MsX', MsX)
        print( 'manhattan dist for', name, '---> MsX =', ((x1 - x2) + abs((y2 - y1))) )
    elif name == 'bill':
        print(name, bookrate['bill'])
        print('MsX ', MsX)
        print( 'manhattan dist for', name, '--> MsX =' , ((x1 - x2) + abs((y2 - y1))) )
    elif name == 'jim':
        print(name, bookrate['jim'])
        print('MsX', MsX)
        print( 'manhattan dist for', name, '---> MsX =', ((x1 - x2) + abs((y2 - y1))) )
    print()

distX('amy')
distX('bill')
distX('jim')
