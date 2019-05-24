import sys
import re

from PIL import Image, ImageDraw
import numpy as np
import scipy.misc


def main(input_file, pict_path, output_path):
    birth_pixels = []
    with open(input_file) as f:
        for line in f:
            birth_time, death_time, birth_pixel, _ = re.split(r"\s+", line.strip())
            if float(death_time) - float(birth_time) < -0.3:
                birth_pixels.append(parse_pixel(birth_pixel))

    scipy.misc.imsave("grayscale.png", np.loadtxt(pict_path))

    image = Image.open("grayscale.png").convert("RGB")
    draw = ImageDraw.Draw(image)

    for y, x in birth_pixels:
        draw.ellipse(((x-2, y-2), (x+2, y+2)), fill=(255, 0, 0))
    image.save(output_path)


def parse_pixel(value):
    m = re.match(r"\(([\d,]+)\)\Z", value)
    return map(int, re.split(r",", m.group(1)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
