# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:55:48 2017

@author: Isaac Ng
"""

def fibo(n):
    n += 1
    phi = (1+(5**0.5))/2
    altphi = (1-(5**0.5))/2
    return int((phi**n-altphi**n)/(phi-altphi))

n=[0]
m=2
while fibo(m)<4000000:
    n.append(fibo(m))
    m += 3
#print sum(n)            #euler project q2

  
         
def sieve(n):
    numbers = range(2, n+1)
    notprime = []
    for n in numbers:
        for m in numbers:
            notprime.append(n*m)
    for number in notprime:
        if number in numbers:
            numbers.remove(number)
    print "sieve generated"
    return numbers

  
    
#print sieve(100)
#    
#def primefactorise(n):
#    primes = sieve(int(n**0.5))
##    primes = sieve(n)
#    factors = []
#    for prime in primes:
#        if n%float(prime) == 0:
#            factors.append(prime)
#            n = n/prime
#        print prime, "calculated"
#    return factors

#print primefactorise(600851475143)

def isprime(x, primedict = None):
    if x == 2: return True
    if primedict == None:
        upperlimit = int(x**0.5)+1
        #print range(2,upperlimit+1)
        for testnumber in xrange(2,upperlimit+1):
            #print float(x), testnumber, float(x)%testnumber
            if float(x)%testnumber == 0:
                return False
        return True
    else:
        for testprime in primedict:
            if float(x)%testprime == 0:
                return False
        return True            
        
    

def primefactorise(x):
    x = float(x)
    testprime = 2
    factors = []
    primedict = [2]
    while x != 1.0:
        if x%testprime == 0:
            factors.append(testprime)
            x = x/testprime
        else:
            testprime = testprime+1             #add 1, then test if it's prime. if not then add agn
            while not isprime(testprime, primedict):               #basically find the next prime
                testprime = testprime+1
            primedict.append(testprime)
    return factors


#for n in [2,3,6,8,9,12,47,100,600851475143]:
#    print n, primefactorise(n)
    
def ispalindrome(x):
    x=str(x)
    for idx in range(len(x)):
        if x[idx-1]==x[-idx]:
            pass
        else:
            return False
    return True

#biggestpalindrome = 0
#for n in xrange(999,0,-1):
#    for m in xrange(999,n,-1):
#        if n == 993:
#            print m
#        if ispalindrome(n*m) and n*m>biggestpalindrome:
#            biggestpalindrome = n*m
#            print n,m
#print biggestpalindrome


def gcd(a,b):
    num1 = max (a,b)
    num2 = min (a,b)
    while num1 != num2:
        num1 = num1 % num2
        if num1 == 0:
            break
        num2 = num2 % num1
        if num2 == 0:
            break
    return max(num2,num1)


def gcdmultiple(listofnumbers):
    while len(listofnumbers) != 1:
        listofnumbers[0] = gcd(listofnumbers[0],listofnumbers[1])
        listofnumbers.pop(1)
    return listofnumbers[0]

def lcm(a,b):
    return a/gcd(a,b)*b

def lcmmultiple(listofnumbers):
    while len(listofnumbers) != 1:
        listofnumbers[0] = lcm(listofnumbers[0],listofnumbers[1])
        listofnumbers.pop(1)
    return listofnumbers[0]

#print lcmmultiple(range(1,21))

###
from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt(((p1.x-p2.x) ** 2) + ((p1.y-p2.y) ** 2))
    side2 = sqrt(((p2.x-p3.x) ** 2) + ((p2.y-p3.y) ** 2))
    side3 = sqrt(((p3.x-p1.x) ** 2) + ((p3.y-p1.y) ** 2))
    s = (side1 + side2 + side3)/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area
###

def sumofsquares(n):
    total = 0
    for m in range(n+1):
        total += m**2
    return total

def squareofsum(n):
    return((n+1)*n/2)**2

#for n in range(10):
#    print "sumofsquares: %i squareofsum: %i" %(sumofsquares(n), squareofsum(n))
    
#print squareofsum(100)-sumofsquares(100)

a = []

def isprime(x, primedict = None):
    if x == 2: return True
    if primedict == None:
        upperlimit = int(x**0.5)+1
        #print range(2,upperlimit+1)
        for testnumber in xrange(2,upperlimit+1):
            #print float(x), testnumber, float(x)%testnumber
            if float(x)%testnumber == 0:
                return False
        return True
    else:
        for testprime in primedict:
            if float(x)%testprime == 0:
                return False
        return True  
print isprime(100)


