import sys
import random
import math
import hashlib
import os
import json
from json import JSONDecoder

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

json = os.getenv('JSON')
M = JSONDecoder().decode(json)
List = M.split(',')

with open("data.json") as file_in:
    records = json.load(file_in)
    L = records[0]["1"]
    xy = records[0]["2"]
    q = records[0]["3"]

y, x = math.modf(xy)
y = str(y)[2:]
y = int(y)
l2, l1 = math.modf(L)
l2 = str(l2)[2:]
l2 = int(l2)

w = int(List[1])
w= bin(w)[2:]
w = str(w)
r1 = w[:l1]
s1 = w[l2:]
r1 = int(r1, 2)
s1 = int(s1, 2)
if r1>0 and r1<q and s1>0 and s1<q:  
else:
    sys.exit()

m = List[0]
h = hashlib.sha256(m.encode('ascii')).hexdigest()
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
E = z%q
if E == 0:
	E = 1

v = (E**(-1))%q
z1 = (s1*v)%q
z2 = ((-1)*r1*v)%q
z1 = int(z1)
z2 = int(z2)
xP, yP = N4()
xz1, yz1 = N5(z1,xP,yP)
xz2, yz2 = N5(z2, xQ, yQ)
xC = xz1+xz2
yC = yz1+yz2
R = xC%q

if R==r1:
    Str = 'верные данные'
else:
    Str = 'неверные данные'
print(Str)