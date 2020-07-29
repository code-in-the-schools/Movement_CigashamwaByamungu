import pygame
import os

img_path = os.path.join(' RedPacman.png')

class person (object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)


    person.image = pygame.image.load
    (' RedPacman.png')
    self.image = person.image
    self.image = pygame.transform.scale(self.image(50,50))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x, self.y, 55, 55)

def draw(self, surface):
  surface.blit(self.image,(self.x, self.y))


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite = person()
clock = pygame.time.clock()

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill(255, 255, 255)
  Sprite.draw(screen)
  pygame. display.update()

  clock.tick(60)

