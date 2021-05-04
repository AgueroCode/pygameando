import pygame as pg
import sys
from random import randint, choice

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx, vy, color, radio=7):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.anchura = radio*2
        self.altura = radio*2

#Meter una funcion que aglutine las funciones rebotaX y rebotaY
    def actualizar(self):
        self.x += self.vx
        self.y += self.vy 

        if self.y <=0:
            self.vy = -self.vy  

        if self.x <=0 or self.x >=ANCHO:
            self.vx = -self.vx 
           
        if self.y >=ALTO:
            self.x = ANCHO // 2
            self.y = ALTO // 2
            self.vx = randint(5, 10)*choice([-1, 1])
            self.vy = randint(5, 10)*choice([-1, 1])
            return True
        return False

    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.anchura//2)

    def comprueba_colision(self, objeto):
        '''
        if self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
           self.x + self.anchura >= objeto.x and self.x + self.anchura <= objeto.x + objeto.anchura:
            choqueX = True
        else:
            choqueX = False      
        '''

        choqueX = self.x >= objeto.x and self.x <= objeto.x+objeto.anchura or \
           self.x+self.anchura >= objeto.x and self.x+self.anchura <= objeto.x + objeto.anchura
        choqueY = self.y >= objeto.y and self.y <= objeto.y+objeto.altura or \
           self.y+self.altura >= objeto.y and self.y+self.altura <= objeto.y + objeto.altura

        if choqueX and choqueY:
            self.vy *= -1
            return True

class Raqueta():
    def __init__(self, x=0, y=0):
        self.altura = 25
        self.anchura = 100
        self.color = (255, 255, 255)
        self.x = (ANCHO - self.anchura) // 2
        self.y = ALTO - self.altura - 15
        self.vy = 0
        self.vx = 7

    def dibujar(self, lienzo):
        rect = pg.Rect(self.x, self.y, self.anchura, self.altura)
        pg.draw.rect(lienzo, self.color, rect)

    def actualizar(self):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT] and self.x < ANCHO - self.anchura:
            self.x += self.vx

vidas = 3
score = 0
font = pg.font.SysFont("Arial", 32)
over_font = pg.font.SysFont("Arial", 64)

def vidasRestantes():
    valor_vidas = font.render("Vidas " + str(vidas), True, (255, 255, 255))
    pantalla.blit(valor_vidas, (10,10))

def puntuacion():
    valor_score = font.render("Score " + str(score), True, (255, 255, 255))
    pantalla.blit(valor_score, (690, 10))

def hasPerdido():
    if vidas == 0:
        se_acabo = over_font.render("GAME OVER", True, (255, 255, 255))
        pantalla.blit(se_acabo, (240, 200)) 

bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                randint(5, 10)*choice([-1, 1]),
                randint(5, 10)*choice([-1, 1]),
                (randint(0, 255), randint(0, 255), randint(0, 255)))

raqueta = Raqueta()

game_over = False
while not game_over and vidas > 0:
    reloj.tick(60)
    #gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True       

    #modificacion de estado 
    raqueta.actualizar()
    pierdebola = bola.actualizar()
    if pierdebola:
        vidas -= 1
    if bola.comprueba_colision(raqueta) == True:
        score += 5
   
    #gestion de la pantalla
    pantalla.fill(NEGRO)
    bola.dibujar(pantalla)
    raqueta.dibujar(pantalla)
    vidasRestantes()
    puntuacion()
    

    pg.display.flip()
    if pierdebola:
        pg.time.delay(500)

pantalla.fill(ROJO)
hasPerdido()
pg.display.flip()
pg.time.delay(1000)   

pg.quit()
sys.exit()
