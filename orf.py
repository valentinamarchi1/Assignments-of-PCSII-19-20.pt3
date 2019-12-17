rna_codons = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
 "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
 "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
 "UUG": "L","CUG": "L", "AUG": "M", "GUG": "V",
 "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
 "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
 "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
 "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
 "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
 "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
 "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
 "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
 "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
 "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
 "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
 "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

def trans(strand):
    for i in strand:
        return strand.replace('T','U')
    
def rev(dna):
    rnareverse=''
    for i in range(len(dna)):
        ind=len(dna)-1-i
        if dna[ind]=="T":
            dna[ind]=="U"
            rnareverse+="A"
        else:
            if dna[ind] == "A":
                rnareverse+="U"
            else:
                if dna[ind]=="C":
                    rnareverse+="G"
                else:
                    rnareverse+="C"
    return rnareverse
    
def prot(strand):
    result=[]
    for i in range(len(strand)-2):
        if strand[i:i+3]=='AUG':
            j=i
            aminoseq = ""
            let='AUG'
            while rna_codons[let]!= "STOP":
                aminoseq+=rna_codons[let]
                j+=3
                if j>len(strand)-3:
                    break
                let=strand[j:j+3]
            if rna_codons[let]=="STOP" and aminoseq not in result:
                result.append(aminoseq)

    return result


DNA = "GCATGTCTACTAAAATTTGTGTAAGCGGTACCCGGAGCCTTTGTGGACACCACAATGTAAAAGTATTTTTAAATGGGAAGACCATGCTGATAGACGACGTAGTTCGCCTGTGGACGTCTGTGAAAACGGTAAGGTAGCGCCGATTATGCTATCATCCGCGTATCTGTAGACCACGGCATGGGATGAATCAGCCGAGGATACGAGTAACCTGCGAACTATTGTTACGCCTTCGACAGGTTGCCGCAAATAATTGCATGCGACACATTCGCATTCAAACGTAGAATACACCAAGCACATCCTTCGAGTTCCTTCCACTCTCAACTCTCATGATCTAGTTTGGAATATAAAACCCTGCCCTGTCGGACCCATTAAGTGCCCCTGACCCCTGTAGTTCGCGTGATGACCTCAATATCTAGGCTAGAAGGTAATTCGCATCTAAGGGTCGGCATGTAAGACTCTATGTGTAGACCTCATTTTAACTAATAGCTATTAGTTAAAATGAGGTCTACACATCCAAACAGACCCATGCCTTCCTCAGAAGCTAGCCTCATAAACGGCAAGCCACTCATGGCTGTCCACACGGTGGTGCGTGTAGTCAATATTCGACATATTCAACATAATACCACCAATTTATTGCGTCAATGAAGGGGCTCATCGAAATGCCGTTCAGGAGGATGCAAGCCACCAAAAGTTCAACATTGAAGGTACAACGACCCATATCAGGCCTGACTAAGATCGAATCGACCACAGAAGGCACTTTGCAAACGACTGTTGACTCCCAAGTACCGTGATGGCCTTCGTCCAACCATGAGAGGCGTAGCGCGCGGTGGGTCTGCATGATTCCTTTCCGGTCGATGACTAACAAAGAATCTGGTTGACGATAGGTAAGATATGTCGAGGATATCGGGTTGGCACTATCTGACAGCTGAAACTTTCCCTCTAGTGGTATTAGGTGAGATCAGAGCACATAAG"
rna= trans(DNA)
revstrand= rev(DNA)
res=[]
nor=prot(rna)
reve= prot(revstrand)

def final(res1,res2):
    for i in res1:
        res.append(i)
        for j in res2:
            if j not in res:
                res.append(j)
    return res

f= final(nor,reve)
with open ("result.txt", "w") as l:
    for i in f:
        l.write(i)
        







