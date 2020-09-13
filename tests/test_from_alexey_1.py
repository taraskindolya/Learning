import os

import pytest

from src.tools.methods import compare_images, find_fragment
from src.tools.variables import *


def test_compare_images_1(get_path_to_images):
    assert compare_images(os.path.join(get_path_to_images, im_full),
                          os.path.join(get_path_to_images, im_full)) == "Yes", "Fail! Images are not equal!"


@pytest.mark.xfail
def test_compare_images_2(get_path_to_images):
    assert compare_images(os.path.join(get_path_to_images, im_full),
                          os.path.join(get_path_to_images, im_b)) == "Yes", "Fail! Images are equal!"


def test_find_fragment_1(get_path_to_images):
    assert find_fragment(os.path.join(get_path_to_images, im_full),
                         os.path.join(get_path_to_images,
                                      im_b)) == "Yes", "Fail! Image does not contain given fragment!"


@pytest.mark.xfail
def test_find_fragment_2(get_path_to_images):
    assert find_fragment(os.path.join(get_path_to_images, im_full),
                         os.path.join(get_path_to_images, im_s)) == "Yes", "Fail! Image contains given fragment!"
