#! /usr/bin/env python

'''
Author: Adam Hennefer
Date: April 14, 2021

To get run time stats:
python -m cProfile coreSE_challenge.py

'''
from collections import Counter


print('\n   Largest Common Byte Strand\n')


files = ['sample.1','sample.2','sample.3','sample.4','sample.5',
		'sample.6','sample.7', 'sample.8','sample.9','sample.10']
glossary = {}
common_bytes = []
max_len = 0
longest_common =  bytes()


for file_num, file_name in enumerate(files):
	offset = 0
	with open(file_name, 'rb') as file:
		for strand in file:
			strand_len = len(strand)
			try:
				prev = glossary[strand]
				# try clause will only continue if the byte strand was in the glossary
				if strand == longest_common:
					common_bytes.append(('   sample.'+str(file_num+1), offset))
				elif strand_len > max_len:
					max_len = strand_len
					longest_common = strand
					common_bytes = [prev, ('   sample.'+str(file_num+1), offset)]
			except KeyError as e:
				glossary[strand] = ('   sample.'+str(file_num+1), offset)
			offset += strand_len

if not common_bytes:
	print('   No common bytes found.')
else:
	print('{0:<10} {1:>9}'.format('   File','Offset'), sep="  ")
	for file, offset in common_bytes:
		print('{0:<10} {1:>8}'.format(file, offset), sep="  ")

