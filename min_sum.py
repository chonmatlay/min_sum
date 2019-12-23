
from common import *

#the minimal sum algorithm 

def min_sum(num) : 
    a = load_testcase(num)
    k=1 
    t= a[0]
    s= a[0]
    while (k!=len(a)) :
        t= min(t + a[k] , a[k])
        s= min(s,t)
        k = k+1
    return s

#write to the output file
def min_sum_write_output() : 
    clear_output(1)
    for x in range(1,11):

        write_output(min_sum(x),1)
