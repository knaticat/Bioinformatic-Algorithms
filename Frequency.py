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
def FasterFreqWords(Text,k):
    freqpat = set()
    freqarr = ComputeFrequencies(Text,k)
    maxcount = max(freqarr)
    for i in range(0,4**k):
        if freqarr[i] == maxcount:
            pattern = NumberToPattern(i,k)
            freqpat.add(pattern)
    return freqpat
def FindingFreqWordsBySort(Text,k):
    freqpat = set()
    l = len(Text)
    index = np.zeros((l-k)+1)
    count = np.zeros((l-k)+1)
   
    for i in range(0,(l-k)+1):
        Pattern = Text[i:i+k]
        index[i]= PatternToNumber(Pattern)
        count[i]=1
    sortedindex = np.sort(index)
    for j in range(1,(l-k)+1):
        if sortedindex[j] == sortedindex[j-1]:
            count[j]= count[j-1] + 1
    maxcount = max(count)
    for m in range(0,(l-k)+1):
        if count[m]== maxcount:
            pat  = NumberToPattern(sortedindex[m],k)
            freqpat.add(pat)
    return freqpat
        
