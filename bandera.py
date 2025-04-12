import pygame
import random

# Инициализация pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bandera")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Шрифты
font = pygame.font.Font(None, 36)

# Класс для элементов, которые нужно тапать
class TapItem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

# Группа спрайтов
all_sprites = pygame.sprite.Group()
tap_items = pygame.sprite.Group()

# Создание нескольких элементов
for _ in range(10):
    item = TapItem()
    all_sprites.add(item)
    tap_items.add(item)

# Основной цикл игры
clock = pygame.time.Clock()
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for item in tap_items:
                if item.rect.collidepoint(mouse_pos):
                    score += 1
                    item.reset_position()

    # Обновление экрана
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Отображение счета
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()