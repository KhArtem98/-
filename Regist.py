#!/usr/bin/env python
import sys
import random
import hashlib
import json
import os
from json import JSONDecoder 
import base64
import js2py

def N2():	
    global N 
    N = 23
    n = 2**N
    global lst
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
                continue
        for j in lst:
                if j*j-1 > i:
                    lst.append(i)
                    break
                if (i % j == 0):
                    break
        else:
            lst.append(i)
    p = random.choice(lst)
    while p < 3:
        p = random.choice(lst)
        if p > 3:
            break
    return p

def N3():
    global p
    p = N2()
    global q
    q = random.choice(lst)
    while q < 2**(N-1) or q > 2**(N+1):
        q = random.choice(lst)
        if q > 2**(N-1) and q < 2**(N+1):
            break
    global k
    k = 0
    while k == 0 or k == q:
        k = random.randint(1, q-1)
    K = k
    J = 0
    global a
    global b
    while J==0 or J==1728:
        a = 3*K%p
        b = 2*K%p
        J = 1728*(4*(a**3))/(4*(a**3)+27*(b**2))%p
        if J==0 or J==1728:
            
            while K == 0 or K == q:
                K = random.randint(1, q-1)
            continue
        else:
            break
    return q

def N4():
    global xP, yP
    yP=0
    while yP==0:
        for i in range(1,p):
            xP = i
            A = xP**3+a*xP+b
            yP = math.sqrt(A)%p
            if yP==0:
                continue
            else:
                break
    return xP, yP
	
def N5(k, xP,yP):
    x1 = xP
    x2 = xP
    x3 = xP
    y1 = yP
    y2 = yP
    y3 = yP
    V = ((3*(x1**2)+a)/(2*y1))%p
    V = int(V)
    x3 = V**2-x1-x2
    y3 = V*(x1-x3)-y1
    for i in range(k-1):
        f1 = y1-y3
        f2 = x1-x3
        try:
            V = (f1/f2)%p
        except ZeroDivisionError:
            V=0
        V = int(V)
        x = x3
        x3 = V**2-x3-x1
        y3 = V*(x-x3)-y3
    return x3, y3

M = json.loads(base64.b64decode(sys.argv[1]))
h = hashlib.sha256(M.encode('ascii')).hexdigest()
g = bin(int(h, 16))[2:]

l=len(str(g))
H=[]
for i in range(l-1,-1,-1):
    t = str(g)[i]
    H.append(t)
H = list(map(int, H))
g = int(''.join(map(str, H)))

v = len(str(g))
g = int(g)
z=0
for i in range(v):
    try:
        z = (z + g // 10**i % i)*2^i
    except ZeroDivisionError as err:
        continue
N3()
e = z%q
if e == 0:
	e = 1

r = 0
s = 0
while r == 0 or s == 0:
    xP, yP = N4()
    x, y = N5(k,xP,yP)
    r=x%q
    d = random.randint(1, q-1)
    xQ, yQ = N5(d, xP, yP)
    s = (r*d+k*e)%q
    if r==0 or s==0:
        continue

def con(u):
    t = []
    while u:
        t = [u & 1] + t
        u >>= 1
    return t
u1 = con(r)
u2 = con(s)
l1=len(u1)
l2=len(u2)
w = u1 + u2
res = int(''.join(map(str, w)))
w= int(str(res), 2)

T = str(M)+','+str(w)
q=str(q)
Q = str(xQ)+','+str(yQ)
L =str(l1)+','+str(l2)
res = 'path1='+L+'&path2='+Q+'&path3='+q+'&path4='+T

data = {'path1': L, 'path2': Q, 'path3': q, 'path4': T}
with open('datas.json', 'w') as outfile:
	json.dump(data, outfile)