def sseq(s):
    indices = []
    s=val[0]
    t=val[1]
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            indices.append(i + 1)
            j += 1
        i += 1

    return indices

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

strands=FASTA_parse("rosalind_sseq.txt")
val= list(strands.values())

print(*sseq(strands))