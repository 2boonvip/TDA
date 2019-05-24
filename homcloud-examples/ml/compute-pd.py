import os
import sys
import homcloud.pict.binarize as binarize

def main():
    os.makedirs("data-1-pd", exist_ok=True)
    for n in range(100):
        print(n, file=sys.stderr)
        binarize.main(binarize.argument_parser().parse_args([
            "-m", "white-base", "-t", "128", "-I", "-s", "-D",
            "data-1/{:04d}.png".format(n), "data-1-pd/{:04d}.idiagram".format(n)
        ]))

if __name__ == "__main__":
    main()
