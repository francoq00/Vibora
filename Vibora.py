#importamos random
import random
#importamos turtle
from turtle import *
#importamos un paquete espeficico de random
from random import randrange
#importamos dos paquetes especificos de free games.
from freegames import square, vector

#Definimos la pocicion inicial e la que se encontrara la comida.
food = vector(0, 0)
# definimos la posicion inicial donde comenzara la víbora.
snake = [vector(10, 0)]
aim = vector(0, -10)

#Definimos un arreglo de colores para la serpiente y para la comida, respectivamente.
coloresSerp = ["blue","black","brown","yellow","green","orange","beige","turquoise","pink"]
#Con ayuda del random choice, se va a seleccuionar un color random del arreglo.
colorrandomS = random.choice(coloresSerp)
#Se hace el mismo proceso de arriba.
coloresCom = ["blue","black","brown","yellow","green","orange","beige","turquoise","pink"]
colorrandomC = random.choice(coloresCom)

#Definimos el ciclo aleatorio de la comida.
#No supimos como hacerlo.
#def foodRand():
    #val = random.randrange(1,5)
    #if val == 1:
        #if food.x <= -150:
            #food.x +=10 
    #elif val == 2:
        #if food.x >= 150:
            #food.x -=10
    #elif val == 3:
        #if food.y <= -150:
            #food.y += 10
    #elif val == 4:
        #if food.y >= 150:
            #food.y -= 10

#Definimos el cambio de posicion de la serpiente en x,y.
def change(x, y):
    "Change snake direction."
    #Cambia en x
    aim.x = x
    #Cambia en y
    aim.y = y

#definimos que cuando la cabeza se encuentre adentro de los limites, seguimos jugando.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Definimos como se va a mover la serpiente.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    #Solo se mueve la cabeza, el cuerpo solo sigue el movimiento.
    head.move(aim)
    
    #Cuando 'topemos' con una pared, o contra el cuerpo, se va a parar el programa.
    if not inside(head) or head in snake:
        #Se va a poner la cabeza roja por el choque.
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Cuando estemos en la posicion donde este la comida, quiere decir que la agarramos.
    if head == food:
        #Imprime cuantas 'comidas' hemos comido, osea cuanto mide la serpiente.
        print('Snake:', len(snake))
        #Aparece la comida en un lugar random dentro del marco.
        food.x = randrange(-15, 15) * 10 
        food.y = randrange(-15, 15) * 10
    else:
        #Si no, no pasa nada y no ganamos nada.
        snake.pop(0)
    clear()
    
    #Definimos el ciclo de la serpiente.
    for body in snake:
        square(body.x, body.y, 9, colorrandomS)
    #Se sigue actualizando.
    square(food.x, food.y, 9, colorrandomC)
    update()
    ontimer(move, 100)
               
#Medida de nuestra pantalla.
setup(420, 420, 370, 0)
#Escondemos la forma de tortuga.
hideturtle()
tracer(False)
listen()
#Definimos lo que pasara cuando teclemos ciertas teclas
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Se mueve y el programa empieza a correr.
move()
done()