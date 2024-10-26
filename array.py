# Array problems
"""
# array 1
def function_1(n):
  a = []
  for i in range(n):
    a.append(2*i +1)
  print(a)

  

# array 2

def function_2(n):
  a = []
  for i in range(n):
    a.append(2**i)
  print(a)

  
# array 3 

def function_3(n, A, D):
  a = []
  for i in range(n):
    a.append(A+ i*D)
  print(a)

# array 4

def function_4(n, A, D):
  a = []
  for i in range(n):
    a.append(A  * D**i)
  print(a)


  
#array 5 

def function_5(n):
  a = [0 ,1]
  if n == 0:
    print(1)
  if n == 1:
    print(1)
  else:
    for i in range(n - 2):
        
        a.append(a[i] + a[i+1])
    print(a)


#array 6
def function_6(n ,A, B):
    assert n > 2
    a = [A, B]
    for i in range(n -2):
        a.append(sum(a) )
    print(a)


#array 7

def function_7(n):
    
    n.reverse()
    print(n)

# array 8

def function_8(n):
    a = []
    for i in range(len(n)):
        if(n[i]% 2!= 0):
            a.append(n[i])
    a.sort()
    print(a)
    print(len(a))

# array 9

def function_9(n):
    a = []
    for i in range(len(n)):
        if(n[i]% 2== 0):
            a.append(n[i])
    a.sort(reverse = True)
    print(a)
    print(len(a))

# array 10 

def function_10(n):
    a = []
    b = []
    for i in range(len(n)):
        if(n[i] % 2 == 0):
            a.append(n[i])
        else:
            b.append(n[i])
    a.sort()
    b.sort(reverse = True)
    print(a)
    print(b)


# array 11

def function_11(n, K):
    assert 1 <= K < len(n)
    a = []
    i = 1
    while(K *i < len(n)):
        a.append(n[K*i])
        i = i +1
    print(a)

# array 12

def function_12(n):
    assert len(n) % 2 == 0
    a = []
    i = 0
    while(i < len(n)):
        a.append(n[i])
        i += 2
    print(a)

# array 13
def function_13(n):
    assert len(n) % 2 != 0
    a =[]
    i = 1
    while( i <= len(n) -1 ):
        a.append(n[i])
        i += 2
    print(a)


# array 14

def function_14(n):
    a = []
    b = []
    i =0
    while(i <len(n)):
        a.append(n[i])
        i +=2
    j = 1 
    while(j < len(n) ):
        b.append(n[j])
        j +=2
    print(a)
    print(b)


    
# array 15

def function_15(n):
    a = []
    b = []
    i =0
    j =1
    while(i  < len(n)):
        a.append(n[i])
        
        i +=2
    while( j < len(n)):
        b.append(n[j])
        j += 2
    b.sort()
    a.sort(reverse =True)
    print(b)
    print(a)


# array 16

def function_16(n):
    a = []
    b = []
    for i in range(len(n)):
        a.append(n[i])
        a.append(n[- 1 - i])
    
    for j in range(len(n)):
        b.append(a[j])
        
    print(b)


# array 17

def function_17(n):
    a = []
    b = []
    i =0
    while(i < len(n) - 1):
        a.append(n[i])
        a.append(n[i+1])
        a.append(n[-1-i])
        a.append(n[-2-i])
        i +=2
    for j in range(len(n)):
        b.append(a[j])
    print(b)


# array 18

def function_18(n):
    a = []
    i = 0
    while i < len(n) and n[-1] <= n[i]:
        a.append(n[i])
        i += 1
    k = len(a)
    if k <len(n):
        
        print(n[k])
    else:
        print(0)


    
# array 19

def function_19(n):
    a =[]
    for i in range(len(n)):
        if n[i] > n[0] and n[i] < n[-1]:
            a.append(n[i])
    if len(a)  == 0:
        print(0)
    else:
        print(a[-1])

# array 20

def function_20(N, K,L):
    a = N[K+1:L]
    print(sum(a))



# array 21

def function_21(N,K,L):
    a = N[K+1:L]
    print(
    sum(a) / len(a)
    )


# array 22

def function_22(N,K,L):
    a = []
    b = []
    c = []
    a= sum(N)
    for i in range(K+1):
        b.append(N[i])
    for j in  range(L+1):
        c.append(N[j])
    print(
    a - (sum(c) - sum(b) - N[L] ) 
    )

# array 23 

def function_23(N,K,L):
    a = []
    b = []
    c = []
    a = sum(N)
    for i in range(K+1):
        b.append(N[i])
    for j in  range(L+1):
        c.append(N[j])
    print(
    (a- (sum(c) - sum(b) - N[L])) / (len(N) - (L - K -1))
    )

# array 24 

def function_24(n):
    a = []
    for i in range(len(n)-1):
        a.append(n[i+1] - n[i])
    b = all(x == n[1] - n[0]  for x in a)
    if b == True:
        print(n[1] - n[0])
    else:
        print(0)
        
    print(a)
    print(b)

# array 25

def function_25(n):
    a = []
    for i in range(len(n) -1):
        a.append(n[i+1] / n[i])
    b = all(x == n[1] / n[0] for x in a)
    if b == True:
        print(
        n[1]/ n[0]
        )
    else:
        print(0)


# array 26

def function_26(n):
    a = []
    for i in range(0, len(n) -1, 2):
        if n[i] % 2 == 0 and n[i+1] % 2 == 1:
            a.append(n[i])
            a.append(n[i+1])
        else:
            break
    if len(a) == len(n):
        print(0)
        
    elif len(n) % 2 == 1:
        print("Number of elements in the array should be even")
    
    else:
        k =  n.index(n[len(a)]) 
        print(k+1)

# array 27

def function_27(n):
    A = [j for j, k in enumerate(n) if k == 0]
    if not A:
        pass
    else:
        print(A)
    if n[0] < 0:
        print("First element")
    for i in range(1, len(n)):
        if i % 2 == 0 and n[i] <=0:
            return i
        elif i % 2 == 1 and n[i] >=0:
            return i
    return 0


# array 28

def function_28(n):
    a = []
    for i in range(0, len(n), 2):
        a.append(n[i])
    return max(a)

# array 29

def function_29(n):
    a = []
    for i in  range(1, len(n), 2):
        a.append(n[i])
    return min(a)
"""

