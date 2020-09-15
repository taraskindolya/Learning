import cv2
import numpy as np
import os

from os import listdir
from src.tools.variables import *

# calculates hash
def calc_image_hash(f_name):
    image = cv2.imread(f_name)  # read image
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # zoom out the picture
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # convert to black and white format
    avg = gray_image.mean()  # average pixel value
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # threshold binarization

    # calculate hash
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


# compare hash
def compare_images(im_1, im_2):
    hash1 = calc_image_hash(im_1)
    hash2 = calc_image_hash(im_2)
    lh = len(hash1)
    i = 0
    result = "Yes"
    while i < lh:
        if hash1[i] != hash2[i]:
            result = "No"
            break
        else:
            i = i + 1
    return result


def find_fragment(im_where, im_what):
    where_find = cv2.imread(im_where)
    what_find = cv2.imread(im_what)

    res = cv2.matchTemplate(where_find, what_find, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    result = "Yes"
    if len(loc[0]) == 0 and len(loc[1]) == 0:
        result = "No"
    return result


def find_icon_center_coordinates(path):
    icons = [file for file in listdir(path) if file.startswith(icon_prefix)]  # collect all icon names
    icon_center_coordinates = {}
    for icon in icons:
        icon_name = os.path.splitext(icon)[0]

        where_find = cv2.imread(path + im_full)
        what_find = cv2.imread(path + icon)
        w, h = what_find.shape[:2]  # get shape of icon

        res = cv2.matchTemplate(where_find, what_find, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)

        # calculate coordinates of center
        x_center = loc[1][0] + h / 2
        y_center = loc[0][0] + w / 2

        icon_center_coordinates[icon_name] = [x_center, y_center]

    return icon_center_coordinates
