
fck = 25.0
fcd = fck/1.5
fyk = 500.0
fyd = fyk/1.15
fctm = 0.3*(fck)**(2.0/3.0)

a = 0.30
b = 0.40
A = 2.70
B = 2.60
h = 0.65
D = 0.80
qu = 0.50
Ng = 1.00
Nq = 0.20
Cnom = 0.03
phi = 0.01


def foundation((a,b,A,B,h,D,qu,Ng,Nq)):
    list1 = []

    dx = h - Cnom - phi/2
    dy = h - Cnom - phi/2 - phi

    print('1. Materiaux')
    print("fck ="+str(fck))
    print("fcd ="+str(fcd))
    print("fyk ="+str(fyk))
    print("fyd ="+str(fyd))

    print('2. Sollicitations')

    Nu = 1.35*Ng + 1.5*Nq
    print("Nu ="+str(Nu))
    list1.append(Nu)

    print('3. Moment de reference')


    Muy = ((B-0.7*b)**2)/(8*B)*Nu
    Muz = ((A-0.7*a)**2)/(8*A)*Nu
    print("Muy ="+str(Muy))
    print("Muz ="+str(Muz))
    list1.append(Muy)
    list1.append(Muz)

    print('4. Aciers longitudinaux')

    Mu1 = max(Muy,Muz)
    Mu2 = min(Muy,Muz)

    print('4.1 Direction principale')
    # tranche de 1m
    print b
    print dx
    print fcd
    muu = Mu1/(1*dx**2*fcd)
    list1.append(muu)
    print("muu ="+str(muu))
    au = 1.0/0.8*(1-(1-2*muu)**0.5)
    print au
    yu = au*dx 
    print yu
    zu = dx - 0.4*yu
    print zu
    ro = fyd
    Asreqt1 = Mu1/(zu*ro)
    list1.append(Asreqt1*10000)
    print("Asreqt1 ="+str(Asreqt1))

    print('4.2 Direction secondaire')
    # tranche de 1m
    muu = Mu2/(1*dy**2*fcd)
    list1.append(muu)
    print("muu ="+str(muu))
    au = 1.0/0.8*(1-(1-2*muu)**0.5)
    yu = au*dy 
    zu = dy - 0.4*yu
    ro = fyd
    Asreqt2 = Mu2/(zu*ro)
    list1.append(Asreqt2*10000)
    print("Asreqt2 ="+str(Asreqt2))

    print('5. Contrainte sous fondation')

    q = (Ng+Nq)/(A*B)
    print("q ="+str(q))
    print("qu ="+str(qu))
    if q < qu:
        print("ok")
    else:
        print("nok")


    S = A*B
    ro = (Ng+Nq)/S
    list1.append(ro)

    # print list1

    # return Asreqt1,Asreqt2

foundation((a,b,A,B,h,D,qu,Ng,Nq))


# test = ((0.30,0.40,2.70,2.60,0.65,0.80,0.50,1.,0.2),
# (0.30,0.50,2.70,2.60,0.65,0.80,0.60,1.,0.25),
# (0.30,0.60,2.70,2.60,0.65,0.80,0.65,1.,0.2),
# (0.30,0.40,2.70,2.60,0.65,0.80,0.70,1.,0.25),
# (0.30,0.50,2.70,2.60,0.65,0.80,0.50,1.,0.2),
# (0.30,0.60,2.70,2.60,0.65,0.90,0.60,0.8,0.3),
# (0.30,0.40,2.70,2.60,0.65,0.90,0.65,0.8,0.35),
# (0.30,0.50,2.70,2.60,0.65,0.90,0.70,0.8,0.3),
# (0.30,0.60,2.70,2.60,0.65,0.90,0.70,0.8,0.35),
# (0.30,0.40,2.70,2.60,0.65,0.90,0.50,0.8,0.3))
# count = 0
# for i in test:
#     count += 1
#     print(count)
#     foundation(i)



