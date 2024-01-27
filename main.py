# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame
from pygame import Surface, Color

from tests import file_to_rows


def fill_surface(surf):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        rows = file_to_rows(name)
        for y, row in enumerate(rows):
            true_y = 127 - y
            for x,z in enumerate(row):
                if z > 128:
                    print("red", 2*x+1, 2*y+1, z)
                    color = Color(255, 0, 0)
                else:
                    color = Color(2*z, 2*z, 2*z)
                # color = Color(255, 255, 255)
                for dx in range(4):
                    for dy in range(4):
                        surf.set_at((4*x+dx, 4*true_y+dy), color)


def run_pygame():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    surf = Surface((512, 512))
    fill_surface(surf)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("darkblue")
        screen.blit(surf, (200, 20))

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    run_pygame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
