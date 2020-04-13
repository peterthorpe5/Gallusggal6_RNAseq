import os
import sys
from optparse import OptionParser
import datetime
from collections import defaultdict

f_in = open("aa.fasta_vs_nr_tax.tab", "r")

name_to_annot = defaultdict(str)

for line in f_in:
    if line.startswith("#"): continue
    if line.strip():
        data = line.split("\t")
        name = data[0]
        annot = data[12]
        name_to_annot[name.rstrip()] = annot.rstrip()
f_in.close()

wanted = """sampleA
ENSGALT00000027850.6
ENSGALT00000106077.1
ENSGALT00000063371.2
ENSGALT00000084212.2
ENSGALT00000093696.1
ENSGALT00000091563.1
ENSGALT00000001004.6
ENSGALT00000024213.6
ENSGALT00000103955.1
ENSGALT00000095777.1
ENSGALT00000073443.2
ENSGALT00000075595.2
ENSGALT00000055325.2
ENSGALT00000099296.1
ENSGALT00000027215.6
ENSGALT00000066642.2
ENSGALT00000094440.1
ENSGALT00000023888.7
ENSGALT00000104567.1





""".split()
for i in wanted:
    print(i, "\t", name_to_annot[i])
           
    
		
