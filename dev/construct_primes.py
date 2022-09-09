#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  construct_primes.py
#  
#  Copyright 2022 mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import Primes


'''
	Prime.isprime() handles approx 100,000 queries/sec
	
	Note: search for maximum number of repeated digits - not longest run
	
	consider 4 digit primes 1000-9999
	repeated digit d = 0	not msd or lsd
	repeated digit 2,4,5,6,8	not prime if lsd
	repeated digit 1,3,7,9		? no restrictions ?
	3331
	3313 -18
	3133 -180
	1333  -1800
	
	7771
	7717 -54
	7177 -540
	1777 -5400
	drep0 = [0]	100x 200x 900x
	drepnotlsd = [2,4,5,6,8]
	drep = [1,3,7,9]
	
	
'''

def rot_right(m,width):
	d = m % 10
	m //= 10
	m = m + d * (10**(width-1))
	return m
	
def rot_left(m,width):
	d = m // 10**(width-1)	#MSD
	m %= 10**(width-1)	# remaining digits
	m = m*10 + d
	return m

def prime_runs(drep, width):
	# Construct a list of primes with runs of digits
	# list  of variable numbers in tuples indexed by the rep digit 0-9	
	n_var = (9,7,3,1)
	for var_d in n_var:
		s =  str(var_d) + str(drep)*(width-1)
		n = int(s)
		for x in range(width):
			print(n,end=" ")
			if Primes.isprime(n):
				print("Prime")
			else:
				print("Comp")
			n = rot_left(n,width)
		print()
			
def main(args):
	prime_runs(9,4)
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
