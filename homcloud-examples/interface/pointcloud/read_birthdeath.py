import homcloud.interface as hc


def print_birthdeath(pd):
    print(pd.births)
    print(pd.deaths)


pds = hc.PDs("output.idiagram")
print("PD1")
print_birthdeath(pds[1])
print("PD2")
print_birthdeath(pds[2])