"""
def function_30(n):
    a = []
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            a.append(i)

        
    print(a)
    print(len(a))

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_30(n)

"""

"""
def function_31(n):
    a= []
    for i in range(len(n)-1):
        if n[i] < n[i+1] :
            a.append(i+1)
    a.sort(reverse= True)
    print(a)
    print(len(a))

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_31(n)

"""
"""
def function_32(n):
    a = []
    for i in range(len(n)-2):
         if n[i] > n[i+1] and n[i+1] < n[i+2]:
              a.append(i+1)
    print(a[0])

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_32(n)

"""
"""
def function_33(n):
    a = []
    for i in range(len(n) - 2):
        if n[i] < n[i+1] and n[i+1] > n[i+2]:
            a.append(i+1)
    print(a[-1])


n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_33(n)
"""
"""
def function_34(n):
    a = []
    for i in range(len(n) -2):
        if n[i] > n[i+1] and n[i+1] < n[i+2]:
            a.append(n[i+1])
    print(max(a))

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_34(n)
"""
"""
def function_35(n):
    a = []
    for i in range(len(n) -2):
        if n[i] < n[i+1] and n[i+1] > n[i+2]:
            a.append(n[i+1])
    print(min(a))

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_35(n)

"""
"""
def function_36(n):
    a = []
    for i in range(len(n) -2):
        if (n[i] > n[i+1] and n[i+1] < n[i+2]) or (n[i] < n[i+1] and n[i+1] >n[i+2]):
            continue
        else:
            a.append(n[i+1])
    a.append(n[0])
    a.append(n[-1])
    if not a:
       print(0)
    else:
        print(max(a))
    

n =[ 3,1,4,1,5,9,2,6, 5,3,5,9]
function_36(n)
"""
"""
def function_37(n):
    a = []
    for i in range(len(n)-2):
        if n[i] < n[i+1] and n[i+1] > n[i+2]:
            a.append(n[i+1])
    if n[-1] > n[-2]:
        a.append(n[-1])
            
            
        
    print(len(a))

n =[1,2,3,4,0,8,9,10,7,6,5,19,20,21,22,23]
function_37(n)
"""
"""
def function_38(n):
    a = []
    for i in range(len(n) -2):
        if n[i+1] < n[i] and n[i+1] < n[i+2]:
            a.append(n[i+1])
    if n[-1] < n [-2]:
        a.append(n[-1])
    print(len(a))



n = [6,5,4,5,9,10,8,7, 10,2,1,0]
function_38(n)

"""
"""
def function_39(n):
    a = []
    for i in range(len(n) -2):
        if (n[i+1] > n[i] and n[i+1] > n[i+2]) or (n[i+1] < n[i] and n[i+1] < n[i+2]):
            a.append(n[i+1])
    if n[-1] > n[-2] or n[-1] < n[-2]:
        a.append(n[-1])
    print(len(a))

n = [1,2,3,4,5,4,3,2,7,8,9,11,9,8,77,77,77,80,79]
function_39(n)
"""
"""
def function_40(n, R):
    a = []
    for i in range(len(n)):
        a.append(abs(n[i] - R))

    b = min(a)
    k = a.index(b)
    print(n[k])
    
    
n = [1,2,3,4,7]
function_40(n,5)
"""
"""
def function_41(n):
    a = []
    for i in range(len(n) -1):
        a.append(n[i] + n[i+1])
    b = max(a)
    k = a.index(b)
    print(n[k], n[k+1])

n = [1,2,3,4,7,0,8,9,12,13]
function_41(n)
"""
"""
def function_42(n,R):
    a = []
    b = []
    for i in range(len(n) -1):
        a.append(n[i] + n[i+1])
    for j in range(len(a)):
        b.append(abs(a[j] - R))
    k = min(b)
    l = b.index(k)
    print(n[l], n[l+1])

n = [1,2,3,4,5,0,2,3,12,5,8,8,9,10,7,7]
function_42(n,17)
"""
"""
def function_43(n):
    a = []
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            continue
        else:
            a.append(n[i])
    a.append(n[-1])
    print(len(a))
    


n = [1,2,7,8,8,8,9,9,10,10,10,11,11,11,12,12]
function_43(n)
"""
"""
#array 44
def function_44(n):
    a = []
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[i] == n[j] and i !=j:
                a.append(i)
                a.append(j)
    b = []
    k = []
    if len(a) > 2:
        for i in range(0,len(a) - 2, 4):
            b.append(a[i])
            b.append(a[i+1])
        b.append(a[-1])
        b.append(a[-2])
        print(b)
    else:
        k.append(a[-1])
        k.append(a[-2])
        print(k)
    
n= [1,1,2,2,37,28,88, 9,12,13,14,9,18,18]
m= [4,4]
function_44(n)

"""
"""
#array 45
def function_45(n):
    a = []
    b = []
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                a.append(abs(n[i] - n[j]))
                b.append(i)
                b.append(j)
    k = min(a)
    l = a.index(k)
    
    print(b[2*l],b[2*l+1])
    

n = [1,48,50,51]
function_45(n)

"""
"""
# array 46 

def function_46(n,R):
    a = []
    b = []
    c = []
    d = []
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                a.append(n[i] + n[j])
                b.append(i)
                c.append(j)
    for m in range(len(a)):
        d.append(abs(a[m]  - R))
    k  = min(d)            
    l = d.index(k)
    print(n[b[l]])
    print(n[c[l]])
n = [3,4,9,16,1,2,10]
m = [1,2,3]

function_46(n, 26)
"""
"""
#array 47

def function_47(n):
    a = []
    for i in range(len(n)):
        if n[i] not in a:
            a.append(n[i])
            
                
                
    print(a)
n = [7,4,2,3,1,5,2,4,7,7]
function_47(n)
"""
"""
# array 48
n = [7,4,2,3,1,5,2,4,7,7,7,7,7,1,1,1,1,1,1,1,1,1]

def function_48(n):
    a = []
    b = []
    for i in range(len(n)):
        if n[i] not in a:
            a.append(n[i])
    for x in a:
        b.append(n.count(x))
    print(max(b))
function_48(n)
"""
"""
# array 49
def function_49(n):
    k = len(n)
    seen = set()
    for i in range(k):
        if n[i] < 1 or n[i]> k or n[i] in  seen:
            return i 
        seen.add(n[i])
    return 0
n = [1,2,3,4,5,7]
print(function_49(n))
"""
"""
# array 50

def function_50(n):
    j = 0
    for i in range(len(n)-1):
        if n [i] > n[i+1]:
            j += 1
    print(j)
n = [4,2,31,16,17,18,15]
function_50(n)
"""
#array 51
"""

def function_51(a,b,n):
    a,b = b , a
    print(a)
    print(b)

a = [1,2,3]
b= [4,5,6]
function_51(a,b, len(a))
"""
"""
# array 52

def function_52(a):
    n = len(a)
    b = []
    for i in range(n):
        if a[i] < 5:
            b.append(2 * a[i])
        else:
            b.append(a[i] / 2)
    print(b)

a  = [1,7,8,4]
function_52(a)
"""
"""
# array 52 
def function_53(a,b):
    n = len(a)
    c = []
    for i in range(n):
        c.append(max(a[i], b[i]))
    print(c)
a = [4,8,9,10]
b = [5,7,11,17]
function_53(a,b)
"""
"""
# array 54

def function_54(a):
    n = len(a)
    b= []
    for i in  range(n):
        if a[i] % 2 == 0:
            b.append(a[i])
    print(len(b), b)
a = [2,4,8 ,7,9,0, 15,17,19,22]
function_54(a)
"""
"""
# array 55

def function_55(a):
    n = len(a)
    b = []
    for i in range(1, len(a), 2):
        b.append(a[i])
    print(len(b), b)

a = [0,1,2,3,4,5,6,7,8,9]
function_55(a)
"""
"""
# array 56

def function_56(a):
    n = len(a)
    b = []
    for i in range(3, n , 3):
        b.append(a[i])
    print(len(b), b)
a= [0,1,2,3,4,5,6,7,8,9]
function_56(a)
"""
"""
# array 57
 
def function_57(a):
    n = len(a)
    b = []
    for i in range(0,n, 2):
        b.append(a[i])
    for i in range(1, n, 2):
        b.append(a[i])
    print(len(b), b)

a = [0,1,2,3,4,5,6,7,8,9]
function_57(a)
"""
"""
# array 58

def function_58(a):
    b = []
    for i in range(len(a)):
        b.append(sum(a[0:i+1]))
    print(b)

a =[0,1,2,3,4,5]
function_58(a)
"""
"""
# array 59

def function_59(a):
    n  = len(a)
    b = []
    for i in range(n):
        b.append(sum(a[0:i+1]  ) / (i+1))
    print(b)

a =[0,1,2,3,4,5]
function_59(a)
"""
"""
# array 60

def function_60(a):
    b = []
    for i in range(len(a)):
        b.append(sum(a[i::]))
    print(b)

a =[0,1,2,3,4,5]
function_60(a)
"""
"""
# array 61 

def function_61(a):
    b = []
    for i in range(len(a)):
        b.append(sum(a[i::]) / (i+1))
    print(b)
a =[0,1,2,3,4,5]
function_61(a)
"""
"""
# array 62

def function_62(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i] >=0:
            b.append(a[i])
        else:
            c.append(a[i])
    print(len(b), b)
    print(len(c), c)
a =[0,1,2,3,4,5, -8, -9, -13,-8]
function_62(a)
"""
"""
# array 63

def function_64(a,b):

    c = []

    for i in range(len(a)):
        c.append(a[i])
    for i in range(len(b)):
        c.append(b[i])
    c.sort()
    print(c)
a = [3,4,1,2,-3]
b = [9,12,1,7,5]
function_64(a,b)
"""
"""
# array 64

def function_64(a,b,c):
    d = []
    for i in range(len(a)):
        d.append(a[i])
    for i in range(len(b)):
        d.append(b[i])
    for i in range(len(c)):
        d.append(c[i])
    d.sort()
    print(d)

a = [1,2,3]
b= [-2,-1,-0]
c =[1,35,90]
function_64(a,b,c)
"""
"""
# array 65

def function_65(a, k):
    for i in range(len(a)):
        a[i] = a[i] + a[k]
    print(a)
a = [1,2,3]
function_65(a,2)
"""
"""
# array 66

def function_66(a):
    b = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
            break
        else:
            continue
    if not b:
        print("No even numbers")
    else:
        for i in  range(len(a)):
            if a[i] % 2 == 0:
                a[i] += b[0]

    print(a)
                
a = [1,2,3,5,7,8,10,2,6,9]
b = [1,3,5]
function_66(b)
"""
"""
# array 109

def function_109(n):
    a = []
    for i in range(len(n)):
        if n[i] < 0:
            a.append(i+1)
    for i in range(len(a)):
        n.insert(a[i] + i, 0)
    print(n)
n = [12,-3,4,5,-9, 9, 0, -8,-7,5,6,-2]
function_109(n)
"""
"""
# array 110
def function_110(n):
    a = []
    for i in range(len(n)):
        if n[i] % 2 == 0:
            a.append(n[i])
    for i in range(len(a)):
        n[i] += a[i]
    print(n)
n = [ 1,2,3,4,5,6,7,8,9]
function_110(n)
"""
"""
# array 111

def function_111(n):
    a = []
    for i in range(len(n)):
        if n[i] % 2 == 1:
            a.append(n[i])
    for i in range(len(a)):
        n[i] += 2 * a[i]
    print(n)
n = [ 1,2,3,4,5,6,7,8,9]
function_111(n)
"""
"""
# array 112

def function_112(n):
    for i in  range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    print(n)
n = [ -9, -9, 1,3,0, 9,8,77,7,7,7, 1,2,3]
function_112(n)
"""
"""
# array 113

def function_113(n):
    for i in range(len(n) - 1):
        min_i  = i
        for j in range(i+1, len(n)):
            if n[j]< n[min_i]:
                min_i = j
        n[i], n[min_i] = n[min_i], n[i]
    print(n)


n = [ -9, -9, 1,3,0, 9,8,77,7,7,7, 1,2,3]
function_113(n)
"""
"""
# array 114

def function_114(n):
    for i in range(1,len(n)):
        key = n[i]
        j = i-1
        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -=1
            n[j+1] = key
    print(n)


n = [ -9, -9, 1,3,0, 9,8,77,7,7,7, 1,2,3]
function_114(n)
"""

