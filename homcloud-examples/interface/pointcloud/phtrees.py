import json

import homcloud.interface as hc


def phtrees():
    phtrees = hc.PHTrees(path="output.2.pht")
    # The following line is same as:
    # nodes = phtrees.nodes_of(pds[2].pairs_in_rectangle(0.21, 0.25, 0.28, 0.35))
    nodes = phtrees.query_rectangle(0.21, 0.25, 0.28, 0.35)
    first_node = nodes[0]
    print("PD2 optimal volume by phtrees")
    print("  Optimal volume for ({}, {})".format(first_node.birth_time(),
                                                 first_node.death_time()))
    print("    Birth position:", first_node.birth_position())
    print("    Death position:", first_node.death_position())
    print("    Simplices: ", first_node.simplices())
    print("    Points:", first_node.points())
    print("    Boundary:", first_node.boundary())
    print("    Boundary points:", first_node.boundary())
    print("    (Direct) children pairs:", [(c.birth_time(), c.death_time())
                                           for c in first_node.children
                                           if c.living()])
    print("    Descendants: ", [(d.birth_time(), d.death_time())
                                for d in first_node.living_descendants()])

    with open("optimal-volume.2.json", "w") as f:
        json.dump({
            "result": [node.to_jsondict() for node in nodes]
        }, f)


phtrees()
