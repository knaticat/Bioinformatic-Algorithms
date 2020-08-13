def integermass():
    a= 'G A S P V T C I L N D K Q E M H F R Y W'
    m = '57 71 87 97 99 101 103 113 113 114 115 128 128 129 131 137 147 156 163 186'
    al = a.split()
    ml = m.split()
    di = {k: int(v) for k, v in zip(al, ml)} 
    return di
intmass = integermass()
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
if __name__ == "__main__":
    v = cyclospectrum("ANKQLFLAFYSMMG",intmass)
    for x in v:
        print(x,end=" ")
