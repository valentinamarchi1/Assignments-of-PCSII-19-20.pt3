def Distance(s1,s2):
    if len(s1)== len(s2):
        dis = 0.0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1    
                
    return '%.5f'%(dis/len(s1))



def FASTA_parse(file):
    strings={}
    with open(file) as f:
        text=f.read()
        items=text.split('>')
        
    for item in items[1:]:
        item=item.split('\n')
        string_id=item.pop(0)
        strings[string_id]=''.join(item)
        
    return strings

dic=FASTA_parse("rosalind_pdst.txt")
DNAs=dic.values()

counter=[]
for strand1 in DNAs:
        for strand2 in DNAs:
            counter.append(Distance(strand1,strand2))

for i in range(0,len(counter),len(DNAs)):
    print (' '.join(map(str, counter[i:i+len(DNAs)])))

