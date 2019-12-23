from common import *

#by listing all the section, then traverse that list to compute the correct result 
#to compare with the result of the algorithm

def brute_force(num): 
    a = load_testcase(num)
    s=a[0]
    for i in range(0,len(a)) : 
        for j in range(i,len(a)):
            b = a[i:j+1]
            if (s>sum(b)) :
                s=sum(b)
    return s
#write to the output
def brute_force_write_output():
    clear_output(0)
    for x in range(1,11):
        write_output(brute_force(x),0)
           
