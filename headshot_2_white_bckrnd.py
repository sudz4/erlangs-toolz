"""
Story 101 - As a Student, I want to be able to take a headshot photo with my laptop computer 
and save the output with a white background, 
so that the photo can be printed onto a student id card.
TASK 1 -
TASK 2 -

Acceptance Criteria: 

Issue(s):
Complex background confuses AI model.

"""

import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

def make_background_white(image_path, output_path):
    img = cv2.imread(image_path)

    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = selfie_segmentation.process(img_rgb)

        mask = result.segmentation_mask
        mask = (mask > 0.1).astype(np.uint8)
        mask = cv2.dilate(mask, np.ones((3, 3), dtype=np.uint8), iterations=1)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        img_white_bg = np.where(mask, img, 255)

    cv2.imwrite(output_path, img_white_bg)

if __name__ == "__main__":
    make_background_white("usd_id_card_1mb.jpg", "usd_id_card_1mb_white.jpg")