#!/bin/env python


ifile=open("elementi.dat","r")

lines=ifile.readlines()
elementi=[]
for i in range(len(lines)):
	if "INIZIO" in lines[i]:
		elementi.append(lines[i+2].strip())

print(elementi)
for j in elementi:
	for i in range(11):
		if j in lines[i]:
			print(j)
			for k in range(i,11):
				#print(lines[k])
				el_file=open(j+".txt","a")
				start=False
				if "<!--========================-->" in lines[k]:
					print(j)
					start=True
					continue
				elif "</text1>" in lines[k]:
				#	print(k)
					start=False
					break
				#else:
				#	print(lines[k])
					#el_file.write(lines[k])


#print(elementi)
#print(len(elementi))
