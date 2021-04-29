import pygame as pg
import sys
from random import randint, choice

# def rebotaX(x):
#     if x <=0 or x >=ANCHO:
#         return -1
    
#     return 1

# def rebotaY(y):
#     if y <=0 or y >=ALTO:
#         return -1
    
#     return 1

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
newValues = list(range(-10, -4)) + list(range(5, 11))
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx, vy, color, radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

#Meter una funcion que aglutine las funciones rebotaX y rebotaY
    def actualizar(self):
        self.x += self.vx
        self.y += self.vy 

        if self.x <=0 or self.x >=ANCHO:
            self.vx = -self.vx 

        if self.y <=0 or self.y >=ALTO:
            self.vy = -self.vy        

    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio)
        
bolas = []
for _ in range(10):
    bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                choice(newValues),
                choice(newValues),
                (randint(0, 255), randint(0, 255), randint(0, 255)))

    bolas.append(bola)

game_over = False
while not game_over:
    reloj.tick(60)
    #gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    #modificacion de estado 
    for bola in bolas:
        bola.actualizar()
              
    #gestion de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:
        bola.dibujar(pantalla)
        #pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
    
    pg.display.flip()

pg.quit()
sys.exit()
