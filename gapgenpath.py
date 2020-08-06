def paired_tuple(string,k):
    l = string.split("\n")
    li = l[1:-1]
    new = []
    for i in li:
        new.append((i[0:k],i[k+1:2*k+1]))
    return new
def LastSymbol(Pattern):
    return Pattern[-1]
def GenomePath(dna):
    text = dna[0]
    for pat in dna[1:]:
        k = LastSymbol(pat)
        text += k
    return text
def StringSpelledByGappedPatterns(GappedPatterns,k,d):
    first = []
    second = []
    for x in GappedPatterns:
        first.append(x[0])
        second.append(x[1])
    pre = GenomePath(first)
    suf = GenomePath(second)
    for i in range(k+d+1,len(pre)):
        if pre[i] != suf[i-k-d]:
            return "No string"
    return pre + suf[-(k+d):]
            
if __name__ == "__main__":
    GappedPatterns = paired_tuple("""
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA
""",4)
    v = StringSpelledByGappedPatterns(GappedPatterns,4,2)
    print(v)
