import math         #importa libreria math
from turtle import *    #modulo que permite el dibujo del grafico
title('Mi corazon')
def hearta(k):     #coordenada x
    return 15*math.sin(k)**3    #calcula el seno de k elevado al cubo y lo multiplica por 15
def heartb(k): #calculos de coordenada de Y y coseno
    return 12*math.cos(k)-5*\
              math.cos(2*k)-2*\
              math.cos(3*k)-\
              math.cos(4*k)
speed(1000) #velocidad
bgcolor('black') #fondo

# Agregar el título
penup()  # Levantar la tortuga para moverla sin dibujar
goto(0, 250)  # Mover la tortuga a la parte superior del dibujo
pendown() # Baja la tortuga para escribir
color('white')  # color del texto
write("Para Elias", align="center", font=("Arial", 20, "bold"))


for i in range (6000):
    goto(hearta(i)*20,heartb(i)*20)
    color('#f73487')
    goto(0,0)

done()

#NOTAS

# #def heartb(k): #calculos de coordenada de Y y coseno
#     return 12*math.cos(k)-5*\     (calcula el coseno de k, y se multiplica por 12)
#               math.cos(2*k)-2*\   (Resta 5 veces el coseno de 2k)
#               math.cos(3*k)-\     (Resta 2 veces el coseno de 3k)
#               math.cos(4*k)       (Final del calculo, resta el coseno de 4k)



# for i in range (6000):              (bucle que se repetira 6000 veces)
#     goto(hearta(i)*20,heartb(i)*20) (movimiento de la posición de turtle X e Y, multiplicado por 20 para el tamaño del corazon)
#     color('#f73487')                (color del corazon)
#     goto(0,0)                       (Movimiendo de regreso a la posición 0;0, para dar efecto de relleno)