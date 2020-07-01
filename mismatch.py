import numpy as np
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
def LastSymbol(Pattern):
    return Pattern[-1]
def FirstSymbol(Pattern):
    return Pattern[0]
def Prefix(Pattern):
    return Pattern[:-1]
def Suffix(Pattern):
    return Pattern[1:]
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
def Neighbors(Pattern,d):
    if d == 0:
        return {Pattern}
    elif len(Pattern) == 1:
        return {'A','C','G','T'}
    mate = set()
    suf = Neighbors(Suffix(Pattern),d)
    for Text in suf:
        if hamming_distance(Suffix(Pattern),Text) < d:
            for x in {'A','C','G','T'}:
                mate.add(x+Text)
        else:
            mate.add(FirstSymbol(Pattern)+Text)
    return mate
    
def ApproxPatternCount(Text, Pattern, d):
    count = 0
    for i in range(0,len(Text)-len(Pattern)+1):
        Pattern0 = Text[i:i+len(Pattern)]
        if hamming_distance(Pattern,Pattern0) <= d:
            count+=1
    return count
def FreqWordMismatch(Text,k,d):
    FreqPat = set()
    close = np.zeros(4**k)
    FreqArr = np.zeros(4**k)
    for i in range(0,(len(Text)-k)+1):
        nebhood = Neighbors(Text[i:i+k],d)
        for Pattern in nebhood:
            index = PatternToNumber(Pattern)
            close[index]=1
    for i in range(0,4**k):
        if close[i] == 1:
            pat = NumberToPattern(i,k)
            FreqArr[i] = ApproxPatternCount(Text,pat,d)
    maxCount = max(FreqArr)
    for i in range(0,4**k):
        if FreqArr[i] == maxCount:
            Pattern = NumberToPattern(i,k)
            FreqPat.add(Pattern)
    return FreqPat
            
