# 01-11-24
print('  |   0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

for i in range(0, 13):
    print(str(i).rjust(2), end='')
    print('|', end='')
    for j in range(0, 13):
       print(str(i * j).rjust(4), end='')
    print()
    
