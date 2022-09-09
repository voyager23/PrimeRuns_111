#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  a_dev.py
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
from sympy import sieve,prime

def main(args):
	# consider 4 digit primes
	# use tuple to associate (prime,string)
	digits = ('0','1','2','3','4','5','6','7','8','9')
	n = 4
	
	plist = sieve.primerange(10**(n-1),10**n)
	pstrings = []
	for i in plist:
		pstrings.append( (i,"".join(sorted("%s"%i))) )
	
	SSums = 0
	for d in digits:
		m = n-1
		N = 0
		S = 0
		while m:
			for j in pstrings:
				posn = j[1].find( d*m )
				if posn != -1:
					print(j)
					N += 1
					S += j[0]
					continue
			if N == 0:
				m -= 1
				continue
			else:
				print(f"max substring {d*m} count {N} Sum {S}")
				SSums += S
				break
		print(f"Sum of sums {SSums}")
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
