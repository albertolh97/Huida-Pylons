import random
import time

#Para generar la cuadrícula completa
def Mapa(r,c): 
    mapa = []
    for i in range(1,r+1):
        for j in range(1,c+1):
            mapa.append((i,j))
    return mapa

def Huida(r,c):
    mapa = Mapa(r,c)
    posible = True  #Debe cambiar cuando el problema es imposible
    
    start = time.time()
    while posible: 
        origen = random.choice(mapa) #Fija el primer punto
        print ('origen'+str(origen))
        usado = []  #Se usará para almacenar los puntos en los que ya hemos estado
        usado.append(origen)
        intento = True #Cambia cuando vayamos a probar con otro origen
        
        while intento:
            r1 = usado[-1] [0]
            c1 = usado[-1] [1]
            opciones=[]
            for r in range(1,r+1):
                for c in range(1,c+1):
                    if r==r1 or c==c1 or r-c==r1-c1 or r+c==r1+c1:
                        continue
                    if (r,c) in usado:
                        continue
                    else:
                        opciones.append((r,c))
            print ('opciones'+str(opciones))
            if opciones == []:
                intento = False
            if opciones != []:
                a = random.choice(opciones)
                usado.append(a)
                print ('usado'+str(usado))
            if len(usado) == len(mapa):
                print ('Y = POSSIBLE')
                return 'L = ' + str(usado)
        
        end = time.time()
        if (end-start)>10:
            return 'IMPOSSIBLE'
            
print (Huida(3,3))            
    

    