import random
from Bio.Seq import Seq
#import numpy as np

def ProbableGibbs(Text,Profile,k):
    kmer = []
    randomscore = []
    index = 0
    for i in range((len(Text)-k)+1):
        pat = Text[i:i+k]
        kmer.append(pat)
    freqmatrix = Profile 
    for element in kmer:
        score = 1
        for i in range(0,k):
            score *= freqmatrix[element[i]][i]
        randomscore.append(score)
    C = sum(randomscore)
    newList = [x / C for x in randomscore]
#     maxval = np.random.choice(kmer, p = newList)
#     return maxval
    maxval = max(newList)
    ind = newList.index(maxval)
    pro = kmer[ind]
    return pro
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
def GibbSampler(string,k,t,N):
    dna = makednalist(string)
    n = len(dna[0])
    bestmotifs = [] 
    motifs = []
    for x in dna:
        randvalue = random.randint(0,(n-k))
        motifs.append(x[randvalue:randvalue+k])
    bestmotifs = motifs[:]
    for j in range(0,N):
        i = random.randint(0,t-1)
        temp = motifs[:i] + motifs[i+1:]
        profile = CreateProfileMat(temp,t-1)
        motifs[i] = ProbableGibbs(dna[i],profile,k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs[:]
    return bestmotifs   
def Helper(string,k,t,N):
    last = GibbSampler(string,k,t,N)
    for i in range(0,20):
        best = GibbSampler(string,k,t,N)
        if(score(best)<score(last)):
            last = best
    return last
