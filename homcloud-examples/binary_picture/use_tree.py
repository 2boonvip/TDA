import msgpack
from PIL import Image, ImageDraw

import homcloud.pict.tree as picttree

def main():
    picttree.main(picttree.argument_parser().parse_args([
        "-m", "black-base", "-t", "128", "-s", "-T", "picture2d",
        "-O", "msgpack", "-o", "output.p2mt", "input.png"
    ]))
    with open("output.p2mt", "rb") as f:
        treeinfo = msgpack.load(f, encoding="UTF-8")

    show_0th_volumes(treeinfo)
    show_0th_volumes_4_5(treeinfo)
    show_1st_volume(treeinfo)
    show_1st_volume_6_7(treeinfo)
    # image = Image.open("input.png").convert("RGB")
    # print(image)

    picttree.main(picttree.argument_parser().parse_args([
        "-m", "black-base", "-t", "128", "-s", "-T", "picture2d",
        "-O", "json", "-o", "output-tree.json", "input.png"
    ]))

def show_0th_volumes(treeinfo):
    image = Image.open("input.png").convert("RGB")

    def draw_birthdeath_pair(birth, death, color1, color2):
        for node in treeinfo["lower"]["nodes"].values():
            if node["birth-time"] == birth and node["death-time"] == death:
                found = node
                break

        for (y, x) in found["volume"]:
            is_white = image.getpixel((x, y))[0] == 255
            if is_white:
                image.putpixel((x, y), color1)
            else:
                image.putpixel((x, y), color2)
        image.putpixel(tuple(reversed(found["birth-pixel"])), (0, 0, 255))
        image.putpixel(tuple(reversed(found["death-pixel"])), (255, 0, 0))

    draw_birthdeath_pair(-6, 5, (255, 128, 128), (128, 64, 64))
    draw_birthdeath_pair(-15, 6, (128, 255, 128), (64, 128, 64))
    image.save("output_0_long_lifetime.png")

def show_0th_volumes_4_5(treeinfo):
    image = Image.open("input.png").convert("RGB")

    for node in treeinfo["lower"]["nodes"].values():
        if node["birth-time"] == -5 and node["death-time"] == -4:
            for (y, x) in node["volume"]:
                image.putpixel((x, y), (128, 64, 64))
            image.putpixel(tuple(reversed(node["birth-pixel"])), (255, 0, 0))

    image.save("output_0_-5_-4.png")

def show_1st_volume(treeinfo):
    image = Image.open("input.png").convert("RGB")

    for node in treeinfo["upper"]["nodes"].values():
        if node["birth-time"] == -5 and node["death-time"] == 3:
            for (y, x) in node["volume"]:
                is_white = image.getpixel((x, y))[0] == 255
                if is_white:
                    image.putpixel((x, y), (255, 128, 128))
                else:
                    image.putpixel((x, y), (128, 64, 64))

    image.save("output_1_long_lifetime.png")

def show_1st_volume_6_7(treeinfo):
    image = Image.open("input.png").convert("RGB")

    for node in treeinfo["upper"]["nodes"].values():
        if node["birth-time"] == 6 and node["death-time"] == 7:
            for (y, x) in node["volume"]:
                is_white = image.getpixel((x, y))[0] == 255
                if is_white:
                    image.putpixel((x, y), (255, 128, 128))
                else:
                    image.putpixel((x, y), (128, 64, 64))
            image.putpixel(tuple(reversed(node["death-pixel"])), (255, 0, 0))

    image.save("output_1_6_7.png")

main()
