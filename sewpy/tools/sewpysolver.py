#!/usr/bin/env python3

import math
import os
import argparse

"""
    Script to solve bateman equation, considering only decays
    which is
    
    dN_{i}/dt = A_{ij} N_{j}
    
    Does not use scipy, uses explicit runge kutta 4 method to solve
    and compares with analytical result
"""
def main():
    # get command line args for input and output files
    parser = argparse.ArgumentParser(description='Bateman')
    parser.add_argument('input', type=argparse.FileType('r'), help='The absolute path to the input file')
    parser.add_argument('output', type=argparse.FileType('w'), help='The absolute path to the output file')
    args = parser.parse_args()

    # input and output filenames
    ifilename = args.input.name
    ofilename = args.output.name

    # timestep
    dt = -1.0

    # initial and end time
    ti = -1.0
    tf = -1.0

    # general vector and matrix
    N0 = [ ]
    A  = [ ]

    # read input file
    with open(ifilename, 'rt') as fi:
        lines = [l.strip() for l in fi.readlines() if l.strip()]

        def check_keyword(keyword):
            if lines.count(keyword) != 1:
                raise RuntimeError("{} keyword error".format(keyword))

        check_keyword('timestep')
        check_keyword('initial_time')
        check_keyword('final_time')
        check_keyword('inventory')
        check_keyword('matrix')

        dt = float(lines[lines.index('timestep')+1])
        ti = float(lines[lines.index('initial_time')+1])
        tf = float(lines[lines.index('final_time')+1])

        nr_of_inv = int(lines[lines.index('inventory')+1])
        nr_of_matrix = int(lines[lines.index('matrix')+1])
        if nr_of_inv != nr_of_matrix:
            raise RuntimeError("inventory and matrix are of different sizes")

        for i in range(1, nr_of_inv+1):
            N0.append(float(lines[lines.index('inventory')+1+i]))

        for i in range(1, nr_of_matrix+1):
            col = [float(l.strip()) for l in lines[lines.index('matrix')+1+i].split(',')]
            A.append(col)

        print("".join(["=" for i in range(0,40)]))
        print("Timestep: {}".format(dt))
        print("Start time: {}".format(ti))
        print("End time: {}".format(tf))
        print("Initial inventory: {}".format(N0))
        print("Decay matrix: {}".format(A))
        print("".join(["=" for i in range(0,40)]))


    def eval(tn, yn):
        ym = []
        for i in range(0, len(yn)):
            sum = 0.
            for j in range(0, len(yn)):
                sum += A[i][j]*yn[j]
            ym.append(sum)
            
        return ym

    # runge kutta coefficients
    def rk4_k1(tn, yn):
        a = eval(tn, yn)
        return [dt*a[i] for i in range(0, len(a))]

    def rk4_k2(tn, yn):
        k1 = rk4_k1(tn, yn)
        ya = [yn[i] + (k1[i]/2.0) for i in range(0, len(yn))]
        a = eval(tn + (dt/2.0), ya)
        return [dt*a[i] for i in range(0, len(a))]

    def rk4_k3(tn, yn):
        k2 = rk4_k2(tn, yn)
        ya = [yn[i] + (k2[i]/2.0) for i in range(0, len(yn))]
        a = eval(tn + (dt/2.0), ya)
        return [dt*a[i] for i in range(0, len(a))]

    def rk4_k4(tn, yn):
        k3 = rk4_k3(tn, yn)
        ya = [yn[i] + k3[i] for i in range(0, len(yn))]
        a = eval(tn + dt, ya)
        return [dt*a[i] for i in range(0, len(a))]

    def evalnextstep(tn, yn):
        coeff = (1.0/6.0)
        k1 = rk4_k1(tn, yn)
        k2 = rk4_k2(tn, yn)
        k3 = rk4_k3(tn, yn)
        k4 = rk4_k4(tn, yn)
        return [yn[i] + coeff*(k1[i] + 2.0*k2[i] + 2.0*k3[i] + k4[i]) for i in range(0, len(yn))]

    # using runge kutta
    yn = N0
    t = ti
    times = []
    N_list = []
    while t < tf:
        times.append(t)
        N_list.append(yn)
        yn = evalnextstep(t, yn)
        t = t + dt

    print("Start:: time: {:.2f} inv: {}".format(times[0],  N_list[0]))
    print("End  :: time: {:.2f} inv: {}".format(times[-1], N_list[-1]))

    # write to output file
    assert len(times) == len(N_list)
    with open(ofilename, 'wt') as fo:
        for i in range(0, len(times)):
            fo.write("=====================\n")
            fo.write("{:<10} {:<30}\n".format('Time: ', times[i]))
            fo.write("---------------------\n")
            for j in range(0, len(N_list[i])):
                fo.write("{:<10} {:.4e}\n".format(j, N_list[i][j]))

if __name__ == "__main__":
    main()
