def DNA_strand(dna):
	DNA_comp = ''
	for i in dna:
		if(i == 'A'):
			DNA_comp += 'T'
		elif(i == 'T'):
			DNA_comp += 'A'
		elif(i == 'G'):
			DNA_comp += 'C'
		elif(i == 'C'):
			DNA_comp += 'G'
	return(DNA_comp)

print(DNA_strand("ATTGC"))