#!/usr/bin/python

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')

onetwo={}
twoone={}

for line in f1: 
	c = line.split()
	qid = c[0]
	sid = c[1]
	onetwo[qid]=sid


for line in f2: 
	c = line.split()
	qid = c[0]
	sid = c[1]
	twoone[qid]=sid

for q in onetwo:
	if q==twoone[onetwo[q]]:
		print onetwo[q],q
#	print q,onetwo[q],twoone[onetwo[q]]





f1.close()
f2.close()


























