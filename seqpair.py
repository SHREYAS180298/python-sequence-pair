import numpy as np

n=int(input("Enter the number of modules:\n"))
##print("Enter the width and height of each module in WxH format in order:\n")
##for i in range(1,n+1):
##    print("Module :",i)
##    a,b=input().split('x')
##    w.append(a)
##    h.append(b)
w_h=[[]*2]*n
w=[]
h=[]
right=[]
left=[]
above=[]
below=[]


def common(list_o,list1,list2):
    for elem in list1:
        if elem in list2:
            list_o.append(elem)
    list_o.sort()
    #print(list_o)
    

def divide_chunks(o,l):
    for i in range(len(l)-1):
        o=[]
        for j in range(0,5):
            o[j]=l[i+j]
            
  


j=input("Enter the positive sequence :\n")
pos_seq=[int(j) for j in str(j)]
print(pos_seq)
m=input("Enter the negative sequence :\n")
neg_seq=[int(d) for d in str(m)]
print(neg_seq)
mat=[]
print("-----------------------------------------------------------------------------------------------------------------------------------\n")
print("Module      right                         left                               above                              below          \n")
print("-----------------------------------------------------------------------------------------------------------------------------------\n")
for el in pos_seq:
    if el in neg_seq:
        right=[[]]
        left=[[]]
        above=[[]]
        below=[[]]
        ind_el_p=pos_seq.index(el)
        #print("indes of %d is %d",el,ind_el_p)
        ind_el_n=neg_seq.index(el)
        #print("index of %d is %d",el,ind_el_n)
        i=0
        if((ind_el_n)+1 < n and (ind_el_p)+1 < n):
            l1=pos_seq[ind_el_p+1:n]
            l2=neg_seq[ind_el_p+1:n]
            common(right[i],l1,l2)
        #print(right[i])

        
        if(ind_el_n > 0  and ind_el_p > 0):
            l3=pos_seq[0:ind_el_p]
            l4=neg_seq[0:ind_el_n]
            common(left[i],l3,l4)
        #print(left[i])


        if(ind_el_n+1 < n  and ind_el_p > 0):
            l7=pos_seq[0:ind_el_p]
            l8=neg_seq[ind_el_n+1:n]
            common(above[i],l7,l8) 
        #print(above[i])

        
        if(ind_el_n > 0  and ind_el_p+1 < n):
            l5=pos_seq[ind_el_p+1:n]
            l6=neg_seq[0:ind_el_n]
            common(below[i],l5,l6)
        #print(below[i])
        right[i].extend([0]*(n - len(right[i])))
        left[i].extend([0]*(n - len(left[i])))
        above[i].extend([0]*(n - len(above[i])))
        below[i].extend([0]*(n - len(below[i])))
        print(el,"      ",right[i],"        ",left[i],"         ",above[i],"        ",below[i],"  \n");
        
        mat.append(el)
        mat.append(right[i])
        mat.append(left[i])
        mat.append(above[i])
        mat.append(below[i])

        i=i+1
#print (mat)
print ("len=",len(mat))
res = [] 
subl = [] 
cnt = 0
for sub in mat: 
    subl.append(sub) 
    cnt = cnt + 1
    if cnt >= 5: 
        res.append(subl) 
        subl = [] 
        cnt = 0
#print(res)
cmp_lst=[0,0,0,0,0,0,0,0]
def fix_corner(lst):
    for row in lst:
        #print("row=\n")
        #print(row)
        if(row[1]==cmp_lst):
            rightmost=row[0]
            print("Right most=",rightmost)
        if(row[2]==cmp_lst):
            leftmost=row[0]
            print("lef most=",leftmost)
        if(row[3]==cmp_lst):
            topmost=row[0]
            print("Top most=",topmost)
        if(row[4]==cmp_lst):
            btmmost=row[0]
            print("Botom most=",btmmost)
        
        #for elmn in row:
            #if elmn
            
            
        
fix_corner(res)
    
    

            
