def write_output(out,mod): 
    if (mod) :
        path = "output/min_sum"
    else :
        path = "output/brute_force"
    f= open(path,"a")
    f.write(str(out))
    f.write(' ')
    f.close()

def clear_output(mod):
    if (mod) :
        path = "output/min_sum"
    else :
        path = "output/brute_force"
    f = open(path,"w")
    f.write('')
    f.close()
def load_testcase(num):
    path = "testcase/" +str(num)
    f= open(path,"r")
    a=f.read()
    a=a.split()
    for x in range(0,len(a)) : 
        a[x] = int(a[x])
    return a
def compare() : 
    wrong =0
    print("compare :")
    f1 = open("output/brute_force")
    f2 = open("output/min_sum")
    bf = f1.read().split(' ')
    ms = f2.read().split(' ')
    bf= bf[0:len(bf)-1]
    ms = ms[0:len(ms)-1]
    if (len(bf)!=len(ms)) :
        print("output err!! ")
        return 
    for i in range(0,len(bf)) :
        if (bf[i].lstrip('-').isdigit() and ms[i].lstrip('-').isdigit()) :
            if (int(bf[i])!=int(ms[i])) :
                print("wrong aswer at case :",i)
                wrong=1
    if(wrong == 0) :
        print("success!!")    
    f1.close()
    f2.close()
