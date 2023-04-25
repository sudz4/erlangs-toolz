import cv2
import mediapipe as mp
import numpy as np
import os

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

def make_id_photo(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)

    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = selfie_segmentation.process(img_rgb)

        mask = result.segmentation_mask
        mask = (mask > 0.1).astype(np.uint8)

        mask = cv2.GaussianBlur(mask, (7, 7), 0)
        mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

        img_white_bg = np.where(mask, img, 255)

    id_width, id_height = 45 * 5, 35 * 5
    img_id_size = cv2.resize(img_white_bg, (id_width, id_height), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(output_image_path, img_id_size, [cv2.IMWRITE_JPEG_QUALITY, 95]) # increasing number parameter makes quality better but also makes file size larger

    output_size_kb = os.path.getsize(output_image_path) / 1024
    while output_size_kb > 1024:
        quality = int(1024 * 80 / output_size_kb)
        cv2.imwrite(output_image_path, img_id_size, [cv2.IMWRITE_JPEG_QUALITY, quality])
        output_size_kb = os.path.getsize(output_image_path) / 1024

    print(f"Output image specs:")
    print(f"File name: {output_image_path}")
    print(f"File size: {output_size_kb:.2f} KB")
    print(f"Image dimensions: {id_width} x {id_height} pixels")

if __name__ == "__main__":
    input_image_path = "usd_id_card_1mb.jpg"
    # input_image_path = "usd_low_complex_bckrnd.jpg"
    output_image_path = "usd_torreros_mss.jpg"
    make_id_photo(input_image_path, output_image_path)