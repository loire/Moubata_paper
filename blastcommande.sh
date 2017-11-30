#!/bin/bash
#$ -V 
#$ -q bigmem.q
#$ -cwd
#$ -pe parallel_smp 35

module load bioinfo/ncbi-blast/2.2.31
blastp -num_threads 35 -query Francisella_sp_proteine_fasta.txt -db /bank/uniprot/uniprot_sprot.fasta -max_target_seqs 1 -outfmt "6 qacc sacc evalue qlen slen" > blastp_uniprotsprot.txt

