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

DNA=FASTA_parse("rosalind_grph.txt")

def grph(lst):
    key_list = list(DNA.keys()) 
    val_list = list(DNA.values()) 
    result = ""
    for i in val_list:
        for j in val_list:
            if i[-3:]==j[:3] and i!=j:
                result+=key_list[val_list.index(i)]+' '
                result+=key_list[val_list.index(j)]+'\n'
    return result

with open('rosalind_grph_out.txt', 'w') as f:
    f.write(grph(DNA))