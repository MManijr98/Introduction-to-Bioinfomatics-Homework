# Name: Michael Manigault
# Course: CSC 336/BIO 336
# Date: 2/21/19
# Summary of what your program does. Maximum 30 words.
# Summary: This program contains code pretaining to the length of an RNA sequence, the amount of codons said sequenece contains, where the start codon is located and the first for codons of the sequence.


print ('Enter an RNA sequence:' ,)
rnaSequence = ('AUGACCGAUUGACGA')

print ('RNA sequence:' , rnaSequence)

print ('Length of RNA sequence:' , len(rnaSequence))

print ('The RNA sequence contains' , len(rnaSequence) / 3 , 'codons and start codon in position' , rnaSequence[0:3])


print ('The first four codons in the sequence are:')
print (rnaSequence[0:3])
print (rnaSequence[4:7])
print (rnaSequence[8:11])
print (rnaSequence[12:15]) 

