import math
f = 500
V = 5

omega  = 2 * math.pi * f 
C = 0.01

r = [30,10,50,68,5.6,100,20,30]

V_R = []
V_C = []

for i in range(len(r)):
    V_R.append(r[i] * V / math.sqrt(r[i]**2 + (1/2*math.pi*f*C)**2))
    V_C.append((1/2*math.pi*f*C) * V /math.sqrt(r[i]**2 + (1/2*math.pi*f*C)**2))