import math

import pygame

# Game Variables
WIDTH, HEIGHT = 800, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
IMAGES = []

hangman_status = 4

RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400


def initialize(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    A = 65
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman Game by Luigi")
    for i in range(7):
        IMAGES.append(pygame.image.load("images/hangman" + str(i) + ".png"))

    for i in range(26):
        x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = start_y + ((i // 13) * (GAP + RADIUS * 2))
        pos = (x, y)
        letters.append([pos, chr(A + i), True])

    print(IMAGES)
    return win


def draw(window):
    window.fill(WHITE)
    letter_font = pygame.font.SysFont('comicsans', 40)
    for ltr in letters:
        if ltr[2]:
            pygame.draw.circle(window, BLACK, ltr[0], RADIUS, 2)
            text = letter_font.render(ltr[1], 1, BLACK)
            ltr_x = ltr[0][0] - text.get_width() / 2
            ltr_y = ltr[0][1] - text.get_height() / 2
            window.blit(text, (ltr_x, ltr_y))

    window.blit(IMAGES[hangman_status], (150, 100))
    pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = initialize('PyCharm')
    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)
        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    if letter[2]:
                        pos_x, pos_y = letter[0]
                        dis = math.sqrt((pos_x - m_x) ** 2 + (pos_y - m_y) ** 2)
                        if dis < RADIUS:
                            print(letter[1])
                            letter[2] = False
            elif event.type == pygame.MOUSEMOTION:
                print(pygame.mouse.get_pos())

    pygame.quit()
    print(f'Gamem over mai fren....')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
