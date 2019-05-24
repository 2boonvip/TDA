import sys
import re

from PIL import Image, ImageDraw


def main(birth, death, input_file, pict_path, output_path):
    birth_pixels = []
    with open(input_file) as f:
        for line in f:
            birth_time, death_time, birth_pixel, _ = re.split(r"\s+", line.strip())
            if birth_time == birth and death_time == death:
                birth_pixels.append(parse_pixel(birth_pixel))

    image = Image.open(pict_path).convert("RGB")
    for y, x in birth_pixels:
        image.putpixel((x, y), (255, 0, 0))
    image.save(output_path)


def parse_pixel(value):
    m = re.match(r"\(([\d,]+)\)\Z", value)
    return map(int, re.split(r",", m.group(1)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
