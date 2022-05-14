import math

import cv2
import numpy as np

"""
Methods: In this section, all relevant methods are stored.
"""


def save_image(name, file):
    path = "output/" + name + ".jpg"
    cv2.imwrite(path, file)


def motion_blur_filter(h, w):
    [u, v] = np.mgrid[-h/2:h/2, -w/2:w/2]
    u = 2 * u/h
    v = 2 * v/w
    a = 0.22  # alpha
    b = 0.22  # beta
    h = np.sinc((a * u + b * v)) * np.exp(-1j * np.pi * (a * u + b * v))
    return h

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Read images for the exercises

    img_1_1 = cv2.imread("img/bird.jpg")
    img_1_1 = img_1_1.astype(np.double)
    img_1_2 = cv2.imread("img/geese.jpg")
    img_1_2 = img_1_2.astype(np.double)
    cv2.imshow("Original", img_1_1/255)

    # --- Exercise 1 ---------------------------------------------------------------------------------------------------

    cv2.imshow("Original", img_1_1/255)

    # Convert images to frequency domain
    f_1_1 = np.fft.fft2(img_1_1)

    # Create motion blur filter
    height1, width1, channels1 = f_1_1.shape
    blur_filter1 = motion_blur_filter(height1, width1)
    # Add third dimension for 3 channels of the filter
    h1 = np.repeat(blur_filter1[:, :, np.newaxis], 3, axis=2)

    # Add filter to image
    g1 = f_1_1*h1

    # Convert back to spatial domain
    img_1_1_motion_blur = np.fft.ifft2(g1)
    img_1_1_motion_blur = np.real(img_1_1_motion_blur)/255
    cv2.imshow("Back", img_1_1_motion_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    """
    x = cv2.imread("img/bird.jpg")
    x = x.astype(np.double)

    n2, n1, c = x.shape

    [k1, k2] = np.mgrid[0:n2, 0:n1]

    [u, v] = np.mgrid[-n2 / 2:n2 / 2, -n1 / 2:n1 / 2]
    u = 2 * u / n2
    v = 2 * v / n1

    F = np.fft.fft2(x)

    a = 0.22
    b = 0.22

    # Blurring function.
    H = np.sinc((u * a + v * b)) * np.exp(-1j * np.pi * (u * a + v * b))
    H = np.repeat(H[:, :, np.newaxis], 3, axis=2)
    G = F*H
    # Motion Blurred Image.
    g = np.fft.ifft2(G)
    cv2.imshow("motion blur", np.abs(g)/255)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

