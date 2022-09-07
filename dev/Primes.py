#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  primes.py
#  
# Module primes file

from sympy import sieve,prime
from functools import reduce

# Grow the sieve to cover all primes <= n (a real number).
sieve.extend(1000)

def nth_prime(n):
	print(n, sieve[n])
	
def factors(n,unique=False,radical=False):
	if n < 2: return n
	# return a list of all prime factors of n
	lpf = []
	lunique = []
	lo,hi = sieve.search(n)
	#print(f"n:{n} lo:{sieve[lo]} hi:{sieve[hi]}")
	m = n
	i = 1	# first prime = 2
	while i <= lo:
		if m % sieve[i] == 0:
			lpf.append(sieve[i])
			m = m / sieve[i]
			while m % sieve[i] == 0:
				lpf.append(sieve[i])
				m = m / sieve[i]
		i += 1
	print("lpf",lpf)
	if unique==True or radical==True:
		while len(lpf)>0:
			p = lpf.pop(0)
			try:
				if p != lunique[-1]:
					lunique.append(p)
			except IndexError:
				lunique.append(p)
			
		if radical == True:
			return(reduce(lambda a,b:a*b, lunique))
		else:
			return lunique
			
	return lpf
	
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
