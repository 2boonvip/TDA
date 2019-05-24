
import homcloud.pc2diphacomplex as pc2diphacomplex
import homcloud.plot_PD as plot_PD
import homcloud.dump_diagram as dump_diagram
import homcloud.full_ph_tree as full_ph_tree
import homcloud.query_full_ph_tree as query_full_ph_tree

def main():
    pc2diphacomplex.main(pc2diphacomplex.argument_parser().parse_args([
        "-d", "3", "--no-square", "-I", "-D", "input.txt", "output.idiagram"
    ]))
    plot_PD.main(plot_PD.argument_parser().parse_args([
        "-d", "1", "-x", "[0:0.5]", "-X", "256", "-l", "-U", "no unit",
        "-t", "PD_1", "-m", "100", "-o", "output.1.png", "output.idiagram"
    ]))
    plot_PD.main(plot_PD.argument_parser().parse_args([
        "-d", "2", "-x", "[0:0.5]", "-X", "256", "-l", "-U", "no unit",
        "-t", "PD_2", "-m", "100", "-o", "output.2.png", "output.idiagram"
    ]))
    dump_diagram.main(dump_diagram.argument_parser().parse_args([
        "-d", "1", "output.idiagram", "-o", "output.1.txt",
    ]))
    dump_diagram.main(dump_diagram.argument_parser().parse_args([
        "-d", "2", "output.idiagram", "-o", "output.2.txt",
    ]))
    full_ph_tree.main(full_ph_tree.argument_parser().parse_args([
        "-d", "2", "output.idiagram", "output.2.pht",
    ]))
    query_full_ph_tree.main(query_full_ph_tree.argument_parser().parse_args([
        "-c", "draw-volumes-in-rectangle 0.21 0.25 0.28 0.35 voids.vtk",
        "output.2.pht", "-B", "yes", "-D", "yes",
    ]))

main()
