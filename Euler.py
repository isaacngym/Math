# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:55:48 2017

@author: Isaac Ng
"""
import time
import math
import itertools
from math import sqrt
from collections import Counter

#find the nth fibo number without calculating everything that came before
def fibo(n):
    n += 1
    phi = (1+(5**0.5))/2
    altphi = (1-(5**0.5))/2
    return int((phi**n-altphi**n)/(phi-altphi))

def euler2():
    n=[0]
    m=2
    while fibo(m)<4000000:
        n.append(fibo(m))
        m += 3
    return sum(n)

#prime sieve in list form, consolidated removes zeros
def sieve(n, consolidated = True):
    numbers = range(2, int(n)+1)
    idx = 0
    current_number = numbers[idx]
    print current_number
    while current_number < (n+1)**0.5 +1:
        #sets non primes divisible by the current_number to 0
        #kinda hacky that last statement after the [0] 
        #because i got lazy to calculate how many elements there are lol
        #edit: it's (math.ceil((49-1)/n)) but that's another calculation         
        numbers[current_number+idx::current_number] = [0]*len(numbers[current_number+idx::current_number])
        print numbers
        #go to next number
        idx += 1
        current_number = numbers[idx]
        print current_number
        #search for next prime (there's a version of while that executes first then checks right?)
        while current_number == 0:
            idx += 1
            current_number = numbers[idx]
            print current_number
        
    if consolidated == True:
        numbers = filter(None, numbers)
    print "sieve generated:"
    print numbers
    return numbers 

#prime tester that can take in a prime dictionary
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

#takes in a positive int 
#might be faster in some cases? testing needed
def primefactorise(x, primedict = None, verbose = True):
    m = x
    if x == 1 or x == 0: return []
    toreturn = []
    if primedict == None or max(primedict) < x**0.5:
        if verbose == True: print "no dict or dict not suitable, your calculation may be slower"
        for n in range(2,int(math.ceil(x**0.5))+1):
            if x%n == 0:
                while x%n == 0:
                    x = x/n
                    toreturn.append(n)
    # elif max(primedict) >= x**0.5:
    else:
        if verbose == True: print "using primedict: only useful for large numbers of primes"
        for n in primedict:
            if x%n == 0:
                while x%n == 0:
                    x = x/n
                    toreturn.append(n)
            
    if x != 1:
        if isprime(x) == False:
            print x, m, "x, m"
            print toreturn
        toreturn.append(x)
    
#    print toreturn, "toreturn"
    return toreturn

def euler3():
    return primefactorise(600851475143)

def ispalindrome(x):
    x=str(x)
    for idx in range(len(x)):
        if x[idx-1]==x[-idx]:
            pass
        else:
            return False
    return True

#takes in a number and returns a boolean
def ispalindrome(x):
    return str(x) == str(x)[::-1]

#biggestpalindrome = 0
#for n in xrange(999,0,-1):
#    for m in xrange(999,n,-1):
#        if n == 993:
#            print m
#        if ispalindrome(n*m) and n*m>biggestpalindrome:
#            biggestpalindrome = n*m
#            print n,m
#print biggestpalindrome

#calculates gcd of two numbers
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

class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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




#TEST FOR SPEED
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

              
              
              



#returns the product of all numbers in a list
#same as np.product or something like that
def productlist(lis):
#    print lis
    pdt = 1
    for n in lis:
        n = int(n)
        pdt = n*pdt
    return pdt

#oh this is faster. reduce!
def productlist(lis):
    return reduce(lambda x, y: x*y, lis)

def numsearch(x):
    possibilities = x.split("0")
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
        
def euler8():
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
    return numsearch(euler8test)
    
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
#there's a better parameterisation of pytho triplets below
##TODO
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
    return sum(primes)


#e11_grid = """
#08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
#49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
#81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
#52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
#22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
#24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
#32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
#67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
#24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
#21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
#78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
#16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
#86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
#19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
#04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
#88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
#04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
#20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
#20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
#01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#"""
#e11_grid = e11_grid.split("\n")
#e11 = []
#for row in e11_grid[1:-1]:
#    e11.append([int(n) for n in row.split(" ")])
#now we have a more workable data structure

#in hindsight this question was a lesson in how efficient numpy is

def euler11(grid=[], howmanynumbers = 4):
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
    
#print euler11()

##gauss oh gauss
def trianglenumber(n):
    return int((n+1)*(n/2.0))

def e12(ndivisors = 500):
    n = 0
    testdivisors = []
    while True:
        
        testdivisors = []
        factors = primefactorise(trianglenumber(n))
        factors.append(1)
        
        #factors to prime factors
        for numberoffactors in range(len(factors)):
#            print trianglenumber(n)
            for factorset in itertools.combinations(factors, numberoffactors):
                testdivisors.append(productlist(list(factorset)))
