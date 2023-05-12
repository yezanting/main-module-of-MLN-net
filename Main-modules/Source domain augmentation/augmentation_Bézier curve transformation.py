from __future__ import print_function
import math
import os
import random
import copy

import cv2
import scipy
import imageio
import string
import numpy as np
from skimage.transform import resize
try:  # SciPy >= 0.19
    from scipy.special import comb
except ImportError:
    from scipy.misc import comb

def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i

def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       Control points should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    nPoints = len(points)

    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals



def nonlinear_transformation(x, prob=0.5):

    # points = [[0, 0],[0.35,0.65],[0.65,0.35],[1, 1]]
    points = [[0, 0], [0.9, 0.1], [0.1, 0.9], [1, 1]]
    xpoints = [p[0] for p in points]
    ypoints = [p[1] for p in points]
    xvals, yvals = bezier_curve(points, nTimes=100000)


    xvals, yvals = np.sort(xvals), np.sort(yvals)
    nonlinear_x = np.interp(x, xvals, yvals)
    return nonlinear_x


def aug_img(img):
    height,width = img.shape[0], img.shape[1]


     # Apply non-Linear transformation with an assigned probability

    img = nonlinear_transformation(img, 0.5)

    return img

if __name__ == '__main__':
    # Define input and output directories
    input_dir = r"G:\data\cbis-ddsm\chen_dong_selectdata\ddsm\cbis_train_test\train\image_512"
    output_dir = r"G:\data\cbis-ddsm\chen_dong_selectdata\ddsm\cbis_train_test\train\image_512_0.9"

    for filename in os.listdir(input_dir):
        # Check if file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Read image
            img = cv2.imread(os.path.join(input_dir, filename))
            grau_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grau_img = grau_img / 255
            B_img = aug_img(grau_img)
            # grau_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            B_img = B_img * 255

            cv2.imwrite(os.path.join(output_dir, filename), B_img)
