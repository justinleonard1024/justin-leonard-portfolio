"""
Duck Hunt
DuckHunt.py
Created by Justin Leonard
"""

import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("arial", 72)
duck_pos = [50, 100, 150, 200, 250, 300, 350]
pygame.mouse.set_visible(False)

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("materials/target.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.value = 0
        self.image = font.render("Score: %d"%self.value, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 375
        self.rect.centery = 550
        
    def update(self):
        self.image = font.render("Score: %d"%self.value, True, (0, 0, 0))
        self.rect.centerx = 375
        self.rect.centery = 550
        
class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("materials/tree.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 254
        self.rect.centery = 314
        
    def update(self):
        self.rect.centerx = 254
        self.rect.centery = 314

class Duck_Right(pygame.sprite.Sprite):
    def __init__(self, loc_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("materials/duck_right.png")
        self.sound = pygame.mixer.Sound("sounds/quack.wav")
        self.rect = self.image.get_rect()
        self.rect.centerx = -200
        self.rect.centery = loc_y
        self.speed = speed
        self.time = 0
        self.setTime = False
        self.isCollided = False

    def reset(self):
        self.image = pygame.image.load("materials/duck_right.png")
        self.setTime = False
        self.time = 0
        
        reset_loc_y = random.choice(duck_pos)
        reset_speed = random.randint(5,20)

        self.rect.centerx = -200
        self.rect.centery = reset_loc_y
        self.speed = reset_speed

    def hit(self):
        self.sound.play()
        self.image = pygame.image.load("materials/duck_killed.png")
        self.setTime = True
        
    def update(self):
        if self.rect.right >= screen.get_width() + 100:
            self.reset()

        if self.setTime:
            self.isCollided = False
            self.time += 1
        else:
            self.rect.centerx += self.speed

        if self.time == 15:
            self.reset()

class Duck_Left(pygame.sprite.Sprite):
    def __init__(self, loc_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("materials/duck_left.png")
        self.sound = pygame.mixer.Sound("sounds/quack.wav")
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.centery = loc_y
        self.speed = speed
        self.time = 0
        self.setTime = False
        self.isCollided = False

    def reset(self):
        self.image = pygame.image.load("materials/duck_left.png")
        self.setTime = False
        self.time = 0
        
        reset_loc_y = random.choice(duck_pos)
        reset_speed = random.randint(5,20)

        self.rect.centerx = 1000
        self.rect.centery = reset_loc_y
        self.speed = reset_speed

    def hit(self):
        self.sound.play()
        self.image = pygame.image.load("materials/duck_killed.png")
        self.setTime = True
        
    def update(self):
        if self.rect.left <= -100:
            self.reset()

        if self.setTime:
            self.isCollided = False
            self.time += 1
        else:
            self.rect.centerx -= self.speed

        if self.time == 15:
            self.reset()



def main():
    pygame.display.set_caption("Duck Hunt")
    
    background = pygame.image.load("materials/background.png")
    screen.blit(background, (0,0))
    
    crosshair = Crosshair()
    score = Score()
    tree = Tree()
    
    UISprites = pygame.sprite.Group(crosshair,score)
    backgroundSprites = pygame.sprite.Group(tree)
    
    ducks = []
    for i in range(3):
        loc_y = random.choice(duck_pos)
        speed = random.randint(5,20)
        duck = Duck_Right(loc_y, speed)
        ducks.append(duck)
        
    for i in range(3):
        loc_y = random.choice(duck_pos)
        speed = random.randint(5,20)
        duck = Duck_Left(loc_y, speed)
        ducks.append(duck)
        
    entitySprites = pygame.sprite.Group(ducks)

    
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if not((pos[0] >= 194 and pos[0] <= 314) and (pos[1] >= 194 and pos[1] <= 445)):
                    for duck in ducks:
                        if duck.isCollided == True:
                            duck.hit()
                            score.value += 1

        collided_ducks = pygame.sprite.spritecollide(crosshair, entitySprites, False)
        for duck in collided_ducks:
            duck.isCollided = True
            
        for duck in ducks:
            if duck not in collided_ducks:
                duck.isCollided = False
        
        entitySprites.clear(screen, background)
        backgroundSprites.clear(screen, background)
        UISprites.clear(screen, background)

        entitySprites.update()
        backgroundSprites.update()
        UISprites.update()
        
        entitySprites.draw(screen)
        backgroundSprites.draw(screen)
        UISprites.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
