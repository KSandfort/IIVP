import cv2
import utils


# --- Prepare images ---
bgr_1_1 = cv2.imread("img/img_1_1.jpg")
bgr_1_2 = cv2.imread("img/img_1_2.jpg")

rgb_1_1 = cv2.cvtColor(bgr_1_1, cv2.COLOR_BGR2RGB)
rgb_1_2 = cv2.cvtColor(bgr_1_2, cv2.COLOR_BGR2RGB)

hsv_1_1 = cv2.cvtColor(rgb_1_1, cv2.COLOR_RGB2HSV)
hsv_1_2 = cv2.cvtColor(rgb_1_2, cv2.COLOR_RGB2HSV)

#
"""
--- Collection of functions to show images from the GUI ----------------------------------------------------------------
Functions follow the following naming convention:
show_x_y_z_type_channel, where
x = task number
y = task number suffix
z = image number
type = colour coding
channel = channel name
example: show_1_1_1_rgb_r() means to show the R-channel in RGB space of the first image of task 1.1
"""


# Exercise 1.1 - Image 1
def show_1_1_1_original():
    cv2.imshow("Task 1.1 - Image 1 - Original", bgr_1_1)


def show_1_1_1_rgb():
    cv2.imshow("Task 1.1 - Image 1 - RGB", rgb_1_1)


def show_1_1_1_rgb_r():
    cv2.imshow("Task 1.1 - Image 1 - R-Channel", rgb_1_1[:, :, 0])


def show_1_1_1_rgb_g():
    cv2.imshow("Task 1.1 - Image 1 - G-Channel", rgb_1_1[:, :, 1])


def show_1_1_1_rgb_b():
    cv2.imshow("Task 1.1 - Image 1 - B-Channel", rgb_1_1[:, :, 2])


def show_1_1_1_hsv():
    cv2.imshow("Task 1.1 - Image 1 - HSV with inbuilt function", hsv_1_1)


def show_1_1_1_hsv_h():
    cv2.imshow("Task 1.1 - Image 1 - HSV H-Channel", hsv_1_1[:, :, 0])


def show_1_1_1_hsv_s():
    cv2.imshow("Task 1.1 - Image 1 - HSV S-Channel", hsv_1_1[:, :, 1])


def show_1_1_1_hsv_v():
    cv2.imshow("Task 1.1 - Image 1 - HSV V-Channel", hsv_1_1[:, :, 2])


# Exercise 1.1 - Image 2
def show_1_1_2_original():
    cv2.imshow("Task 1.1 - Image 2 - Original", bgr_1_2)


def show_1_1_2_rgb():
    cv2.imshow("Task 1.1 - Image 2 - RGB", rgb_1_2)


def show_1_1_2_rgb_r():
    cv2.imshow("Task 1.1 - Image 2 - R-Channel", rgb_1_2[:, :, 0])


def show_1_1_2_rgb_g():
    cv2.imshow("Task 1.1 - Image 2 - G-Channel", rgb_1_2[:, :, 1])


def show_1_1_2_rgb_b():
    cv2.imshow("Task 1.1 - Image 2 - B-Channel", rgb_1_2[:, :, 2])


def show_1_1_2_hsv():
    cv2.imshow("Task 1.1 - Image 2 - HSV with inbuilt function", hsv_1_2)


def show_1_1_2_hsv_h():
    cv2.imshow("Task 1.1 - Image 2 - HSV H-Channel", hsv_1_2[:, :, 0])


def show_1_1_2_hsv_s():
    cv2.imshow("Task 1.1 - Image 2 - HSV S-Channel", hsv_1_2[:, :, 1])


def show_1_1_2_hsv_v():
    cv2.imshow("Task 1.1 - Image 2 - HSV V-Channel", hsv_1_2[:, :, 2])


# Exercise 1.2 - Image 1
def show_1_2_1_hsi():
    cv2.imshow("Task 1.2 - Image 1 - HSI", utils.rgb2hsi(rgb_1_1))


def show1_2_1_hsv():
    cv2.imshow("Task 1.2 - Image 1 - HSV", utils.rgb2hsv(rgb_1_1))


def show1_2_1_hsv_h():
    cv2.imshow("Task 1.2 - Image 1 - HSV H-Channel", utils.rgb2hsv(rgb_1_1)[:, :, 0])


def show1_2_1_hsv_s():
    cv2.imshow("Task 1.2 - Image 1 - HSV S-Channel", utils.rgb2hsv(rgb_1_1)[:, :, 1])


def show1_2_1_hsv_v():
    cv2.imshow("Task 1.2 - Image 1 - HSV V-CHannel", utils.rgb2hsv(rgb_1_1)[:, :, 2])


def make_later(self):
    # (1) --- Transformation from RGB to HSV ---------------------------------------------------------------------------


    # Show original image, HSV image and HSV channels

    # (2) --- Transformation from RGB to HSI/HSV manually --------------------------------------------------------------

    # RGB to HSI

    cv2.imshow("1_1 HSI image", hsi_1_1)

    # RGB to HSV
    hsv_1_1 = utils.rgb2hsv(rgb_1_1)
    cv2.imshow("1_1 HSV image", hsv_1_1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # RGB to HSI
    hsi_1_2 = utils.rgb2hsi(rgb_1_2)
    cv2.imshow("1_2 HSI image", hsi_1_2)

    # RGB to HSV
    hsv_1_2 = utils.rgb2hsv(rgb_1_2)
    cv2.imshow("1_2 HSV image", hsv_1_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()