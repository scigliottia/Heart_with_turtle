import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()

import turtle
import tkinter as tk

obj = turtle.Turtle() # Person
obj_2 = turtle.Turtle() # Heart
obj_3 = turtle.Turtle() # Person's face
obj_4 = turtle.Turtle() # Cheeks

factor = 4.1

turtle.title("Amor")

obj.penup()
obj.pencolor("black")
obj.color("black")
obj.pensize(8)

obj_2.penup()
obj_2.pencolor("black")
obj_2.color(198/256,3/256,3/256)
obj_2.pensize(8)
obj_2.hideturtle()

obj_3.penup()
obj_3.pencolor("black")
obj_3.color("black")
obj_3.pensize(5)
obj_3.hideturtle()

obj_4.penup()
obj_4.pencolor("black") 
obj_4.color(255/256,226/256,255/256)
obj_4.pensize(5)
obj_4.hideturtle()


# Person's functions

def first_function(x):
    y =  2.5021812172264*x**(4) + 593.2511403404627*x**(3) + 52739.95931846504*x**(2) + 2083586.6509372194*x + 30865279.032676205   
    obj.goto(x*factor,y*factor)
    obj.pendown()

def second_function(x):
    y =  0.0007015327859*x**(4) + 0.1747691614323*x**(3) + 16.3651641179543*x**(2) + 681.8020200255914*x + 10633.705210436008
    obj.goto(x*factor,y*factor)

def third_function(x):
    y = -0.0000000102245*x**(8) - 0.0000044640578*x**(7) - 0.0008480020013*x**(6) - 0.0915312058422*x**(5) - 6.1392321057998*x**(4) - 261.9921579607785*x**(3) - 6946.3762389142785*x**(2) - 104612.74690302706*x-685112.3862450566
    obj.goto(x*factor,y*factor)

def fourth_function(x):
    y =  -0.0003056827006*x**(5) - 0.0532509079348*x**(4) - 3.7032517050469*x**(3) - 128.5748794178308*x**(2) - 2230.8256755824887*x - 15478.418160332889
    obj.goto(x*factor,y*factor)

def fifth_function(x):
    y = 0.0004345888728*x**(5) + 0.0765174532448*x**(4) + 5.3702820577545*x**(3) + 187.8259281015579*x**(2) + 3275.0259115502877*x+22776.558
    obj.goto(x*factor,y*factor)

def sixth_function(x):
    y = -0.0003281259387*x**(5) - 0.0399654323483*x**(4) - 1.9340841277278*x**(3) - 46.5360299708716*x**(2) - 557.0219229911525*x-2660.880441443968
    obj.goto(x*factor,y*factor)

def seventh_function(x):
    y = 0.0005105930399*x**(4) + 0.0522197260046*x**(3) + 1.9862179448856*x**(2) + 34.2617555739815*x + 211.4635551481368
    obj.goto(x*factor,y*factor)

def eighth_function(x):
    y =  0.5047349563217*x**(4) + 60.4827974503076*x**(3) + 2717.716443796219*x**(2) + 54276.04712002286*x + 406487.07188638893
    obj.goto(x*factor,y*factor)

def nineth_function(x):
    y =-0.0052625889719*x**(3) - 0.3336473923801*x**(2) - 6.0180350157965*x - 49.0024551387247
    obj.goto(x*factor,y*factor)

obj.hideturtle()


# Person's face:
    
def face_1(x):
    y = 0.0006429420849*x**(5) + 0.160607516614* x **(4) + 16.0429348498521*x**(3) + 801.2104872098886*x**(2) + 20009.781509482225*x + 199957.3979831118
    obj_3.goto(x*factor, y*factor)
    obj_3.pendown()

def face_2(x):
    y = -0.0021236302739*x**(4) - 0.4100624978897*x**(3) - 29.6883671996797*x**(2) - 955.0134580459352*x - 11508.013394253592
    obj_3.goto(x*factor, y*factor)


# Cheeks:
    
