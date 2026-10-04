Nucleotides  = ["A","C","T","G"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False

    return tmpseq
import collections

def countNucFrequency(seq):
    # tmpFreqDict  = {"A":0, "T":0,"C":0,"G":0} #For-loop is nice and clean when we do it this way
    # for nuc in seq:
        # tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(collections.Counter(seq)) #This works because DNAseq or seq is already validated beforehand


#Think of how to optimize that? How to optimize with collection?
