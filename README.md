Minecraft Mob Pixel Editor
A Python-based pixel art editor for creating 8x8 Minecraft mob sprites using Pygame. This tool allows you to create pixel art representations of various Minecraft mobs with their authentic color palettes.
Features

8x8 Pixel Grid: Perfect for creating classic Minecraft mob sprites
Pre-defined Color Palettes: Authentic Minecraft mob colors for:

Creeper (green tones)
Enderman (dark with purple eyes)
Skeleton (grayscale tones)
Zombie (various green flesh tones)


Interactive Display: Real-time visualization of your pixel art
Image Export: Save your creations as PNG files

Requirements

Python 3.x
Pygame library

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install pygame
   ```

## Usage

### Basic Usage

Run the main script to create a Creeper sprite:
```bash
python main.py
```

### Creating Custom Sprites

To create your own mob sprite, modify the `main.py` file:

```python
from pixelgrid import PixelGrid

# Create a new pixel grid for your chosen mob
grid = PixelGrid('creeper')  # Options: 'creeper', 'enderman', 'skeleton', 'zombie'

# Paint each row (0-7) with colors from the mob's palette
grid.paint_row(0, ['lg', 'dg', 'dg', 'lg', 'lg', 'lg', 'lg', 'dg'])
grid.paint_row(1, ['dg', 'dg', 'dg', 'dg', 'dg', 'lg', 'dg', 'lg'])
# ... continue for all 8 rows

# Display the grid and export as image
grid.run()
grid.export_grid_as_image()
```

### Color Palette Reference

#### Creeper
- `b` - Black (0, 0, 0)
- `dg` - Dark Green (70, 121, 46)
- `lg` - Light Green (136, 185, 80)

#### Enderman
- `b` - Black (0, 0, 0)
- `g` - Gray (22, 22, 22)
- `p` - Purple (204, 0, 250)
- `lp` - Light Purple (224, 121, 250)

#### Skeleton
- `dg1` - Dark Gray 1 (97, 97, 97)
- `dg2` - Dark Gray 2 (133, 133, 133)
- `g` - Gray (189, 189, 189)
- `lg` - Light Gray (204, 204, 204)
- `ow` - Off White (224, 224, 224)

#### Zombie
- `dg1` - Dark Green 1 (24, 46, 11)
- `dg2` - Dark Green 2 (55, 94, 41)
- `fg1` - Flesh Green 1 (63, 101, 44)
- `fg2` - Flesh Green 2 (68, 109, 53)
- `fg3` - Flesh Green 3 (76, 118, 55)
- `fg4` - Flesh Green 4 (60, 103, 49)
- `ng1` - Natural Green 1 (90, 122, 72)
- `ng2` - Natural Green 2 (105, 134, 86)
- `g` - Green (94, 134, 71)
- `lg` - Light Green (103, 140, 73)

## How It Works

1. **PixelGrid Class**: Manages the pixel grid, color palettes, and rendering
2. **Color Mapping**: Each mob has a predefined color palette with shorthand codes
3. **Row Painting**: Use `paint_row()` to color each row with a list of color codes
5. **Export Function**: Save your creation as a PNG image

## License

This project is for educational purposes. Minecraft is a trademark of Mojang Studios.
