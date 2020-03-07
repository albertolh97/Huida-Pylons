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
    
    start = time.time() #Se comienza a medir el tiempo de ejecución del bucle
    while True: 
        origen = random.choice(mapa) #Fija el primer punto
        usado = []  #Se usará para almacenar los puntos en los que ya hemos estado
        usado.append(origen)
        intento = True #Cambia cuando vayamos a probar con otro origen
        
        while intento:
            r1 = usado[-1] [0] #Representa el valor de la fila de la última cuadrícula escogida
            c1 = usado[-1] [1] #Representa el valor de la columna de la última cuadrícula escogida
            opciones=[] #Aquí se almacenan las posibles cuadrículas a las que te puedes trasladar en cada momento
            for r in range(1,r+1):
                for c in range(1,c+1):
                    if r==r1 or c==c1 or r-c==r1-c1 or r+c==r1+c1: #Asegura que se cumplan las condiciones impuestas por el problema
                        continue
                    if (r,c) in usado: #Asegura que no se utilice la misma cuadrícula dos veces
                        continue
                    else:
                        opciones.append((r,c))
            if opciones == []: #En este caso ninguna cuadrícula era posible por lo que es necesario cambiar el origen y probar de nuevo
                intento = False
            if opciones != []: #Se elige una opción aleatoria dentro de las cuadrículas posibles
                a = random.choice(opciones)
                usado.append(a)
            if len(usado) == len(mapa): #Si esto se cumple se puede decir que hemos estado en todas las cuadrículas una vez
                print ('Y = POSSIBLE')
                return 'L = ' + str(usado)
        
        #Si el tiempo necesario para encontrar una solución es mayor de 10 segundos se asume que no existe 
        #(se debería aumentar el valor en caso de que la cuadrícula escogida fuera muy grande) 
        end = time.time()
        if (end-start)>10: 
            return 'IMPOSSIBLE'
            
print (Huida(3,5))            
    

    