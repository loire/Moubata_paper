#!/usr/bin/env python
import sys
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
from Bio.Emboss.Applications import NeedleCommandline
from Bio import AlignIO



querydict = SeqIO.to_dict(SeqIO.parse(open("Francisella_sp_proteine_fasta.txt",'r'),"fasta"))
subjdict = SeqIO.to_dict(SeqIO.parse(open("localbase/francisella_close.aa.fasta",'r'),"fasta"))

queryNTdict = SeqIO.to_dict(SeqIO.parse(open("Francisella_sp_gene_fasta.txt","r"),"fasta"))
subjNTdict = SeqIO.to_dict(SeqIO.parse(open("localbase/francisella_close.nt.fasta","r"),"fasta"))

#print(queryNTdict.keys())

bbh  = open("ID_pairs_homologs.txt",'r')

i=0
for line in bbh: 
	print "treating gene number "+str(i)
	i+=1
	c = line.split()
	qid = c[1]
	sid = c[0]
#	percid = float(c[2])
#	length  = int(c[3])
#	mismatch = int(c[4])
#	gap  = int(c[5])
#	qstart = int(c[6])
#	qend = int(c[7])
#	sstart = int(c[8])
#	send = int(c[9])
#	eval = float(c[10])
#	bits = float(c[11])
	qseq = querydict[qid].seq
	sseq = subjdict[sid].seq
#	print(qid)
#	print(sid)
#	print(len(qseq))
#	print(len(sseq))
	alig = pairwise2.align.localds(qseq,sseq,MatrixInfo.blosum62,-5,-0.5,one_alignment_only=1)
	wf = open(qid+".prot.alig.fasta",'w')
	wf.write(">"+qid+"\n")
	wf.write(str(alig[0][0])+"\n")
	wf.write(">"+sid+"\n")
	wf.write(str(alig[0][1])+"\n")
	wf.close()
	wnt = open(qid+".nt.seqs_to_align.fasta","w")
	handle = [queryNTdict[qid],subjNTdict[sid]]
	SeqIO.write(handle,wnt,"fasta")

#	print(format_alignment(*alig[0]))



