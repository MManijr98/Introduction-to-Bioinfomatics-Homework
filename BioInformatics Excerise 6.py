Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print 'Thank you!'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Thank you!')?
>>> print (Think you!')
	   
SyntaxError: invalid syntax
>>> print Think you
	   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(Think you)?
>>> print 'Thank you!'
	   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Thank you!')?
>>> print ('Think you!')
	   
Think you!
>>> professor_name = 'Dr Otienburu'
	   
>>> print professoir_name
	   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(professoir_name)?
>>> print (professor_name)
	   
Dr Otienburu
>>> GC_content = 60
	   
>>> print ('The DNA strand contain' GC_content '% GCs')
	   
SyntaxError: invalid syntax
>>> GC = 60
	   
>>> print ('The DNA strand contain' GC '% GCs')
	   
SyntaxError: invalid syntax
>>> mydna = 'acgt'
	   
>>> mydna = mydna + mydna
	   
>>> GC_content 60
	   
SyntaxError: invalid syntax
>>> GC_content = 60
	   
>>> print ('The DNA strand contain' GC_content '%' GCs')
	   
SyntaxError: invalid syntax
>>> dna = 'atgtgtacc'
	   
>>> print 'dna'
	   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('dna')?
>>> dna = 'atgtgtacc'
	   
>>> print ('dna')
	   
dna
>>> nucl_1 = 'A'
nucl_2 = 'G'
nucl_3 = 'C'
nucl_4 = 'T'

print ('DNA that have high' , nucl_1 , nucl_4 , 'content is difficult to sequence.')
	   
SyntaxError: multiple statements found while compiling a single statement
>>> nucl_1 = 'A'
	   
>>> nucl_2 = 'G'
	   
>>> nuc1_3 = 'C'
	   
>>> nucl_4 = 'T'
	   
>>> print ('DNA that have high' , nucl_1 , nucl_4 , 'content is difficult to sequence.')
	   
DNA that have high A T content is difficult to sequence.
>>> dna = 'agtgtat'
dna.upper()
	   
SyntaxError: multiple statements found while compiling a single statement
>>> dna = "agtgtat'
	   
SyntaxError: EOL while scanning string literal
>>> dna.upper()
	   
'ATGTGTACC'
>>> dna = 'agtgtat'
	   
>>> dna.upper()
	   
'AGTGTAT'
>>> dna = 'gtgataggggggatatatatcgatcagatacggcggatcgatcgatcgatgatcgatcg'
	   
>>> dna.count('g')
	   
20
>>> mydna = 'acgt'
	   
>>> mydna = mydna + mydna
	   
>>> myDna
	   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    myDna
NameError: name 'myDna' is not defined
>>> GC_content = 60
	   
>>> print ('The DNA strand contains' GC_content '% GCs.')
	   
SyntaxError: invalid syntax
>>>  professor_name = 'Dr. Otienoburu'
	   
SyntaxError: unexpected indent
>>> professor_name = 'Dr. Otienoburu'
	   
>>> print 'Hello' professor_name
	   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello' professor_name)?
>>> professor_name = 'Dr. Otienoburu'
	   
>>> print ('Hello' professor_name)
	   
SyntaxError: multiple statements found while compiling a single statement
>>> professor_name = 'Dr. Otienoburu'
	   
>>> print ('Hello' professor_name)
	   
SyntaxError: invalid syntax
>>> professor_name = 'Dr. Otienoburu'
	   
>>>  print ('Hello', professor_name)
	   
SyntaxError: unexpected indent
>>> print ('Hello', professor_name)
	   
Hello Dr. Otienoburu
>>> GC_content = 60
	   
>>> print ('The DNA strand contains', GC_content, '% GCs.')
	   
The DNA strand contains 60 % GCs.
>>> 
