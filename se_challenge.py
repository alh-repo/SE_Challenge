#! /usr/bin/env python

'''
Author: Adam Hennefer
Date: April 24, 2021
Requires:  Python 3.6

To get run time stats:
python -m cProfile se_challenge.py

'''
import os

print('\n   Longest Common Byte Strand:\n')


files = ['sample.1','sample.2','sample.3','sample.4','sample.5',
		'sample.6','sample.7', 'sample.8','sample.9','sample.10']
cache = {}
common_bytes = []
max_len = 0
longest_common =  bytes()


for file_name in files:
	if common_bytes:   # clear cache smaller than largest common byte
		#print(f"{'size of cache: ': >11} {len(cache): >9}")
		cache = {k:v for (k, v) in cache.items() if len(k) > max_len}
	
	file_size = os.path.getsize(file_name)
	offset = 0
	with open(file_name, 'rb') as file:
		for strand in file:
			strand_len = len(strand)
			try:
				prev = cache[strand] 
				if strand == longest_common:
					common_bytes.append((file_name, offset))
				elif strand_len > max_len:
					max_len = strand_len
					longest_common = strand
					common_bytes = [prev, (file_name, offset)]
			except KeyError as e:
				if strand_len > max_len:
					cache[strand] = (file_name, offset)
			offset += strand_len
			# lazy file read
			if (file_size - offset) < max_len:
				break

if not common_bytes:
	print('   No common bytes found.\n')
else:
	print(f"{'Files': >11} {'Offset': >9}")
	for file, offset in common_bytes:
		print(f"{file: >11} {offset: >9}")
