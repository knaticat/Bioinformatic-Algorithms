import pprint

def profilemat(entries,k):
    l = entries.split(" ")
    main = [float(i) for i in l]
    m = []
    for i in range(0,len(main),k):
        temp = main[i:i+k]
        m.append(temp)
    base = ['A','C','G','T'] 
    myDict = { k:v for (k,v) in zip(base, m)}  
    
    return myDict
def probable(Text,Profile,k):
    kmer = []
    maxscore = 0
    index = ""
    for i in range((len(Text)-k)+1):
        pat = Text[i:i+k]
        kmer.append(pat)
    #print(kmer)
    freqmatrix = profilemat(Profile,k) 
    #pprint.pprint(freqmatrix)
    for element in kmer:
        score = 1
        for i in range(0,k):
            score *= freqmatrix[element[i]][i]
        #print(f'{score:.20f}')
        if score > maxscore:
            maxscore = score
            index = element
    return index
        