#                print testdivisors, factorset, 111111
#            print testdivisors, n, 222222
        
        testdivisors = list(set(testdivisors))
        if len(testdivisors) > ndivisors:
            break
        
        n += 1
        #i don't get why this works but it does so let's go w it
        print trianglenumber(n-1)
    testdivisors.sort()
    print testdivisors
        
    return trianglenumber(n)
       
#a = time.time()
#print e12(500)
#b = time.time()
#print (b-a)/60
#ur an idiot this took 5 min
#you don't need to multiply all the prime factors
#let t be triangle number
#t can be expressed as f1**p1 * f2**p2 * ... fn**pn
#the number of factors can be expressed by: how many f1's do you want? f2s? f3s? fns?
#so that's (f1+1) * (f2+1) * ... * (fn+1)

def e12(ndivisors = 500):
    n = 0
    testdivisors = []
    while True:
        factors = primefactorise(trianglenumber(n))
        factors = Counter(factors).items()
#        print ([count+1 for factor, count in factors])
        
        numfactors = productlist([count+1 for factor, count in factors])
        if numfactors > ndivisors:
            break
        n += 1
        if n%1000 == 0:
            print n
    return trianglenumber(n)

##TODO - why is this so fast??
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def lol():
    curr = time.time()
    for n in range(1):
#        testfunc here
        factors(10000000001)
        pass
    print (time.time()-curr)/1
                   
# print lol()
def euler13():
    e13 = """37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    89261670696623633820136378418383684178734361726757
    28112879812849979408065481931592621691275889832738
    44274228917432520321923589422876796487670272189318
    47451445736001306439091167216856844588711603153276
    70386486105843025439939619828917593665686757934951
    62176457141856560629502157223196586755079324193331
    64906352462741904929101432445813822663347944758178
    92575867718337217661963751590579239728245598838407
    58203565325359399008402633568948830189458628227828
    80181199384826282014278194139940567587151170094390
    35398664372827112653829987240784473053190104293586
    86515506006295864861532075273371959191420517255829
    71693888707715466499115593487603532921714970056938
    54370070576826684624621495650076471787294438377604
    53282654108756828443191190634694037855217779295145
    36123272525000296071075082563815656710885258350721
    45876576172410976447339110607218265236877223636045
    17423706905851860660448207621209813287860733969412
    81142660418086830619328460811191061556940512689692
    51934325451728388641918047049293215058642563049483
    62467221648435076201727918039944693004732956340691
    15732444386908125794514089057706229429197107928209
    55037687525678773091862540744969844508330393682126
    18336384825330154686196124348767681297534375946515
    80386287592878490201521685554828717201219257766954
    78182833757993103614740356856449095527097864797581
    16726320100436897842553539920931837441497806860984
    48403098129077791799088218795327364475675590848030
    87086987551392711854517078544161852424320693150332
    59959406895756536782107074926966537676326235447210
    69793950679652694742597709739166693763042633987085
    41052684708299085211399427365734116182760315001271
    65378607361501080857009149939512557028198746004375
    35829035317434717326932123578154982629742552737307
    94953759765105305946966067683156574377167401875275
    88902802571733229619176668713819931811048770190271
    25267680276078003013678680992525463401061632866526
    36270218540497705585629946580636237993140746255962
    24074486908231174977792365466257246923322810917141
    91430288197103288597806669760892938638285025333403
    34413065578016127815921815005561868836468420090470
    23053081172816430487623791969842487255036638784583
    11487696932154902810424020138335124462181441773470
    63783299490636259666498587618221225225512486764533
    67720186971698544312419572409913959008952310058822
    95548255300263520781532296796249481641953868218774
    76085327132285723110424803456124867697064507995236
    37774242535411291684276865538926205024910326572967
    23701913275725675285653248258265463092207058596522
    29798860272258331913126375147341994889534765745501
    18495701454879288984856827726077713721403798879715
    38298203783031473527721580348144513491373226651381
    34829543829199918180278916522431027392251122869539
    40957953066405232632538044100059654939159879593635
    29746152185502371307642255121183693803580388584903
    41698116222072977186158236678424689157993532961922
    62467957194401269043877107275048102390895523597457
    23189706772547915061505504953922979530901129967519
    86188088225875314529584099251203829009407770775672
    11306739708304724483816533873502340845647058077308
    82959174767140363198008187129011875491310547126581
    97623331044818386269515456334926366572897563400500
    42846280183517070527831839425882145521227251250327
    55121603546981200581762165212827652751691296897789
    32238195734329339946437501907836945765883352399886
    75506164965184775180738168837861091527357929701337
    62177842752192623401942399639168044983993173312731
    32924185707147349566916674687634660915035914677504
    99518671430235219628894890102423325116913619626622
    73267460800591547471830798392868535206946944540724
    76841822524674417161514036427982273348055556214818
    97142617910342598647204516893989422179826088076852
    87783646182799346313767754307809363333018982642090
    10848802521674670883215120185883543223812876952786
    71329612474782464538636993009049310363619763878039
    62184073572399794223406235393808339651327408011116
    66627891981488087797941876876144230030984490851411
    60661826293682836764744779239180335110989069790714
    85786944089552990653640447425576083659976645795096
    66024396409905389607120198219976047599490197230297
    64913982680032973156037120041377903785566085089252
    16730939319872750275468906903707539413042652315011
    94809377245048795150954100921645863754710598436791
    78639167021187492431995700641917969777599028300699
    15368713711936614952811305876380278410754449733078
    40789923115535562561142322423255033685442488917353
    44889911501440648020369068063960672322193204149535
    41503128880339536053299340368006977710650566631954
    81234880673210146739058568557934581403627822703280
    82616570773948327592232845941706525094512325230608
    22918802058777319719839450180888072429661980811197
    77158542502016545090413245809786882778948721859617
    72107838435069186155435662884062257473692284509516
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690"""
    e13sum = 0
    #
    for n in e13.split('\n'):
        e13sum += int(n[:12])
    
    #euler 13
    print str(e13sum)[0:10]


