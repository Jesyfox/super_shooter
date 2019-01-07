class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.rect.move(0, height)

    def move(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.y > 450:
            self.rect.y = 0
            self.rect.x += self.rect.width
