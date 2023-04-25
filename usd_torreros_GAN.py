
#libs
import torch
import torchvision.transforms as transforms
from torchvision.models import srgan
from PIL import Image

def enhance_image_with_srgan(input_image_path, output_image_path):
    # Load the pre-trained SRGAN model
    model = srgan.create_transformer()
    model.eval()

    # Load the input image and preprocess it
    img = Image.open(input_image_path)
    preprocess = transforms.Compose([
        transforms.Resize((img.height * 4, img.width * 4), Image.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(img).unsqueeze(0)

    # Enhance the image using the SRGAN model
    with torch.no_grad():
        output_tensor = model(input_tensor)

    # Post-process the output image
    postprocess = transforms.Compose([
        transforms.Normalize(mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225], std=[1 / 0.229, 1 / 0.224, 1 / 0.225]),
        transforms.ToPILImage(),
    ])
    output_image = postprocess(output_tensor.squeeze(0))

    # Save the enhanced image
    output_image.save(output_image_path)

if __name__ == "__main__":
    enhance_image_with_srgan("usd_id_card_low_complex_bckrnd.jpg", "us_torreros_GAN_output.jpg")




#### END OF PROGRAM ####




"""

Story 104 - 
TASK 1 - Load a pre-trained GAN model for image enhancement. 
This could be a model like the SRGAN or a similar GAN designed for improving image quality.

TASK 2 - Preprocess the input image: The headshot image with the white background should be preprocessed to meet the requirements of the GAN model, 
such as resizing, normalization, or converting to the appropriate color space.

TASK 3 - Enhance the image using the GAN model: Pass the preprocessed image through the GAN model to enhance its quality. 
The model should generate a higher-quality image, maintaining natural details and improving the overall visual appearance.

TASK 4 - Post-process the output image: Perform any necessary post-processing steps on the enhanced image, 
such as resizing it back to the original dimensions or converting it to the appropriate color space.

TASK 5 - Save the enhanced image: Save the GAN-enhanced image as a new file with the desired specifications (JPEG format, size below 1 MB, 
and passport photo dimensions).

TASK 6 - Evaluate the results: Compare the enhanced image to the original input image to ensure that the quality has improved without 
introducing artifacts or making the image look overly edited.

TASK 7 - Integration with the current code: The new GAN-based image enhancement component should be created in a separate file and referenced 
in the existing Python program. The enhancement step should be added as the final step after the background has been set to white, and the image has been resized and saved with the specified requirements.

Acceptance Criteria: 

Issue(s):
Complex background confuses AI model.
Still having issues 4/25/23

Known Errors & Workarounds:
The AI model is having trouble extracting the headshot from complex backgrounds.
Solid gray background worked decently but not perfectly

"""
