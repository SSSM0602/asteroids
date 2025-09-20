import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        self.rotation = 0
        self.timer = 0
        super().__init__(x, y, PLAYER_RADIUS)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = "white"
        points = self.triangle()
        width = 2
        pygame.draw.polygon(screen, color, points, width)

    def rotate(self, dt):
        rotate_amount = PLAYER_TURN_SPEED * dt
        self.rotation += rotate_amount

    def shoot(self):
        bullet = Shot(self.position[0], self.position[1])
        bullet.velocity = pygame.Vector2(0,1)
        bullet.velocity.rotate_ip(self.rotation)
        bullet.velocity *= PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