# array 115
"""
def function_115(n):
    m = n.copy()
    a = []
    b = []
    for i in range(len(m)):
        a.append(i)

    for i in  range(len(n)):
        for j in range(i, len(n)):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
                a[i], a[j] = a[j], a[i]
    for x  in a:
        b.append(n[x])
    print(a)
        
    
k = [ -9, -9, 1,3,0, 9,8,77,7,7,7, 1,2,3,0 ,2,19,99,109,900,1,2,9000]
    

    

function_115(k)
"""
"""

# array 116 

def function_116(A):
    if all(x == A[0] for x in A):
        print(A[0])
        print(len(A))
        return 0
    a = []
    b = []
    c = []
    d = []
    e = []
    for i in range(len(A) -1):
        if A[i] == A[i+1]:
            continue
        else:
            a.append(A[i])
            b.append(i+1)
    c.append(b[0])
    for i in range(len(b) -1):
        c.append(b[i+1] - b[i])
    for i in range(len(A) - 1):
        if A[-1-i] == A[-1 - (i+1)]:
            continue
        else:
            d.append(A[-1-i])
            e.append(i+1)
    a.append(d[0])
    c.append(e[0])

    print(a)
    print(c)
    
A = [ 1,1,1,3,3,2,2,2,2,2,7,8,9,9,9,10,10,10,9]
#print(function_116(A))
B = [1,1,1,1]
function_116(B)


"""
"""
# array 117

def function_117(n):
    if all(x == n[0] for x in n):
        n.insert(0, 0)
        print(n)
        return n
    a = []
    a.append(0)
    
    for i in range(len(n) - 1):
        if n[i] == n[i+1]:
            a.append(n[i])
        else:
            a.append(n[i])
            a.append(0)


A = [ 1,1,1,3,3,2,2,2,2,2,7,8,9,9,9,10,10,10,10,10,10,9,9]
B = [2,2,2,2,2]
function_117(A)
"""
"""
# array 118


def function_118(n):
    if all(x == n[0] for x in n):
        n.append(0)
        print(n)
        return n
    a = []
    for i in range(len(n) - 1):
        if n[i] == n[i+1]:
            a.append(n[i])
        else:
            a.append(n[i])
            a.append(0)
    
    a.append(n[-1])
    a.append(0)
    n = a
    print(n)
    
A = [ 1,1,1,3,3,2,2,2,2,2,7,8,9,9,9,10,10,10,10,10,10,9,9]
B = [2,2,2,2,2]
function_118(A)
"""
"""
# array 119

def function_119(n):
    if all(x == n[0] for x in n):
        n.append(n[0])
        print(n)
        return n
    a = []
    for i in range(len(n) - 1):
        if n[i] == n[i+1]:
            a.append(n[i])
        else:
            a.append(n[i])
            a.append(n[i])
    
    a.append(n[-1])
    a.append(n[-1])
    n = a
    print(n)
A = [ 1,1,1,3,3,2,2,2,2,2,7,8,9,9,9,10,10,10,10,10,10,9,9]
B= [1,1,1,1]
function_119(B)
"""
"""

#array 120

def function_120(n):
    a = []
    for i in range(len(n) -1):
        if n[i] == n[i+1]:
            a.append(n[i])
        
    print(a)
A = [2,2, 1,1,1,3,3,2,2,2,2,2,7,8,9,9,9,10,10,10,10,10,10,9,9,8,7,7]
B= [1,2,3,4,4]
function_120(B)
"""
# array 121
"""
def function_121(n, K):
    m = n.copy()
    a = []
    b = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    if len(a) < K:
        print("less than K")
    else:
        for i in range(b[K-1]):
            m.insert(sum(b[:K]), a[K-1])
    print(m)



n = [1,1,1,4,5,7,7,1,1,1,1,2,3]
function_121(n, 6)
"""
# array 122
"""
def function_122(n, K):
    m = n.copy()
    a = []
    b = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    if len(a) < K:
        print("less than K")
    else:
        for i in range(b[K-1]):
            m.pop(sum(b[:K-1]))
    print(m)
   

n = [1,1,1,4,5,7,7,1,1,1,1,2,3]
function_122(n, 1)

"""
# array 123
"""

def function_123(n, K):
    m = n.copy()
    a = []
    b = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    if len(a) < K:
        print("less than K")
        return 0
    else:
        for i in range(b[K-1]):
            m.pop(sum(b[:K-1]))
    for i in range(b[0]):
        m.insert(sum(b[:K-1]), a[0])
    for i in range(b[0]):
        m.pop(0)
    for i in range(b[K-1]):
        m.insert(0, a[K-1])
    print(m)
    

n = [1,1,2,3,4,4,4,5,6,7,7,7]
function_123(n, 7)
"""
# array 124
"""
def function_124(n, K):
    m = n.copy()
    a = []
    b = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    if len(a) < K:
        print("less than K")
        return 0
    else:
        for i in range(b[K-1]):
            m.pop(sum(b[:K-1]))
    for i in range(b[-1]):
        m.insert(sum(b[:K-1]), a[-1])
    for i in range(b[-1]):
        m.pop(-1)
    for i in range(b[K-1]):
        m.insert(len(n)-1, a[K-1])
    print(m)

n = [1,1,2,3,4,4,4,5,6,6,6,6,7]
function_124(n, 9)
"""

