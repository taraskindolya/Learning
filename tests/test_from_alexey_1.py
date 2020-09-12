import os

from src.tools.methods import compare_images
from src.tools.variables import *


def test_compare_images_1(get_path_to_images):
    assert compare_images(os.path.join(get_path_to_images, im_full),
                          os.path.join(get_path_to_images, im_full)) == "Equal", "Fail! Images are not equal!"


def test_compare_images_2(get_path_to_images):
    assert compare_images(os.path.join(get_path_to_images, im_full),
                          os.path.join(get_path_to_images, im_b)) != "Equal", "Fail! Images are equal!"