def collatz(n, collatzdict = {}):
    initialn = n
    iterations = 0
    while n != 1:
        if n%2 == 1:
            n = 3*n + 1
        elif n%2 == 0:
            n = n/2
        else:
            print initialn, iterations
            return "ERROR"
        iterations += 1
        if n in collatzdict:
            ans = collatzdict[n] + iterations
            collatzdict[initialn] = ans
            return ans
    if initialn not in collatzdict:
        collatzdict[initialn] = iterations
    return iterations


# a more mathematical programming way - it's slow tho
#collatzdict = {}
#def collatz(n, collatzdict = collatzdict):
#    if n == 1:
#        return 0
#    elif n%2 == 1:
#        return (collatz(3*n+1) + 1)
#    elif n%2 == 0:      
#        return (collatz(n/2) + 1)
#    else:
#        print "panic"
#
#for n in range(1,1000000):
#    ans = collatz(n)
#    if n not in collatzdict:
#        collatzdict[n] = ans
#                   
# this line makes it slow
#print max(collatzdict, key = lambda x: collatzdict[x])


def euler14(n):
    c = {}
    maxcollatz = 0
    numberwithlongestcollatzchain = 0
    for number in xrange(1, n):
        curr = collatz(number, c)
        if curr > maxcollatz:
            maxcollatz = curr
            numberwithlongestcollatzchain = number
#            print maxcollatz
    return numberwithlongestcollatzchain

#print euler14(1000000)


#euler 15: a square k lines long will have (2k choose k) paths 
def nchoosek(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

#euler 15 generalised: Permute 5 from 5, with 2 x 20 repeated elements
def e15permutewithreplacements(p, q):
    n = p + q
    k = p
    ans = math.factorial(n)/(math.factorial(k)*math.factorial(q))
    return ans

#multi-dimensional euler 15?
#def e15(n = 20, m = 20, *arg):
    
def sumdigits(n):
    ans = 0
    for n in str(n):
        ans += int(n)
    return ans

#40.5us
def sumdigits(n):
    return sum([int(digit) for digit in str(n)])

#11.5us wth
def sumdigits2(n):
    return reduce(lambda x, y: x+y, str(n))


#for n in range(50):
#    print n, sumdigits(2**n)

#factors(n) is faster. WHY?
##todo
def allfactors(n, primedict = None, verbose = True):
    primefactors = primefactorise(n, primedict, verbose)
#    print list(set([factor for nprimefactor in range(len(primefactors)) for factor in itertools.combinations(primefactors,nprimefactor)]))
#    would it be better to take the set of factors? why does it not include all prime factors of n in the set? idekkk
    factors = list(set([productlist(factor) for nprimefactor in range(len(primefactors)+1) for factor in itertools.combinations(primefactors,nprimefactor)]))
    return factors    

#what's the sum of amicable pairs under 10000?
def e21():
    e21 = {}
    e21sieve = sieve(10001**0.5)
    amicablepairs = []
    for n in range(10001):
        e21[n] = sum(allfactors(n, e21sieve, False))
           #allfactors includes the number itself. amicable numbers don't need that
           #1 is an bother in this case
        if n != 1:
            e21[n] = e21[n] - n 
    #    if n%100 == 0:
    #        print n
    for number in e21:
        if e21.get(e21[number]) == number and e21[number] != number:
            amicablepairs.append(number)
    print sum(amicablepairs) #e21

          
#given <days> days and <people> people, what's the chance that there's AT LEAST 
#1 repeat of their birthdays, given that their birthdays have uniform prob          
def birthdayproblem(days, people):
    prob = 1
    for person in range(1, people):
        prob *= (1-((person)/float(days)))
    return 1 - prob
#print birthdayproblem(365, 23)

#how many ways are there to permute something, such that no one item is in its original place
def derangement(n, d = {1:0, 2:1}):
#    print n
    if n == 0:
        return 0
    if n in d:
        return d[n]
    else:
        ans = (n-1)*(derangement(n-1)+derangement(n-2))
        d[n] = ans
    return ans

    
