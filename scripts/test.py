def testtrim(ref,allele):
    i = 0
    while ref[i] == "-":
        i = i + 1
    ref = ref[i:]
    allele = allele[i:]
    i = len(allele)-1
    while ref[i] == "-":
        i = i-1
    ref = ref[:i+1]
    allele = allele[:i+1]
    print "after trimming"
    print ref, allele
    # remove extra 10 flanking added to ref
    numrev = 0
    i = 0
    while numrev < 10:
        if ref[i] != "-":
            numrev = numrev + 1
        i = i+1
    ref = ref[i:]
    allele = allele[i:]
    i = len(ref)-1
    numrev = 0
    while numrev < 10:
        if ref[i] != "-":
            numrev = numrev + 1
        i = i-1
    ref = ref[:i]
    allele = allele[:i]
    print ref,allele

testtrim("-CCTACTGTCTATCCAACCATCCATCCATCCATCCATCCATCCATCCATCCA--------CTCTTCCATG-------------------------------","TCCTACTCTCTATCCAACCATCCATCCATCCATCCATCCATCCATCCATCCATCCATCCACTCTTCCATGTATCCACCCAATTACCAATCAGTCTTTCCAA")