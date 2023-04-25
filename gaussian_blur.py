"""
Story 101 - As a Student, I want to be able to take a headshot photo with my laptop computer 
and save the output with a white background, 
so that the photo can be printed onto a student id card.
TASK 1 - Fix edges smoothing
TASK 2 - 

Acceptance Criteria: 

Issue(s):
Complex background confuses AI model.
Still having issues 4/25/23

Known Errors & Workarounds:
The AI model is having trouble extracting the headshot from complex backgrounds.
Solid gray background worked decently but not perfectly

"""

import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

def make_background_white(image_path, output_path):
    img = cv2.imread(image_path)

    # Resize the image
    scale_factor = 1.5
    height, width = img.shape[:2]
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    # Enhance the contrast and brightness
    alpha = 1.2
    beta = 30
    img = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

    # Denoise the image
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # Sharpen the image
    sharpen_kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
    img = cv2.filter2D(img, -1, sharpen_kernel)

    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = selfie_segmentation.process(img_rgb)

        mask = result.segmentation_mask
        mask = (mask > 0.1).astype(np.uint8)

        # Apply Gaussian blur to the binary mask to smooth the edges
        mask = cv2.GaussianBlur(mask, (7, 7), 0)
        mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

        img_white_bg = np.where(mask, img, 255)

    cv2.imwrite(output_path, img_white_bg)

if __name__ == "__main__":
    # make_background_white("usd_id_card_1mb.jpg", "usd_gaus_blurred.jpg")
    make_background_white("usd_low_complex_bckrnd.jpg", "usd_low_complex_gaussian.jpg")


