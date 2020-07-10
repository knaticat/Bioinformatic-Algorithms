from Bio.Seq import Seq

def hamming_distance(s,t):
    counter=0
    first_seq = Seq(s)
    second_seq = Seq(t)
    
    for i in range(len(first_seq)):
        if first_seq[i]!= second_seq[i]:
            counter+=1
        else: continue
    return counter
def NumberToSymbol(index):
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index);
    prefixindex = index // 4
    r = index % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixindex, k-1)
    return PrefixPattern + symbol
def makednalist(string):
    l = string.split("\n")
    return l[1:-1]
def DistaStringPat(Pattern,dna):
    k = len(Pattern)
    distance = 0
    for text in dna:
        ham = float('inf')
        for i in range(0,(len(text)-k)+1):
            pat = text[i:i+k]
            if ham > hamming_distance(Pattern,pat):
                ham = hamming_distance(Pattern,pat)
        distance = distance + ham
    return distance
def MedianString(string,k):
    dna = makednalist(string)
    distance = float('inf')
    for i in range(0,4**k):
        Pat  = NumberToPattern(i,k)
        if distance > DistaStringPat(Pat,dna):
            distance = DistaStringPat(Pat,dna)
            Median = Pat
    return Median
