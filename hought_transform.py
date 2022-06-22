import cv2
from tools.helper_function import *

def process_image(image):

    # convert to grayscale
    gray_img = grayscale(image)
    # show_image("gray_scale", gray_img)

    # darken the grayscale
    darkened_img = adjust_gamma(gray_img, 1)
    # show_image("darkened_img", darkened_img)

    #Convert original image to HLS colour space
    hls_img = to_hls(image)
    # show_image("hls_img", hls_img)
    
    # Color Selection
    white_mask = isolate_color_mask(to_hls(image), np.array([0, 200, 0], dtype=np.uint8), np.array([200, 255, 255], dtype=np.uint8))
    # show_image("white_mask", white_mask)
    
    # yellow_mask = isolate_color_mask(to_hls(image), np.array([10, 0, 100], dtype=np.uint8), np.array([40, 255, 255], dtype=np.uint8))
    # mask = cv2.bitwise_or(white_mask, yellow_mask)
    # colored_img = cv2.bitwise_and(darkened_img, darkened_img, mask=mask)
    # show_image("colored_img", colored_img)

    # Apply Gaussian Blur
    blurred_img = gaussian_blur(white_mask, kernel_size=5)
    # show_image("blurred_img", blurred_img)
    
    # Apply Canny edge filter
    canny_img = canny(blurred_img, low_threshold=50, high_threshold=140)
    show_image("canny_img", canny_img)