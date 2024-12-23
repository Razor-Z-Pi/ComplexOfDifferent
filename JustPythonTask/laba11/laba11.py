import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определяем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Илюстрация на pygame!!!')

# Определяем цвета
sky_blue = (135, 206, 235)
green = (34, 139, 34)
brown = (139, 69, 19)
yellow = (255, 255, 0)

# Функция для рисования дерева
def draw_tree(x, y):
    # Рисуем ствол
    pygame.draw.rect(screen, brown, (x, y, 20, 60))
    # Рисуем крону
    pygame.draw.circle(screen, green, (x + 10, y - 20), 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливаем фон
    screen.fill(sky_blue)

    # Рисуем землю
    pygame.draw.rect(screen, yellow, (0, 500, width, 100))

    # Рисуем деревья
    for i in range(3):
        draw_tree(100 + i * 200, 440)

    # Обновляем экран
    pygame.display.flip()

# Завершаем Pygame
pygame.quit()
sys.exit()