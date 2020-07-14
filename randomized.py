import random
from Bio.Seq import Seq

def probable(Text,Profile,k):
    kmer = []
    maxscore = 0
    index = ""
    for i in range((len(Text)-k)+1):
        pat = Text[i:i+k]
        kmer.append(pat)
    freqmatrix = Profile 
    for element in kmer:
        score = 1
        for i in range(0,k):
            score *= freqmatrix[element[i]][i]
        if score > maxscore:
            maxscore = score
            index = element
    return index
def makednalist(string):
    l = string.split("\n")
    return l[1:-1]
def CreateProfileMat(arr,t):
    n = len(arr[0])
    profilemat = {base:[1]*n for base in "ACGT"}
    
    for dna in arr:
        for index,base in enumerate(dna):
            profilemat[base][index]+= 1/t
    return profilemat
def FindConsensus(arr):
    n= len(arr[0])
    freq_matrix = {base: [0]*n for base in 'ACGT'}

    for dna in arr:
        for index,base in enumerate(dna):
            freq_matrix[base][index]+=1
    consensus = ''
    for i in range(n):
        max_freq = -1
        max_freq_base = None
        
        for base in 'ACGT':
            if freq_matrix[base][i] > max_freq:
                max_freq = freq_matrix[base][i]
                max_freq_base = base
        consensus+= max_freq_base
    return consensus
def hamming_distance(s,t):
    counter=0
    first_seq = Seq(s)
    second_seq = Seq(t)
    
    for i in range(len(first_seq)):
        if first_seq[i]!= second_seq[i]:
            counter+=1
        else: continue
    return counter
def score(motifs):
    consensus = FindConsensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(consensus, motif)
    return score
def Motifs(Profile,dna,k):
    mot = []
    for text in dna:
        value = probable(text,Profile,k)
        mot.append(value)      
    return mot
def RandomizedMotifSearch(string,k,t):
    dna = makednalist(string)
    n = len(dna[0])
    bestmotifs = [] 
    motifs = []
    for x in dna:
        randvalue = random.randint(0,(n-k))
        motifs.append(x[randvalue:randvalue+k])
    bestmotifs = motifs
    while True:
        profile = CreateProfileMat(motifs,t)
        motifs = Motifs(profile,dna,k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else :
            return bestmotifs  
def Helper(string,k,t):
    random.seed(0)
    last = RandomizedMotifSearch(string,k,t)
    for i in range(0,1000):
        best = RandomizedMotifSearch(string,k,t)
        if(score(best)<score(last)):
            last = best
    return last
