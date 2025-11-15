from PIL import Image, ImageDraw
import numpy as np
import random

def image_to_dot_density(
    input_path,
    output_path,
    dot_color=(0, 0, 0),
    background_color=(255, 255, 255),
    resize_to=(300, 200),
    max_dots_per_pixel=8,
    dot_radius=1,
    jitter=0.4
):
    """
    Create a dot-density stipple image based on grayscale brightness.
    
    Dark areas -> many dots
    Bright areas -> few/no dots
    """

    # Load and convert image
    img = Image.open(input_path).convert("L")

    # Optional resize for controllable density
    if resize_to:
        img = img.resize(resize_to)

    # Convert grayscale to 0..1 float array
    gray = np.array(img) / 255.0

    # Create output canvas
    w, h = img.size
    out = Image.new("RGB", (w, h), background_color)
    draw = ImageDraw.Draw(out)

    # Loop all pixels
    for y in range(h):
        for x in range(w):
            brightness = gray[y, x]       # 0 = black, 1 = white
            dot_count = int(max_dots_per_pixel * (1 - brightness))

            for _ in range(dot_count):
                # Random jitter for natural look
                dx = x + random.uniform(-jitter, jitter)
                dy = y + random.uniform(-jitter, jitter)

                # Draw dot
                draw.ellipse(
                    (
                        dx - dot_radius,
                        dy - dot_radius,
                        dx + dot_radius,
                        dy + dot_radius
                    ),
                    fill=dot_color
                )

    # Save
    out_name = (
    f"dom_{dot_color[0]}-{dot_color[1]}-{dot_color[2]}"
    f"_{resize_to[0]}-{resize_to[1]}_{max_dots_per_pixel}_{dot_radius}_"
    f"{jitter}.png"
    )

    output_path = f"./{out_name}"
    out.save(output_path)
    print("Saved:", output_path)



# Example usage:
#for i in range(35, 65, 10):
image_to_dot_density(
    input_path="dom_edit.JPG",
    output_path="city_dots.png",
    dot_color=(38, 255, 67),
    resize_to=(3000, 2000),
    max_dots_per_pixel=2.5,
    dot_radius=0.05,
    jitter=1
)  