def checks(i, j):
    obj_4.begin_fill()
    obj_4.showturtle()
    obj_4.goto(i*factor,j*factor)
    obj_4.pendown()
    obj_4.circle(15,360)
    obj_4.end_fill()
    obj_4.penup()

# Heart's functions:

def heart_function_1(x):
    y = 0.0000000016994*x**(7) + 0.0000002209265*x**(6) + 0.0000098569046*x**(5) + 0.0001556394755*x**(4) - 0.0002410947046*x**(3)-0.0396705070925*x**(2) - 1.1273929586208*x + 40.283204318965
    obj_2.goto(x*factor,y*factor)
    obj_2.pendown()

def heart_function_2(x):
    y = 0.0000003384294*x**(5) - 0.0001159212915*x**(4) + 0.0116575224976*x**(3) - 0.5294781049538*x**(2) + 11.7105567784198*x - 28.0840973295469
    obj_2.goto(x*factor,y*factor)

def heart_function_3(x):
    y = 0.0000002579278*x**(5) + 0.0001360403252*x**(4) - 0.0262284201279*x**(3) + 1.6319312124695*x**(2) - 40.5165483150624*x + 290.1601721510131
    obj_2.goto(x*factor,y*factor)

def heart_function_4(x):
    y =-0.0000000733879*x**(5) + 0.0000033788618*x**(4) - 0.0000384823752*x**(3) + 0.0008231822299*x**(2) - 0.4823499449742*x - 30.4304017196549
    obj_2.goto(x*factor,y*factor)


# Shape of the person

def shape_of_the_person():
    for i in range(-61,-58):
        first_function(i)

    for i in range(-58,-71,-1):
        second_function(i)

    for i in range(-71,-39):
        third_function(i)

    for i in range(-39,-27):
        fourth_function(i)

    for i in range(-27,-42,-1):
        fifth_function(i)

    for i in range(-31,-17):
        sixth_function(i)

    for i in range(-17,-32,-1):
        seventh_function(i)

    for i in range(-28,-31,-1):
        eighth_function(i)

    for i in range(-28,-20):
        nineth_function(i)
    

    # face:

    for i in range(-51,-44):
        face_1(i)

    for i in range(-51,-44):
        face_2(i)

    # Cheeks:

    checks(-40,6)
    checks(-56,4)

    obj_4.hideturtle()

    # Eyes
        
    obj_3.showturtle()

    obj_3.penup()
    obj_3.goto(-55*factor,12*factor)
    obj_3.pendown()
    obj_3.forward(1)

    obj_3.penup()
    obj_3.goto(-42*factor,14*factor)
    obj_3.pendown()
    obj_3.forward(1)

    obj_3.hideturtle()

shape_of_the_person() ####################################################################


# Heart shape:

obj_2.showturtle()

def heart_shape():

    for i in range(-54,7):
        heart_function_1(i)

    for i in range(7,61):
        heart_function_2(i)

    for i in range(61,31,-1):
        heart_function_3(i)

    for i in range(31,-22,-1):
        heart_function_4(i)
    
    obj_2.hideturtle()

heart_shape() ####################################################################


# Message

obj.penup()
obj.color("deep pink")
obj.goto(80, 0)
obj.write("¿Te gustó? \n❤️", align = "center", font = ("Impact", 25, "normal")) 

# Checkbox

def toggle_checkbox():

    if var.get() == 1:
        pass

    else:

        obj.penup()
        obj.goto(50,-60)
        obj.write("Me alegra mucho que te haya gustado:3 ", align = "center", font = ("Arial", 11, "bold")) 
        # Secret message

        turtle.delay(200)
        obj.color("gray")
        obj.penup()
        obj.goto(0,-250)
        obj.write("Te amo mucho Elias<3 ", align = "center", font = ("Arial", 9, "bold")) 

root = tk.Tk()
width = 250
height = 50
root.geometry(f"{width}x{height}")

root.title("¿Aceptarías?")

var = tk.IntVar()

checkbox = tk.Checkbutton(root, text="Sí", variable=var, command=toggle_checkbox)
checkbox.pack()


# Close

turtle.done()
