import turtle

# t = turtle.turtles()

turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.backward(100)
turtle.right(50)
turtle.forward(90)


# Escalier

turtle.left(100)
turtle.forward(250)
turtle.right(50)

# Fonction Escalier
def escalier(taille, nb):
    for i in range(0, 5):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        
escalier(50, 10)


# Carré
def carre(taille):
    for i in range(0, 4):
        turtle.forward(taille)
        turtle.left(90)


carre(90)

turtle.right(180) 
turtle.forward(200)       
        
def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)
        
carres(10, 15)                
        
turtle.done()