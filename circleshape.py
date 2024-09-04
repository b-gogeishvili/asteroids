import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, obj):
        distance = self._calculate_distance(obj)

        if distance <= (self.radius + obj.radius):
            return True
        else:
            return False

    # Formula for calculating distance between two points
    # sqrt( [(x2 - x1)^2] + [(y2 - y1)^2] )
    def _calculate_distance(self, obj):
        x = pow(
            (obj.position.x - self.position.x),
            2
        )

        y = pow(
            (obj.position.y - self.position.y),
            2
        )

        return pow(
            (x + y),
            0.5
        )
