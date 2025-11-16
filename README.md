# Image Grainer

A Python tool that converts your latest holiday pictures into stipple/dot-density art using grayscale brightness values.

## Overview

**Image Grainer** takes an input image and generates a dot-density representation where:
- **Dark areas** → many dots
- **Bright areas** → few or no dots

This creates an artistic, hand-drawn stipple effect reminiscent of pointillism and engraving techniques.

## Features

- Adjustable dot size and density
- Customizable dot and background colors
- Image resizing for density control
- Jitter for natural, organic dot placement
- PNG output with descriptive filename encoding parameters

## Installation

Install dependencies using:
```bash
pip install -r requirements.txt
```

### Requirements
- Python 3.7+
- Pillow (PIL) — image processing
- NumPy — array operations

## Usage

### Basic Example

```python
from skyline import image_to_dot_density

image_to_dot_density(
    input_path="your_image.jpg",
    output_name="output_name",
    dot_color=(0, 0, 0),           # Black dots
    background_color=(255, 255, 255),  # White background
    resize_to=(300, 200),          # Resize for density control
    max_dots_per_pixel=8,          # Max dots per pixel
    dot_radius=1,                  # Dot size in pixels
    jitter=0.4                     # Randomness in dot placement (0-1)
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_path` | str | — | Path to the input image |
| `output_name` | str | — | Base name for the output file (parameters will be appended) |
| `dot_color` | tuple | (0, 0, 0) | RGB tuple for dot color |
| `background_color` | tuple | (255, 255, 255) | RGB tuple for background color |
| `resize_to` | tuple | (300, 200) | Resize image to (width, height); None to skip |
| `max_dots_per_pixel` | float | 8 | Maximum dots per pixel in darkest areas |
| `dot_radius` | float | 1 | Radius of each dot in pixels |
| `jitter` | float | 0.4 | Randomness in dot placement (0 = no jitter, 1 = ±1 pixel) |

### Output

The output filename encodes all parameters:
```
{output_name}_{R}-{G}-{B}_{width}-{height}_{max_dots}_{radius}_{jitter}.png
```

**Example:**
```
skyline_berlin_dots_50-50-255_3000-2000_2.5_0.05_1.png
```

## Example Usage

```python
image_to_dot_density(
    input_path="skyline_berlin.jpeg",
    output_name="skyline_berlin_dots",
    dot_color=(50, 50, 255),      # Blue dots
    resize_to=(3000, 2000),        # High resolution
    max_dots_per_pixel=2.5,
    dot_radius=0.05,
    jitter=1
)
```

## Tips for Best Results

- **For detailed images:** Use smaller `dot_radius` and higher `resize_to` dimensions
- **For artistic effect:** Increase `jitter` for more organic placement
- **For density control:** Adjust `max_dots_per_pixel` and `resize_to`
- **For color:** Experiment with `dot_color` and `background_color`


