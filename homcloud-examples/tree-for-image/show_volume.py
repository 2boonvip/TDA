from PIL import Image, ImageDraw

from homcloud.merge_tree import MergeTree

def main():
    mt = MergeTree.load_from_pmcfile("output.pmt")
    image = Image.open("input.png").convert("RGB")
    draw = ImageDraw.Draw(image)

    node = find_node_by_birthdeath(mt, 16.0, 38.0)
    volume = node.volume()
    print(len(volume))
    for volume_node in volume:
        y, x = volume_node.pos
        draw.point((x, y), fill=(255, 0, 0))
    image.save("volume.png")

def find_node_by_birthdeath(mt, birth, death):
    for node in mt.nodes:
        if node.level == birth and node.death_time == death:
            return node

if __name__ == "__main__":
    main()
