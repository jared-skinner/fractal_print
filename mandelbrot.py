#!/usr/bin/python3

import numpy as np

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn, dtype=np.float32)
    Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
    C = X + Y[:, None]*1j
    N = np.zeros(C.shape, dtype=int)
    Z = np.zeros(C.shape, np.complex64)
    for n in range(maxiter):
        I = np.less(abs(Z), horizon)

        N[I] = 0
        Z[I] = Z[I]**2 + C[I]

    N[N == maxiter-1] = 0

    return Z, N


if __name__ == '__main__':
    import time
    import matplotlib
    from matplotlib import colors
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import argparse

    parser = argparse.ArgumentParser(description='mandelbrot', prog="mandlebrot.py")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.1.0')
    parser.add_argument('--xmin', help="The minimum x value")
    parser.add_argument('--xmax', help="The maxiumu x value")
    parser.add_argument('--ymin', help="The minimum y value")
    parser.add_argument('--ymax', help="The maximum y value")
    parser.add_argument('--iter', help="The number of iterations")
    args = parser.parse_args()

    if args.xmin:
        xmin = float(args.xmin)
    else:
        xmin = -2

    if args.xmax:
        xmax = float(args.xmax)
    else:
        xmax = 2

    if args.ymin:
        ymin = float(args.ymin)
    else:
        ymin = -2

    if args.ymax:
        ymax = float(args.ymax)
    else:
        ymax = 2

    if args.xmin:
        maxiter = int(args.iter)
    else:
        maxiter = 10 

    xn = 3000/2
    yn = 2500/2
    horizon = 2
    log_horizon = np.log(np.log(horizon))/np.log(2)

    for i in range(maxiter):
        Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, i, horizon)

        with np.errstate(invalid='ignore'):
            #M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z)))/np.log(2) + log_horizon)
            M = np.nan_to_num(np.less(abs(Z), 2))

        dpi = 300
        width = 10
        height = 10*yn/xn
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

        plt.imshow(M, extent=[xmin, xmax, ymin, ymax])#, interpolation="bicubic")
        ax.set_xticks([])
        ax.set_yticks([])

        plt.savefig(str(i)+".png")

        plt.close(fig)
