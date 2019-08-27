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
