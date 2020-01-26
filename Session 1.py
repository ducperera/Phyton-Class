def trouble(a_smiles, b_smiles):
    if a_smiles == True and b_smiles == True:
        return True
    elif a_smiles == False and b_smiles == False:
        return True
    else:
        return False
def int_sum(a,b):
    if a==b:
        return (a+b)*2
    else:
        return (a+b)
def hours(h):
    hours_arr = []
    for i in range(h+1,24,1):
        hours_arr.append(i)
    return hours_arr
def hour_1(h):
    return list(range(h+1,24))


def top(a,b,negitive):
    if negitive:
        return (a<0) and (b<0)
    else:
        return (a>0 and b<0) or (a<0 and b>0)
def front_back(s):
    if len(s) == 1 :
        return s
    else:
        mid = s[1:-1]
        f = s[0]
        b = s[-1]
        return(b+mid+f)

def out(s,num=3):
    if len(s) >= 3 :
        new_s = s[0:3]*num
        return(new_s)

def rep_last_2(s,num=4):
    if len(s) >= 2:
        new_s = s[-2:]*num
        return(new_s)

def zero_list(g_list):
    new_list = []
    g_list_len = len(g_list)
    new_list_len = g_list_len * 2
    last_el = g_list[-1]

    for new_el in range (new_list_len):
        new_list.append(0)
    new_list[-1] = last_el
    return new_list

def zero_list_3(g_1):
    new_list = [0]* len(g_1)*2
    new_list[-1] = g_1[-1]
    return new_list

def list_count_9(g_list):
    count = 0

    for i in g_list:
        if i == 9:
            count = 1 + count
        else:
            count = 0 + count
    return count


if __name__ == '__main__':
    #Problem 2
    #val = trouble(True, False)
    #print(val)
    #Problem 3
    #val3 = int_sum(4,4)
    #print(val3)
    #problem 4
    #val4= hours(6)
    #print(val4)
    #val5=top(2,3,False)
    #print(val5)
    #print(front_back("Udara"))
    #print(out("udara",8))\
    #print(rep_last_2("Java",2))
    #print(zero_list([1, 0,2]))
    #print(zero_list_3([1,0,2]))
    print(list_count_9([1,3,9,9]))

f=lambda a: a*a
print(f(12))
h=lambda x,y: x*x +y
print(h(3,1))