import math
import cmath
def cube_root(x):
    return x**(1/3)
def s_q(x):
    return x**(2)

x = input('Enter the Subjected Tensile Load:')
y = input('enter the yeild strength of matterial:')
z = input('enter the factor of safety for rods and spigots:')
w = input('enter the factor of safety for Cotter')
p = float(x)
syt = float(y)
fr = float(z)
fc = float(w)

#permissible stresses for rods and spigots
print('permissible stresses for rods and spigots')
str = syt/fr
scr = 2*str
taor = 0.5*str
print('permissible tension:',str)
print('permissible compression:',scr)
print('permissible shear:',taor)
#permissible stresses for cotter
print('permissible stresses for cotter')
stc = syt/fc
#scc = 2*stc
taoc = 0.5*stc
print('permissible tension:',stc)
#print('permissible compression:',scc)
print('permissible shear:',taoc)

#Diameter of rod
temp = (4*p)/(3.14*str)
d = math.sqrt(temp)
d = d + (3-d%3)
t = 0.31*d
print('diameter of the rods :',d)
print('thickness of the cotter :',t)
A1 = 3.14/4
B1 = -t
C1 = -p/str
sol1 = (-B1 + math.sqrt(s_q(B1)-(4*A1*C1)))/(2*A1)
sol2 = (-B1 - math.sqrt(s_q(B1)-(4*A1*C1)))/(2*A1)
if sol1 > sol2 :
    d2 = sol1
else :
    d2 = sol2
d2 = d2 + (5-d2%5)
print('diameter of the spigot :',d2)

# for socket diameter
A2 = 3.14/4
B2 = -t
C2 = (t*d2)-((s_q(d2)*3.14)/4 )-(p/str)
sol12 = (-B2 + math.sqrt(s_q(B2)-(4*A2*C2)))/(2*A2)
sol22 = (-B2 - math.sqrt(s_q(B2)-(4*A2*C2)))/(2*A2)
if sol12 > sol22 :
    d1 = sol12
else :
    d1 = sol22

d1 = d1 + (5-d1%5)
print('outer diameter of the socket :',d1)

#diameter of spigot collar
d3 = 1.5*d
d4 = 2.4*d
print('diameter of spigot collar :')
print('d3 :',d3)
print('d4 :',d4)
# dimensions of a and c
a = 0.75*d
c = a
print('dimensions of a and c :')
print('a :',a)
print('c :',c)
# width of the cotter
b = p/(2*taoc*t)
b = b+(5-b%5)
print('width of the cotter :',b)
