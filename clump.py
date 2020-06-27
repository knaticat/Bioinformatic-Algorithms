import numpy as np

def LastSymbol(Pattern):
    return Pattern[-1]
def Prefix(Pattern):
    return Pattern[:-1]
def SymbolToNumber(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    elif symbol == "T":
        return 3
def NumberToSymbol(index):
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
def PatternToNumber(Pattern):
    if Pattern is '':
        return 0
    symbol =  LastSymbol(Pattern);
    prefix = Prefix(Pattern);
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol);
def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index);
    prefixindex = index // 4
    r = index % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixindex, k-1)
    return PrefixPattern + symbol
def ComputeFrequencies(Text,k):
    freqarr = np.zeros(4**k)
    l = len(Text)
    
    for j in range(0,(l-k)+1):
        Pattern = Text[j:j+k]
        val = PatternToNumber(Pattern)
        freqarr[val] += 1
    return freqarr
def BetterClumpFinding(Genome,k,L,t):
    FreqPattern = set()
    clump = np.zeros(4**k)
    l = len(Genome)
    Text = Genome[0:L]

    FreqArr = ComputeFrequencies(Text,k)
    for i in range(0,4**k):
        if FreqArr[i] >= t:
            clump[i] = 1
    for i in range(1, (l-L)+1):
        first = Genome[i-1: i-1 + k]
        index = PatternToNumber(first)
        FreqArr[index] -= 1
    
        last = Genome[(i+L-k) : (i+L-k)+k]
        index = PatternToNumber(last)
        FreqArr[index] += 1
        if FreqArr[index] >= t:
            clump[index] = 1
    for i in range(0,4**k):
        if clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FreqPattern.add(Pattern)
    return FreqPattern
        
        