# array 125
"""
def function_125(n, K):
   
    a = []
    b = []
    c = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    
    for i in range(len(b)):
        if b[i] < K:
            c.append(0)
        else:
            for j in range(b[i]):
                c.append(a[i])
    print(c)

n = [1,1,1,2,3,4,4,4,5,6,6,6,6,7,7]
function_125(n,4)
"""
# array 126
"""
def function_126(n, K):
   
    a = []
    b = []
    c = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    
    for i in range(len(b)):
        if b[i]  ==  K:
            c.append(0)
        else:
            for j in range(b[i]):
                c.append(a[i])
    print(c)

n = [1,1,1,1,1,2,3,4,4,4,5,6,6,6,6,7,7,7,7]
function_126(n,4)
"""

# array 127
"""
def function_127(n, K):
   
    a = []
    b = []
    c = []
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    
    for i in range(len(b)):
        if b[i]  > K:
            c.append(0)
        else:
            for j in range(b[i]):
                c.append(a[i])
    print(c)

n = [1,1,1,1,1,2,3,4,4,4,5,6,6,6,6,6,7,7,7,7,7]
function_127(n,4)
"""
# array 128
"""
def function_128(n):
    a = []
    b = []
    m = n.copy()
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    j = b[0]
    c = []
    c.append(0)
    for i in range(1,len(b)):
        if b[i]>j:
            j = b[i]
            c.append(i)
    c[-1]
    m.insert(sum(b[:c[-1]]), a[c[-1]])
    print(m)
    
       
n = [1,1,1,1,1,2,3,4,4,4,5,6,6,6,6,6,6,7,7,7,7,7,6,6,6,6,6,6,9,9,9,9,9,9,]
function_128(n)

"""

