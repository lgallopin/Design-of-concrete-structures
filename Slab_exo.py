# utf-8

from math import *


# 4m entre axes
# epaisseur du plancher 16cm
# voiles 0.20
# 25mpa
# charge exploitation 10kn/m2




# moment en travee 
# mtx = 0.125plx2
# mty = 0
# moment sur appuis
# ma = 0 pour les maconneries
# ma = 0.15Mtx pour les voiles



print(u"###### donnees de base ######")

fck = 25.0
fcd = fck/1.5
fyk = 500.0
fyd = fyk/1.15
fctm = 0.3*(fck)**(2.0/3.0)
h = 0.16
a = 0.20
lnx = 4
lx = lnx +2.0*min(h/2,a/2)
phi = 0.01
cnom = 0.03
dx = h - cnom -  phi/2.0



print("fck ="+str(fck))
print("fcd ="+str(fcd))
print("fyk ="+str(fyk))
print("fyd ="+str(fyd))

print(u"2. Sollicitations")
print(u"2.1 Charge surfacique ")
#sur 1m de large
g = 1*h*0.025
q = 0.010

print ("g ="+str(g))
print ("q ="+str(q))

pu = 1.35*g+1.5*q
print ("pu ="+str(pu))

# print(u"2.2 ux et uy ")
# ro = lx/ly
# ux = 0.0820
# uy = 0.3289

# print("pu ="+str(pu))

print("2.3 moment direction principale")
# Mtx0 = ux*pu*lx**2
# print("ISO en travee Mtx0 ="+str(Mtx0))
Mtx = 0.125*pu*lx**2
print("Maxi en travee Mtx ="+str(Mtx))
# ma = 0.15Mtx pour les voiles
Max = 0.15*Mtx
print("Maxi sur appuis Max ="+str(Max))
# print("2.4 moment direction secondaire")
# Mty0 = uy*Mtx0
# print("ISO en travee Mty0 ="+str(Mty0))
# Mty = 0.85*Mty0
# print("Maxi en travee Mty ="+str(Mty))
# May = Max
# print("Maxi sur appuis May ="+str(May))

# print(u"2.5 Effort tranchant maxi sur appuis direction principale")
# vax = pu*lx / (2.0 + ro)
# print("vax ="+str(vax))
# print(u"2.6 Effort tranchant maxi sur appuis direction secondaire")
# vay = ro*pu*ly/3.0
# print("vay ="+str(vay))

print(u"3. Armatures horizontales")
print(u"3.1 direction principale")
d = dx
b = 1
print(u"Espacement horizontal maxi entre les barres")
sxmax =  min(3*h,0.4)
print("sxmax ="+str(sxmax))
print("Section minimale")
Asminx = max(0.26*fctm/fyk*b*d,0.0013*b*d)
print("Asminx ="+str(Asminx))
print("Calcul et choix armatures en travee")
muu = Mtx/(b*d**2*fcd)
au = 1.0/0.8*(1-(1-2*muu)**0.5)
yu = au*d 
zu = d - 0.4*yu
ro = fyd
Asreqt = Mtx/(zu*ro)
print("Asreqt ="+str(Asreqt))
if Asreqt<Asminx:
    print("===> section minimale requise")
else:
    print("===> ")

print("Calcul et choix armatures sur appuis")
muu = Max/(b*d**2*fcd)
au = 1.0/0.8*(1-(1-2*muu)**0.5)
yu = au*d 
zu = d - 0.4*yu
ro = fyd
Asreqa = Max/(zu*ro)
print("Asreqa ="+str(Asreqa))
if Asreqa<Asminx:
    print("===> section minimale requise")
else:
    print("===> ")

# print(u"3.2 direction secondaire")
# d = dy
# b = 1
# print(u"Espacement horizontal maxi entre les barres")
# sxmax =  min(3.5*h,0.45)
# print("sxmax ="+str(sxmax))
# print("Section minimale")
# # en travee
# Asminyt = 0.2*max(Asreqt,Asminx)
# # sur appuis
# Asminya = 0.2*max(Asreqa,Asminx)
# print("Asminyt ="+str(Asminyt))
# print("Asminya ="+str(Asminya))
# print("Calcul et choix armatures en travee")
# muu = Mty/(b*d**2*fcd)
# au = 1.0/0.8*(1-(1-2*muu)**0.5)
# yu = au*d 
# zu = d - 0.4*yu
# ro = fyd
# Asreq = Mty/(zu*ro)
# print("Asreq ="+str(Asreq))
# if Asreq<Asminyt:
#     print("===> section minimale requise")
# else:
#     print("===> ")

# print("Calcul et choix armatures sur appuis")
# muu = May/(b*d**2*fcd)
# au = 1.0/0.8*(1-(1-2*muu)**0.5)
# yu = au*d 
# zu = d - 0.4*yu
# ro = fyd
# Asreq = May/(zu*ro)
# print("Asreq ="+str(Asreq))
# if Asreq<Asminya:
#     print("===> section minimale requise")
# else:
#     print("===> ")


# # print("4. Armatures transversales")

# # Crdc = 0.18/1.5
# # vmin = 0.34/1.5*fck**0.5
# # k=min(2,1+(200/(d*1000))**0.5)
# # ro = 







