import cv2


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
    result = "Equal"
    while i < lh:
        if hash1[i] != hash2[i]:
            result = "Not equal"
            break
        else:
            i = i + 1
    return result


def find_fragment(im_1, im_2):
    method = cv2.TM_SQDIFF_NORMED

    fragment = cv2.imread(im_1)
    image = cv2.imread(im_2)

    result = cv2.matchTemplate(fragment, image, method)
    print(result)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


find_fragment("s.png", "full.png")
