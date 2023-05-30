           
from PIL import Image
import os
from tqdm import tqdm  # python3 -m pip install tqdm

downloadsFolder = "/Users/Gdi87/Downloads/"

if __name__ == "__main__":
    image_extensions = [".jpg", ".jpeg", ".png"]
    images_to_compress = []

    #images list
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in image_extensions:
            images_to_compress.append(filename)

    # compress and progress bar
    for filename in tqdm(images_to_compress, desc="Compressing images"):
        picture = Image.open(downloadsFolder + filename)
        picture.save(downloadsFolder + "compressed_" + filename, optimize=True, quality=60)
            
