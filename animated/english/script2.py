#!/bin/env python

ifile=open("elementi.dat","r")
#head=open("head","r")
#tail=open("tail","r")
ifile2=open("elements.dat","r")
lines=ifile.readlines()
lines2=ifile2.readlines()
elementi=[]
elements=[]
for i in range(1,len(lines)):
	if "<!--TITOLOOOOOOOOOOOOOOO-->" in lines[i]:
		elementi.append(lines[i+1].strip())

for i in range(1,len(lines2)):
	if "INIZIO" in lines2[i]:
		elements.append(lines2[i+2].strip())

print(elementi)
print(elements)
ifile.close()
ifile2.close()

for j in elements:
	with open("head") as head:
		with open("tail") as tail:
			fin=open(j+".txt","r")
			out=open(elementi[elements.index(j)]+".html","w")
			for line in head:
				out.write(line.replace("Antilope",j))
				
			next(fin)
			for line in fin:
				out.write(line.replace("<text1>", " "))
			for line in tail:
				check=["pasta","Antilope"]
				repl=[elementi[elements.index(j)],j]
				for c, r in zip(check,repl):
					line=line.replace(c, r)
				out.write(line)
			fin.close()
			out.close()

