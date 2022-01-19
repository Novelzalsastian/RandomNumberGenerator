print('           KALKULATOR RNG                  ')
print('-------------------------------------------')
print('           Pilihan Cara                    ')
print('1. Linear Congruental Random Number Generator')
print('2. Multiplicative Random Number Generator')
print('3. Mixed Congruental Random Number Generator')
print('--------------------------------------------')
print("")
#Import 
import math
i=0
#OUTPUT
print('--------------------------------------------')
print('         Input Pilihan Cara RNG             ')
print('--------------------------------------------')
a=float(input('Masukkan Nilai a :  '))
m=float(input('Masukkan Nilai m :  '))
n=float(input('Masukkan Nilai n :  '))
Z0=float(input('Masukkan Nilai Z0 : '))
Zi=Z0
c=float(input('Masukkan Nilai c : '))
option= int(input('Masukkan Pilihan :  '))
print('--------------------------------------------')
print("")

if option == 1:
    print('')
    print('--------------------------------------------------')
    print('          LINEAR CONGRUENT GENERATOR              ')
    print('--------------------------------------------------')
    print('              Zi=(a*Zi-1+c)mod m                  ')
    print('         a= ',a,'Z0= ',Z0,'m= ',m,'c= ',c          )
    print("+---------------+---------------+---------------+---------------+---------------+")
    print("|\ti\t|\tZi\t|\tZi+1\t|\tUi\t|\tUi+1\t|")
    print("+---------------+---------------+---------------+---------------+---------------+")

    while i<25:
        Z0=Zi
        #Zi
        Zi=(a * Zi + c)%m
        #Ui
        U=float(Zi/m)
        fU= '{:.4f}'.format(U)
        #Zi+1
        Z1= int(a * Zi + c)%m
        #Ui+1
        U1= Z1/m
        fU1= '{:.4f}'.format(U1)
        i=i+1
        print("|\t",i,"\t|",Zi,"\t|",Z1,"\t|",fU,"\t|",fU1,"\t|")
        print("+---------------+---------------+---------------+---------------+---------------+")

if option == 2:
    print('')
    print('--------------------------------------------------')
    print('          MULTIPLICATIVE RANDOM GENERATOR              ')
    print('--------------------------------------------------')
    print('              Zi=(a*Zi-1+c)mod m                  ')
    print('         a= ',a,'Z0= ',Z0,'m= ',m         )
    print("+---------------+---------------+---------------+---------------+---------------+")
    print("|\ti\t|\tZi\t|\tZi+1\t|\tUi\t|\tUi+1\t|")
    print("+---------------+---------------+---------------+---------------+---------------+")

    while i<25:
        Z0=Zi
        #Zi
        Zi=(a * Zi )%m
        #Ui
        U=float(Zi/m)
        fU= '{:.4f}'.format(U)
        #Zi+1
        Z1= int(a * Zi )%m
        #Ui+1
        U1= Z1/m
        fU1= '{:.4f}'.format(U1)
        i=i+1
        print("|\t",i,"\t|",Zi,"\t|",Z1,"\t|",fU,"\t|",fU1,"\t|")
        print("+---------------+---------------+---------------+---------------+---------------+")

if option == 3:
        print('')
        print('--------------------------------------------------')
        print('          MULTIPLICATIVE RANDOM GENERATOR              ')
        print('--------------------------------------------------')
        print('              Zi=(a*Zi)mod m                  ')
        print('         a= ',a,'Z0= ',Z0,'n= ',n, 'c =',c         )
        print("+---------------+---------------+---------------+---------------+---------------+")
        print("|\ti\t|\tZi\t|\tZi+1\t|\tUi\t|\tUi+1\t|")
        print("+---------------+---------------+---------------+---------------+---------------+")

        while i<25:
            Z0=Zi
            #Zi
            Zi=((a**n * Zi ) + (a**n - 1 / a - 1)*c)%m
            #Ui
            U=float(Zi/m)
            fU= '{:.4f}'.format(U)
            #Zi+1
            Z1= int((a**n * Zi ) + (a**n - 1 / a - 1)*c)%m
            #Ui+1
            U1= Z1/m
            fU1= '{:.4f}'.format(U1)
            i=i+1
            print("|\t",i,"\t|",Zi,"\t|",Z1,"\t|",fU,"\t|",fU1,"\t|")
            print("+---------------+---------------+---------------+---------------+---------------+")

if option == 4:
   exit()





