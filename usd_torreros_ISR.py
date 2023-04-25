import ISR
from ISR.models import RRDN
from PIL import Image

def enhance_image_with_srresnet(input_image_path, output_image_path):
    # Load the pre-trained SRResNet model
    model = RRDN(weights='div2k')

    # Load the input image
    img = Image.open(input_image_path)

    # Enhance the image using the SRResNet model
    output_image = model.predict(img)

    # Save the enhanced image
    output_image.save(output_image_path)

if __name__ == "__main__":
    enhance_image_with_srresnet("usd_torreros_ms.jpg", "usd_torreros_ms_ISR_output.jpg")
