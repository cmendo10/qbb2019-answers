#!/usr/bin/env python3



from fasta_kmer import FASTAReader
import sys



target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
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
            
kmer_out = []         
for ident1, sequence1 in query:
    sequence1 = sequence1.upper()
    ignore_set = set()
    for q in range(0, len(sequence1) - k + 1):
        kmer_q = sequence1[q:q+k]
        if kmer_q in kmers_dict:
            for target_start, target_id in kmers_dict[kmer_q]:
                if (target_id,target_start) in ignore_set:
                    continue
                match_len = k
                seq = kmer_q
                last_target_start = target_start
                x = q + 1
                while x < len(sequence1) - k +1:
                    next_kmer = sequence1[x:x+k]
                    if next_kmer in kmers_dict:
                        flag = False
                        for i, ident in kmers_dict[next_kmer]:
                            if ident == target_id and i == last_target_start + 1:
                                match_len += 1
                                last_target_start += 1
                                flag = True
                                seq = seq + next_kmer[-1]
                                ignore_set.add((ident,i))
                        if not flag:
                            break
                    else:
                        break
                    x += 1
                kmer_out.append((match_len, seq, target_id, target_start, q))
        
    for match_len, seq, target_id, target_start, j, in sorted(kmer_out,reverse=True,key=lambda t:t[0]):
        print(match_len, seq, target_id, target_start, q)    
            
            
            
