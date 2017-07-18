# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:55:48 2017

@author: Isaac Ng
"""


#find the nth fibo number without calculating everything that came before
def fibo(n):
    n += 1
    phi = (1+(5**0.5))/2
    altphi = (1-(5**0.5))/2
    return int((phi**n-altphi**n)/(phi-altphi))

#n=[0]
#m=2
#while fibo(m)<4000000:
#    n.append(fibo(m))
#    m += 3
#print sum(n)            #euler project q2

  
#prime sieve - horribly inefficient         
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

#efficient sieve
def sieve(n):
    numbers = range(2, n+1)
    idx = 0
    current_number = numbers[idx]
    while current_number < (n+1)**0.5:
        #sets non primes divisible by the current_number to 0
        #kinda hacky that last statement after the [0] 
        #because i got lazy to calculate how many elements there are lol
        #edit: it's (math.ceil((49-1)/n)) but that's another calculation
                    
        numbers[current_number+idx::current_number] = [0]*len(numbers[current_number+idx::current_number])
        
        #go to next number
        idx += 1
        current_number = numbers[idx]
        
        #search for next prime (there's a version of this that executes first then checks right?)
        while current_number == 0:
            idx += 1
            current_number = numbers[idx]
        
#        print numbers
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
    if x == 0:
        return []
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
    #tests if x is prime. optional argument primedict provides faster method
    #the primedict should contain all primes smaller than x
    #this tests for all primes smaller than sqrt(x)
    #proof that 
    #sqrt(x) < the next smallest prime 
    #is still needed
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
#print isprime(100)

def nthprime(n):
    n = int(n)
    if n == 0:
        return "go home you're drunk"
    primelist = [2]
    test = 3
    while len(primelist) < n:
        if isprime(test):
            primelist.append(test)
        test += 1
    return primelist[-1] 
    
#print nthprime(10001) #euler problem 7

              
              
              
euler8test = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

euler8test = euler8test.replace("\n", "")


#returns the product of all numbers in a list
#same as np.product or something like that
def productlist(lis):
    pdt = 1
    for n in lis:
        n = int(n)
        pdt = n*pdt
    return pdt

def euler8(n=euler8test):
    possibilities = euler8test.split("0")
    possibilities2 = []
    highest = 0
    for n in possibilities:
        if len(n) >= 13:
            possibilities2.append(n)
    for n in possibilities2:
        idx = 0
        while idx <= len(n)-13:        
            testcase = productlist(n[idx:idx+13])
            if testcase > highest: 
                highest = testcase
            idx += 1
    return highest
        
    
#print euler8(euler8test)
    

def euler9():
    l = []
    for n in range(1,1001):
        for m in range(1,1001-n):
            for p in range(1,1001-n-m):
                if n**2+m**2 == p**2 and n+m+p == 1000:
                    l.append([n,m,p])
    return l
#this is honestly a p stupid way of doing it
#print euler9()


#def euler9(n):
    #find all pytho triplets under n
    # 1. sum of all pytho triplets is always even
    #   proof is trivial

    # 2.1 pythogran triplets are either primitive, or not
    #   A primitive triplet: a**2 + b**2 = c**2
    #   where gcd(a,b,c) = 1
    #   i.e. coprime
    #    non-primitive: (ka)**2 + (kb)**2 = (kc)**2
    #   == k(primitive)
    # 2.2 (primitive) pytho triplets can be generated with pairs of numbers
    #   c = sqrt((m**2+n**2)/2), b = m+n, a = n-m
    #   we can use this to iterate through the search space much more efficiently
    
    # 3. there's more but i'm not alert enough to care now
    
#sums all primes under n, euler10
def sumofprimes(n=2000000):
    primes = numbers = sieve(n)
    #bottom lines are redundant really, but filter seems the fastest by a wee bit
    primes = filter(None, primes)
#    primes = [x for x in numbers if x is not 0]
    return sum(primes)


e11_grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""
e11_grid = e11_grid.split("\n")
e11 = []
for row in e11_grid[1:-1]:
    e11.append([int(n) for n in row.split(" ")])
#now we have a more workable data structure

#in hindsight this question was a lesson in how efficient numpy is

def euler11(grid=e11, howmanynumbers = 4):
    #insight: we only need to test rightwards, downwards, topright, and downright diagonal
    #this is because multiplication is commutative
    #left-to-right will take the form (grid[n][m])(grid[n][m+1])(grid[n][m+2])...
    #top-to-bottom will take the form (grid[n][m])(grid[n+1][m])(grid[n+2][m])...
    #diagonal: (grid[n][m])(grid[n+1][m+1])(grid[n+2][m+2])...
    #other diagonal... use your brain
    #the main question is how to handle corners? 
    
    nrows = len(grid)
    ncols = len(grid[0])
    
    #first calc all products in a col(vert) from left to right, top to bottom
    #e.g. for 6x4, n = 3 numbers, we want to start at x's and multiply down
    #leaving one row alone because that goes out of index
    """
    xxxxxx
    xxxxxx
    xxxxxx
    oooooo
    """
    #some time can be saved with an overall max variable but this way it's more expandable
    maxcol = 0
    for col in range(ncols):
        for row in range(nrows-(howmanynumbers-1)):
            #someday i'll have to rewrite this with numpy
            listtomultiply = [grid[selectedrow][col] for selectedrow in range(row, row+howmanynumbers)]
            if productlist(listtomultiply) > maxcol:
                maxcol = productlist(listtomultiply)
    
    maxrow = 0
    for row in range(nrows):
        for col in range(ncols-(howmanynumbers-1)):
            listtomultiply = grid[row][col:col+howmanynumbers]
            if productlist(listtomultiply) > maxrow:
                maxrow = productlist(listtomultiply)
              
    #bottom right diag
    """
    xxxxxo
    xxxxxo
    xxxxxo
    oooooo
    """
    maxdiag1 = 0
    for row in range(nrows-howmanynumbers-1):
        for col in range(ncols-(howmanynumbers-1)):
            
            rows = range(row, row+howmanynumbers)
            cols = range(col, col+howmanynumbers)  
            coordinates = zip(rows, cols)
            listtomultiply = []
            
            for rcoordinate, ccoordinate in coordinates:
                listtomultiply.append(grid[rcoordinate][ccoordinate])
                
            if productlist(listtomultiply) > maxdiag1:
                maxdiag1 = productlist(listtomultiply)
        

    #topright diag
    """
    oooooo
    xxxxxo
    xxxxxo
    xxxxxo
    """""
        
    maxdiag2 = 0
    for row in range(nrows-howmanynumbers-1):
        for col in range(howmanynumbers-1,(howmanynumbers)):
            
            rows = range(row, row+howmanynumbers)
            cols = range(col, col+howmanynumbers)[::-1]  
            coordinates = zip(rows, cols)
            listtomultiply = []
            
            for rcoordinate, ccoordinate in coordinates:
                listtomultiply.append(grid[rcoordinate][ccoordinate])
                
            if productlist(listtomultiply) > maxdiag2:
                maxdiag2 = productlist(listtomultiply)
    
    return max([maxrow, maxcol, maxdiag1, maxdiag2])
    
print euler11()

def trianglenumber(n):
    return int((n+1)*(n/2.0))

for n in range(20):
    print trianglenumber(n), primefactorise(trianglenumber(n))
    
def e12(ndivisors = 500):
    n = 0
    testdivisors = 0
    while testdivisors < ndivisors:
        factors = primefactorise(trianglenumber(n))
        


#timer f(x)
import time
def lol():
    curr = time.time()
    for n in range(100):
#        testfunc here
        pass
    print (time.time()-curr)/100
                   
#print lol()
    

