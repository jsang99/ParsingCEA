import os
import numpy as np
import matplotlib.pyplot as plt


def parse(filename):
    with open(filename) as f:  # opening a file
        lines = f.readlines()  # creating an array called lines with lines in that mf

    AEAT = []
    CSTAR = []
    CF = []
    Ivac = []
    Isp = []
    pressures = []
    ofus = []

    for line in lines:
        if "Ae/At" in line:
            new = float(line.replace('Ae/At', '').replace(' ', '').replace('\n', ''))
            AEAT.append(new)
        if "CSTAR, FT/SEC" in line:
            new = float(line.replace('CSTAR, FT/SEC', '').replace(' ', '').replace('\n', ''))
            CSTAR.append(new)
        if "CF" in line:
            new = float(line.replace('CF', '').replace(' ', '').replace('\n', ''))
            CF.append(new)
        if "Ivac,LB-SEC/LB" in line:
            new = float(line.replace('Ivac,LB-SEC/LB', '').replace(' ', '').replace('\n', ''))
            Ivac.append(new)
        if "Isp, LB-SEC/LB " in line:
            new = float(line.replace('Isp, LB-SEC/LB', '').replace(' ', '').replace('\n', ''))
            Isp.append(new)
        if "p,psia" in line:
            pressures = line.replace('p,psia=', '').replace(' ', '').replace('\n', '').split(',')
            i = 0
            while i < len(pressures):
                temp = float(pressures[i])
                pressures[i] = temp
                i += 1
        if "o/f=" in line:
            ofus = line.replace('o/f=', '').replace(' ', '').replace('\n', '').split(',')
            i = 0
            while i < len(ofus):
                temp = float(ofus[i])
                ofus[i] = temp
                i += 1

    numOFUS = len(ofus)
    numPRESSURES = len(pressures)

    ofus = list(np.repeat(ofus, numPRESSURES))
    #print(ofus)
    pressures = pressures * numOFUS
    #print(pressures)

    #print("AEAT ", len(AEAT))
    #print("CSTAR ", len(CSTAR))
    #print("CF ", len(CF))
    #print("Ivac ", len(Ivac))
    #print("Isp ", len(Isp))
    #print("OFUS ", len(ofus))
    #print("pressures ", len(pressures))


    # data to be plotted
    x = pressures[:numOFUS]
    y = Isp[:numOFUS]

    # plotting
    plt.title("Line graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.plot(x, y, color="red")
    plt.show()


if __name__ == '__main__':
    parse('sample_output.out')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
