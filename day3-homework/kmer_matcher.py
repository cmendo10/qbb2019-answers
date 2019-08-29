#!/usr/bin/env python3

"""
Matching kmers in a FASTA file

usage: ./kmer_matcher.py <target file> <query file> <k>
"""

from fasta_kmer import FASTAReader
import sys

#reader = FASTAReader(sys.stdin)

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open((sys.argv[2])))
k = int(sys.argv[3])
kmers_dict = {}
        

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer not in kmers_dict:
            kmers_dict[kmer] = [(i, ident)]
        else:
            kmers_dict[kmer].append((i, ident))
            
for ident1, sequence1 in query:
    sequence1 = sequence1.upper()
    for q in range(0, len(sequence1) - k + 1):
        kmer_q = sequence1[q:q+k]
        if kmer_q in kmers_dict:
            print(kmers_dict[kmer_q], str(q), kmer_q)
            
        
            
#for kmer, count in sorted(kmers.items(),
#                          key=lambda t: t[1]):
#    print(kmer, count, sep="\t")            
            

