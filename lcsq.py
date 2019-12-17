import itertools

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

DNA=FASTA_parse("rosalind_lcsq.txt")
dna=list(DNA.values())
s1=dna[0]
t1=dna[1]

    
def lcsq(s, t):
    Slen, Tlen= len(s), len(t)
    
    if Slen == 0:
        return []
    elif Slen == 1:
        if s[0] in t:
            return [s[0]]
        else:
            return []
    else:
        i = Slen // 2
        Sben, Send = s[:i], s[i:]
        
        longestb = lcsq_length(Sben, t)
        longeste = lcsq_length(Send[::-1], t[::-1])
        _, ff = max((longestb[j] + longeste[Tlen - j], j) for j in range(Tlen + 1))
        
        Tben, Tend = t[:ff], t[ff:]
        
        return lcsq(Sben, Tben) + lcsq(Send, Tend)
    
def lcsq_length(s, t):
    now = list(itertools.repeat(0, 1 + len(t)))
    
    for x in s:
        bef = list(now)
        
        for i, y in enumerate(t):
            if x == y:
                now[i + 1] = bef[i] + 1
            else:
                now[i + 1] = max(now[i], bef[i + 1])
    return now




print (''.join(lcsq(s1, t1)))