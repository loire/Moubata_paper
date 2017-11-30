#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

require(ape)
require(seqinr)
alig = read.dna(file=args[1],format="fasta")
d = dist.dna(alig)
alig = read.alignment(file=args[1],format="fasta")
dnds = kaks(alig)


cat(paste(labels(d)[1],round(d[1],digits = 4)),labels(d)[2] , dnds$ka, dnds$ks, dnds$ka/dnds$ks, dnds$vka, dnds$vks,  "\n")


