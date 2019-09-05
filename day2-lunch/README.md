Fastqc

head -40000 ../rawdata/SRR072893.fastq > SRR072893.10k.fastq
fastqc SRR072893.10k.fastq 
open SRR072893.10k_fastqc.html 

hisat2

hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893-hisat2.sam
less -S SRR072893-hisat2.sam 

samtools

samtools sort -@ 4 SRR072893-hisat2.sam -o SRR072893.bam
samtools index SRR072893.bam 

stringtie

stringtie SRR072893.bam -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o SRR072893.gtf
head SRR072893.gtf 


exercise 3:
cut -f 3 SRR072893-hisat2.sam | sort | grep -v '^@' | uniq -c
This is the slow way. The fast way is to uniq -c the entire bam which is aleady sorted.
The fastest way is to use SAMTOOLS idxstats


exercise 4:
The difference between each category is the number of "flags" associated with each. The reads that aligned have more flags such as NM, NH, MD as a few examples. Those that didn't align have columns. 