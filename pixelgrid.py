import pygame
import sys


class PixelGrid:
    def __init__(self, mob):

        # Get color palette
        mob = mob.lower().strip()
        if mob == 'creeper':
            self.palette = {
                'b': (0, 0, 0), 'dg': (70, 121, 46), 'lg': (136, 185, 80)}
        elif mob == 'enderman':
            self.palette = {'b': (0, 0, 0), 'g': (22, 22, 22), 'p': (
                204, 0, 250), 'lp': (224, 121, 250)}
        elif mob == 'skeleton':
            self.palette = {'dg': (97, 97, 97), 'f': (
                133, 133, 133), 'lg': (204, 204, 204), 'ow': (224, 224, 224)}
        elif mob == 'zombie':
            self.palette = {'dg1': (24, 46, 11), 'dg2': (55, 94, 41), 'fg1': (63, 101, 44), 'fg2': (68, 109, 53), 'fg3': (76, 118, 55), 'fg4': (
                60, 103, 49), 'ng1': (90, 122, 72), 'ng2': (105, 134, 86), 'g': (94, 134, 71), 'lg': (103, 140, 73)}
        else:
            raise Exception('not valid mob')

        # Initialize Pygame
        pygame.init()

        # Set the dimensions for the grid
        self.cell_size = 50  # Size of each cells
        self.grid_size = 8  # 8x8 grid
        self.width = self.height = 400  # 8 grids * 50 pixels = 400 pixels

        # Define cells and their colors. (row, column): color
        self.colored_cells = {}

        # Set up the display
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Minecraft Mob/Block Pixel Editor")

    def paint_row(self, row, colors):
        if len(colors) > 8:
            raise Exception("Too many colors in colors list")

        col = 0
        for color in colors:
            self.colored_cells[(row, col)] = self.palette[color]
            col += 1

    def run(self):
        # Main loop
        running = True
        while running:
            # Check for exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background
            white = (255, 255, 255)
            self.screen.fill(white)

            # Draw the grid
            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    rect = pygame.Rect(
                        col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)

                    # Fill certain cells with specific colors
                    if (row, col) in self.colored_cells:
                        pygame.draw.rect(
                            self.screen, self.colored_cells[(row, col)], rect)

                    # Draw the grid cell border
                    black = (0, 0, 0)
                    pygame.draw.rect(self.screen, black, rect, 1)

            # Update the display
            pygame.display.flip()

    # Save image of grid to current directory, name it "screenshot.png"

    def export_grid_as_image(self):
        pygame.image.save(self.screen, "screenshot.png")