# array 129
"""
def function_129(n):
    a = []
    b = []
    m = n.copy()
    val = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == val:
            length +=1
        else:
            a.append(val)
            b.append(length)
            val = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    j = b[0]
    c = []
    c.append(0)
    for i in range(1,len(b)):
        if b[i]>=j:
            j = b[i]
            c.append(i)
    c[-1]
    m.insert(sum(b[:c[-1]]), a[c[-1]])
    print(m)
    
n = [1,1,1,2,2,2,3,4,9,9,9]
function_129(n)
"""

# array 130
"""
def function_130(n):
    a = []
    b = []
    c = []
    j = n[0]
    length = 1
    for i in range(1, len(n)):
        if n[i] == j:
            length +=1
        else:
            a.append(j)
            b.append(length)
            j = n[i]
            length = 1
    a.append(n[-1])
    b.append(length)
    for i in range(len(b)):
        for j in  range(b[i]+1):
            c.append(a[i])
    print(c)
        


n = [1,2,3,4,4,5]
function_130(n)
"""

# array 131 
"""
def function_131(n,x,y):
    a  = []
    for i in range(len(n)):
        a.append(
            (((n[i][0])- x)**2 + (n[i][1] - y)**2)**(1/2)
        )
    
    print(n[a.index(min(a))])

        

n = [ [1,3], [2,3], [89,90], [1,1]]
function_131(n, 1,1)
"""

