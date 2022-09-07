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
	n = 4
	plist = sieve.primerange(1000,9999)
	pstrings = []
	for i in plist:
		pstrings.append( "".join(sorted("%s"%i)    ) )
	for j in pstrings:
		# Test for digit '3'
		d = '3'
		m = n-1
		while m:
			posn = j.find( d*m )
			if posn != -1:
				print(j)
				break
			m -= 1
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
