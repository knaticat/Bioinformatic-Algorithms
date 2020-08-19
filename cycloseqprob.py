from collections import Counter

def integermass():
    a= 'G A S P V T C I L N D K Q E M H F R Y W'
    m = '57 71 87 97 99 101 103 113 113 114 115 128 128 129 131 137 147 156 163 186'
    al = a.split()
    ml = m.split()
    di = {k: int(v) for k, v in zip(al, ml)} 
    return di,al,ml
def cyclospectrum(peptide,intmass):
    prefixmass = [0]
    amino = list(intmass.keys())
    for i in range(len(peptide)):
        for j in range(20):
            if amino[j] == peptide[i]:
                prefix = prefixmass[i] + intmass[amino[j]]
                prefixmass.append(prefix)
    peptidemass = prefixmass[len(peptide)]
    cyclo = [0]
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            diff = prefixmass[j] - prefixmass[i]
            cyclo.append(diff)
            if i > 0 and j < len(peptide):
                left = peptidemass - (prefixmass[j] - prefixmass[i])
                cyclo.append(left)
    cyclo.sort()
    return cyclo
def makespectrum(string):
    sp = string.split()
    return sp
def expand(peptides,m):
    new = set()
    for x in peptides:
        for mass in m:
            if x != "":
                new.add(x+'-'+mass)
            else:
                new.add(mass)                
    return new
def mass(peptide):
    mass = 0
    m = peptide.split("-")
    for i in m:
        mass = mass + int(i)
    return mass
def temp():
    a= 'G A S P V T C L N D Q E M H F R Y W'
    m = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
    al = a.split()
    ml = m.split()
    di = {v: k for k, v in zip(al, ml)} 
    return di
def parentmass(spectrum):
    return spectrum[-1]
def makeamino(peptide):
    di = temp()
    new = ""
    v = peptide.split("-")
    for i in v:
        new = new + di[i]
    return new
def theoreticalspectrum(peptide,intmass):
    prefixmass = [0]
    amino = list(intmass.keys())
    for i in range(len(peptide)):
        for j in range(20):
            if amino[j] == peptide[i]:
                prefix = prefixmass[i] + intmass[amino[j]]
                prefixmass.append(prefix)
    linear = [0]
    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1):
            diff = prefixmass[j] - prefixmass[i]
            linear.append(diff)
    linear.sort()
    return linear
def checkconsistent(peptide,spectrum,intmass):
    li = theoreticalspectrum(peptide,intmass)
    short_counts = Counter(li)
    large_counts = Counter(spectrum)
    return all(value <= large_counts.get(key, 0) for key, value in short_counts.items())
def cyclopeptidesequencing(spectrum,intmass,ma):
    peptides = set()
    peptides.add("")
    while len(peptides) > 0:
        peptides = expand(peptides,ma)
        for pep in peptides.copy():
            newpep = makeamino(pep)
            if mass(pep) == parentmass(spectrum):
                if cyclospectrum(newpep,intmass) == spectrum:
                    print(pep,end=" ")
                peptides.remove(pep)
            elif mass(pep) != parentmass(spectrum):
                if checkconsistent(newpep,spectrum,intmass) == False:
                        peptides.remove(pep)
if __name__ == "__main__":
    spec  = makespectrum('0 113 128 186 241 299 314 427')
    spectrum = [int(i) for i in spec]
    di,_,m = integermass()
    cyclopeptidesequencing(spectrum,di,m)
    