# array 132
"""
def function_132(n):
    a = []
    for i in range(len(n)):
        if n[i][0] < 0 and n[i][1] > 0:
            a.append(
                n[i][0]**2 + n[i][1]**2
            )
        if not a:
            print(0)
            return 0 
        
            
    print(
        n[a.index(max(a))]
    )
n = [[1,2], [2,3], [3,4], [5,6]]
function_132(n)
"""

def function_133(n):
    a = []
    for i in range(len(n)):
        if n[i][0]  * n[i][1] > 0:
            a.append(
                n[i][0]**2 + n[i][1]**2
            )
        if not a:
            print(0)
            return 0 
       
            
        
            
    print(
        n[a.index(max(a))]
    )
# n = [[1,2], [2,3], [3,4], [5,6], [-9,-10],[-20,90]]
# function_133(n)

# array 134 

def function_134(n):
    a = []
    b = []
    for i in range(len(n)):
        for j in range(len(n)):
            a.append(
                ((n[i][0] - n[j][0])**2 + (n[i][1] - n[j][1])**2)**(1/2)
            )
            b.append([i,j])
    
    
    m = b[a.index(max(a))]
    print(n[m[0]], n[m[1]])
    print(max(a))
        
#n = [[1,1], [2,3], [-3,5], [0,0], [3,-9], [100,100]]
#function_134(n)

