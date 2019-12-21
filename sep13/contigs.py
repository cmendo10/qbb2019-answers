#!/usr/bin/env python3

"""
Parse and print all records from a FASTA file
"""

import sys


class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.eof:
            # return None, None
            raise StopIteration
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
            #If we reach here, ident is set correctly
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
                
        sequence = "".join(sequences)
        return ident, sequence
                
fasta_name = FASTAReader(open(sys.argv[1]))

counter = 0
sequencelist = []
for ident, sequence in fasta_name:
    counter += 1
    # print(sequence)
    sequencelist.append(len(sequence))
    sequencelist.sort()
    
# print(sequencelist)
print(counter)
print(min(sequencelist))
print(max(sequencelist))
avg = sum(sequencelist) / len(sequencelist)
print(avg)


middle = sum(sequencelist)/2
n50= 0
counter = 0
for contig_length in sequencelist:
   counter += contig_length
   if counter >= middle:
       n50 = contig_length
print(n50)

# n50 = max(sequence)/2
# print(sequencelist[n50])
# print(sequencelist[143])



# sum = sum(sequencelist)
# total_length = 0
#
# for i, item in enumerate(sequencelist):
#     total_length += len(item)
#     if total_length >= sum/2:
#         print([i])
#         print(len(i))
    
    #if total length >= midpoint of whole sequence: 
        

#What I want to work:

# reader = FASTAReader(f)
#
# while True:
#     ident, sequence = reader.next()
#     if ident is None:
#         break
#     print(ident, sequence)