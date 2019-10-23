import math

a = input ("Parâmryto a: ")
a_int = int(a)
b = input ("parâmetro b: ")
b_int = int (b)
c = input ("parâmetro c: ")
c_int = int (c)

delta = b_int**2 - (4*a_int*c_int)

if (delta == 0):
    raiz = (b_int*(-1))/(2*a_int)
    print("a raíz desta equação é",raiz)
if (delta > 0):
        raiz_1 = (b_int*(-1) + math.sqrt(delta)) /(2*a_int)
        raiz_2 = (b_int*(-1) - math.sqrt(delta)) /(2*a_int)
        print("as raízes desta equação são",raiz_1,"e",raiz_2)
if(delta <0):
            print ("esta equação não possui raízes reais")