# array 135 

def function_135(A,B):
    a = []
    b = []
    for i in range(len(A)):
        for j in range(len(B)):
            a.append(
                ((A[i][0] - B[j][0])**2 + (A[i][1] - B[j][1])**2)**(1/2)
            )
            b.append([i,j])
    m = a.index(max(a))
    l = b[m]
    print(max(a))
    print(A[l[0]], B[l[1]])
    

#A = [[1,2], [2,3]]
#B = [[0,0], [8,-9], [0,-1]]
#function_135(A,B)

# array 136

def function_136(n):
    a = []
    b = []
    c = []
    for i in range(len(n)):
        for j in range(len(n)):
            a.append(
                ((n[i][0] -n[j][0])**2  + (n[i][1] -n[j][1])**2 )
            )
            b.append([i,j])
   
    
    m = len(n)
    for i in range(0, len(a), len(n)):
        c.append(sum(a[i:i+m]))
    k = c.index(min(c))
    print(n[b[3*k][0]])

#n = [[0,0], [8,-9], [0,-1]]
#function_136(n)

""""
# demo version
# array 137  demo
def function_137_demo(n):
    a = []
    b = []
    for i in range(len(n)):
        for j in range(len(n)):
            for k in range(len(n)):
                if (i == j or j ==k or i == k) :
                    continue
                else:
                    a.append([n[i],n[j],n[k]])
    for i in range(len(a)):
        b.append(
            (
                ((a[i][0][0] - a[i][1][0])**2 + (a[i][0][1] - a[i][1][1])**2)**(1/2) + 
                ((a[i][0][0] - a[i][2][0])**2 + (a[i][0][1] - a[i][2][1])**2)**(1/2) +
                ((a[i][1][0] - a[i][2][0])**2 + (a[i][1][1] - a[i][2][1])**2)**(1/2) 

            )
        )

    m = b.index(max(b))
    print(a[m])
nm = [[0,0],[3,0], [0,4],[-3,0]]
n = [[0,0],[3,0], [0,4],[-3,0],[0.1, 0.2], [0.4,0.5], [-1,-2], [100,0], [200,1000]]

function_137_dmeo(n)
"""
# array 137 
def function_137(n):
    a = []
    b = []
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            for k in range(j+1,len(n)):
                a.append([n[i],n[j],n[k]])
    for i in range(len(a)):
        b.append(
            (
                ((a[i][0][0] - a[i][1][0])**2 + (a[i][0][1] - a[i][1][1])**2)**(1/2) + 
                ((a[i][0][0] - a[i][2][0])**2 + (a[i][0][1] - a[i][2][1])**2)**(1/2) +
                ((a[i][1][0] - a[i][2][0])**2 + (a[i][1][1] - a[i][2][1])**2)**(1/2) 
            )
        )
    m = b.index(max(b))
    print(a[m])
    


n = [[0,0],[3,0], [0,4],[-3,0],[0.1, 0.2], [0.4,0.5], [-1,-2], [100,0], [200,1000],[-900,0]]
m = [[0,0],[3,0], [0,4],[-3,0],[1,1], [99,99]]


function_137(n)



