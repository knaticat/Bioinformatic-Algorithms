from Bio.Seq import Seq

def probable(Text,Profile,k):
    kmer = []
    maxscore = 0
    index = ""
    ind = set()
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
    profilemat = {base:[0]*n for base in "ACGT"}
    
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
def GreedyMotifSearch(string,k,t):
    dna = makednalist(string)
    bestmotifs = [] 
    for x in dna:
        bestmotifs.append(x[0:k])
    for i in range(0,(len(dna[0])-k +1)):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1,t):
            profile = CreateProfileMat(motifs[0:j],t)
            val = probable(dna[j],profile,k)
            if val == '':
                motifs.append(dna[j][0:k])
            else : motifs.append(val)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs
            
