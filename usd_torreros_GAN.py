
""" 
ESRGAN enhancer
"""

#libs
import torch
import torchvision.transforms as transforms
from PIL import Image
from ESRGAN.RRDBNet_arch import RRDBNet as arch

def enhance_image_with_esrgan(input_image_path, output_image_path, model_path='ESRGAN/models/RRDB_ESRGAN_x4.pth'):
    # Load the pre-trained ESRGAN model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    model = model.to(device)

    # Load the input image and preprocess it
    img = Image.open(input_image_path).convert('RGB')
    img_tensor = transforms.ToTensor()(img).unsqueeze(0).to(device)

    # Enhance the image using the ESRGAN model
    with torch.no_grad():
        output_tensor = model(img_tensor)

    # Post-process the output image
    output_image = transforms.ToPILImage()(output_tensor.squeeze(0).cpu())

    # Save the enhanced image
    output_image.save(output_image_path)


if __name__ == "__main__":
    enhance_image_with_esrgan("usd_torreros_ms.jpg", "usd_torreros_ms_GAN_output.jpg")



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
