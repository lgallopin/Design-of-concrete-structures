# utf-8

from math import *


print(u"###### donnees de base ######")

fck = 30.0
fcd = fck/1.5
fyk = 500.0
fyd = fyk/1.15
g=0.0310
q=0.0170
l=6.0
b=0.2
d=0.3
#3HA8

print ("fck ="+str(fck))
print ("fcd ="+str(fcd))
print ("fyk ="+str(fyk))
print ("fyd ="+str(fyd))
print ("g ="+str(g))
print ("q ="+str(q))
print ("l ="+str(l))
print ("b ="+str(b))
print ("d ="+str(d))

pu = 1.35*g+1.5*q
ved = pu*l/2.0

print("pu ="+str(pu))
print("ved ="+str(ved))

print("3 armatures transversales sur appuis")
print("3.1 resistance des bielles")

z=0.9*d

vrdmax=0.6*(1.0-fck/250.0)*fcd*b*z/2.0
print("vrdmax "+str(str(vrdmax)))
if vrdmax>ved:
    print("OK")
else:
    print("nok")

print("3.2taux de ferraillage")
#reduction sur appuis
ved=ved-d*pu

Asws = ved/(fyd*z)
print("asws ="+str(Asws))
#2 HA8

print("3.4 Espacement longitudinal")
Asw = 0.000101
s = Asw/Asws
print("s ="+str(s))
print("min(0.6,0.75*d) ="+str(min(0.6,0.75*d)))
if s<min(0.6,0.75*d):
    print("OK")
else:
    print("nOK")

print("3.5 Smin Smax")
smax = 0.75*d
smin = 0.07

print("smax ="+str(smax))
print("smin ="+str(smin))

if smin < s < smax:
    print("OK")
else:
    print("nok")

print("3.6 taux armature effort tranchant mini maxi")

Aswsmin = b*0.08*sqrt(fck)/fyk
Aswsmax = b*(0.6*(1.0-fck/250)*fcd)/(2.0*fyd)
smax = Asw/Aswsmin
smin = Asw/Aswsmax

print("smax ="+str(smax))
print("smin ="+str(smin))

if smin < s < smax:
    print("OK")
else:
    print("nok")


