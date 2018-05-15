a = input('Enter the size')

def printing(a):
    for x in range(a):
        print ' -- ' * a
        print '|\t' * (a+1)
    print ' -- ' * a

printing(a)
