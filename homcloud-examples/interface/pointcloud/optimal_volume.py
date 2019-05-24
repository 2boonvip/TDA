import json

import homcloud.interface as hc


def optimal_volumes():
    pds = hc.PDs("output.idiagram")
    optimal_volumes = [
        pair.optimal_volume(cutoff_radius=1.0, num_retry=3)
        for pair in pds[1].pairs()
        if (0.2 < pair.birth_time() < 0.25) and (0.35 < pair.death_time() < 0.4)
    ]
    print("PD1 optimal volume:")
    print("  number of pairs in (0.2, 0.25)x(0.35, 0.4): %d" % len(optimal_volumes))
    optimal_volume = optimal_volumes[0]
    print("  Optimal Volume for (%f, %f)" % (optimal_volume.birth_time(),
                                             optimal_volume.death_time()))
    print("    Simplices:", optimal_volume.simplices())
    print("    Points in simplices:", optimal_volume.points())
    print("    Boundary:", optimal_volume.boundary())
    print("    Boundary points:", optimal_volume.boundary())
    print("    Children:", optimal_volume.children())

    with open("optimal-volume.1.json", "w") as f:
        json.dump({
            "result": [optimal_volume.to_dict() for optimal_volume in optimal_volumes]
        }, f)


optimal_volumes()
