import random #importamos random
from turtle import * #importamos turtle
from random import randrange #importamos un paquete espeficico de random
from freegames import square, vector #importamos dos paquetes especificos de free games.

food = vector(0, 0) #Definimos la pocicion inicial e la que se encontrara la comida.
snake = [vector(10, 0)] # definimos la posicion inicial donde comenzara la víbora.
aim = vector(0, -10)

#Definimos un arreglo de colores para la serpiente y para la comida, respectivamente.
coloresSerp = ["blue","black","brown","yellow","green","orange","beige","turquoise","pink"]
#Con ayuda del random choice, se va a seleccuionar un color random del arreglo.
colorrandomS = random.choice(coloresSerp)
#Se hace el mismo proceso de arriba.
coloresCom = ["blue","black","brown","yellow","green","orange","beige","turquoise","pink"]
colorrandomC = random.choice(coloresCom)

def change(x, y): #Definimos el cambio de posicion de la serpiente en x,y.
    "Change snake direction."
    aim.x = x #Cambia en x
    aim.y = y #Cambia en y

def inside(head): #definimos que cuando la cabeza se encuentre adentro de los limites, seguimos jugando.
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move(): #Definimos como se va a mover la serpiente.
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim) #Solo se mueve la cabeza, el cuerpo solo sigue el movimiento.

    if not inside(head) or head in snake: #Cuando 'topemos' con una pared, o contra el cuerpo, se va  apara el programa
        square(head.x, head.y, 9, 'red') #Se va a poner la cabeza roja por el choque.
        update()
        return

    snake.append(head)

    if head == food: #Cuando estemos en la posicion donde este la comida, quiere decir que la agarramos.
        print('Snake:', len(snake)) #Imprime cuantas 'comidas' hemos comido, osea cuanto mide la serpiente
        food.x = randrange(-15, 15) * 10 #Aparece en un lugar random dentro del marco
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0) #Si no, no pasa nada y no ganamos nada.

    clear()
    
    for body in snake: #Definimos el ciclo de la serpiente.
        square(body.x, body.y, 9, colorrandomS)

    square(food.x, food.y, 9, colorrandomC) #Definimos el ciclo de la comida.
    update() #Se sigue actualizando.
    ontimer(move, 100)

setup(420, 420, 370, 0) #Medida de nuestra pantalla.
hideturtle() #Escondemos la tortuga.
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