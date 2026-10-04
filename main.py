from DNAtoolkit import *
import random
rndDNAStr = "ACTGACTGACTG"

#generate random DNA string
randomDNAstring = ''.join([random.choice(Nucleotides) for nuc in range(123)])

DNAstr = validateSeq(randomDNAstring)
print(DNAstr)
print(countNucFrequency(DNAstr)) #See how many times a nucleotide is found in a DNA sequence