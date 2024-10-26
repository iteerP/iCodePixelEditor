import pygame
import sys
from pixelgrid import PixelGrid


def main():
    grid = PixelGrid('creeper')  # instance of pixel editor grid

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    # ADD COLORS TO PIXEL EDITOR GRID

    # Row 0
    grid.paint_row(0, ['lg', 'dg', 'dg', 'lg', 'lg', 'lg', 'lg', 'dg'])

    # Row 1
    grid.paint_row(1, ['dg', 'dg', 'dg', 'dg', 'dg', 'lg', 'dg', 'lg'])

    # Row 2
    grid.paint_row(2, ['dg', 'b', 'b', 'lg', 'dg', 'b', 'b', 'lg'])

    # Row 3
    grid.paint_row(3, ['dg', 'b', 'b', 'dg', 'dg', 'b', 'b', 'lg'])

    # Row 4
    grid.paint_row(4, ['lg', 'dg', 'dg', 'b', 'b', 'lg', 'dg', 'dg'])

    # Row 5
    grid.paint_row(5, ['lg', 'dg', 'b', 'b', 'b', 'b', 'dg', 'lg'])

    # Row 6
    grid.paint_row(6, ['lg', 'dg', 'b', 'b', 'b', 'b', 'dg', 'dg'])

    # Row 7
    grid.paint_row(7, ['dg', 'lg', 'b', 'dg', 'dg', 'b', 'dg', 'dg'])

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    grid.run()  # run pixel editor

    # save image of pixel grid to project directory
    grid.export_grid_as_image()


if __name__ == '__main__':
    main()

    # Quit Pygame
    pygame.quit()
    sys.exit()
