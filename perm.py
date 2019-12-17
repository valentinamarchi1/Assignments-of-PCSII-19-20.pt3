from itertools import permutations

def perm(n):
    totp=0
    l=list(permutations(range(1,n+1)))
    l2=[]
    string=''
    for i in l:
        totp+=l.count(i)
    l2.append(str(totp))
    for i in l:
        for k in i:
            string+=str(k)
        l2.append(string)
        string=''
    return l2


with open('rosalind_perm_out.txt', 'w') as f:
    arr=perm(5)
    f.write(arr[0] + '\n')
    del arr[0]
    for k in arr:
        k=' '.join(k)
        f.write(k + '\n')