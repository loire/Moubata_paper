#!/usr/bin/python
import sys

LQf = open("Length_francisella.txt",'r')
LDBf  = open("Length_uniprot.txt",'r')

pairf = open("ID_pairs_homologs.txt",'r')


LQ = {}

for line in LQf:
	c = line.split()
	LQ[c[0]]  = c[1]

LDB = {}

for line in LDBf:
	c = line.split()
	LDB[c[0]]  = c[1]


for line in pairf:
	c = line.split()
	print c[0],c[1],LQ[c[0]],LDB[c[1]]


