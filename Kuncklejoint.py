import math
def cube_root(x):
    return x**(1/3)

x = input('Enter the Subjected Tensile Load:')
y = input('enter the yeild strength of matterial:')
z = input('enter the factor of safety:')
p = float(x)
syt = float(y)
f = float(z)

#permissible stresses
st = syt/f
sc = st
tao = 0.5*sc
print('permissible tension:',st)
print('permissible compression:',sc)
print('permissible shear:',tao)

#Diameter of rod
temp = (4*p)/(3.14*st)
D = math.sqrt(temp)
D = D + (5-D%5)
D1 = 1.1*D
a = 0.75*D
b = 1.25*D
print('Diameter of rod D :',D)
print('Enlarged diameter of rod D1 :',D1)
#diameter of the pin
temp1 = (2*p)/(3.14*tao)
temp12 = math.sqrt(temp1)
temp2 = (32/(3.14*st))*(p/2)*((b/4)+(a/3))
temp22 = cube_root(temp2)
if temp22 > temp12:
    d = temp22
else :
    d = temp12
d = d + (5-d%5)
print('Diameter Of The Pin')
print('d :',d)
# dimentions of d1 & d0
d0 = 2*d
d1 = 1.5*d
print('d0 :',d0)
print('d1 :',d1)

#Check for the stresses
print('Verification of the Stresses')
stf = p/(b*(d0-d))
scf = p/(b*d)
taof = p/(b*(d0-d))
print('net tension :',stf)
print('net crushing :',scf)
print('net shear :',taof)



