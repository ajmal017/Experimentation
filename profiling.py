__author__ = 'Amit Rappel'

import math
import cProfile, pstats, StringIO
import pstats

def my_manipulation(x):
    pr = cProfile.Profile()
    pr.enable()
    temp = math.exp(-x) / (1+math.exp(x))
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()
    return temp

def my_sum(max_number):
    total = 0

    for i in range(max_number):
        total += my_manipulation(math.sin(i))

    return total

def my_sum1(max_number):
    total = my_sum(max_number)
    '''
    total = 0
    for i in range(max_number):
        x = math.sin(i)
        y = math.exp(x)
        total += 1 / (y*(1+y))
    '''
    return total

def main():
    print my_sum1(10**1)

'''
pr = cProfile.Profile()
pr.enable()
main()
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
'''
#cProfile.run('main()')

main()
