 ##old version          
##from PIL import Image
##import os
##from tqdm import tqdm  # python3 -m pip install tqdm

##downloadsFolder = "/Users/Gdi87/Downloads/"

##if __name__ == "__main__":
    ##image_extensions = [".jpg", ".jpeg", ".png"]
    ##images_to_compress = []

 ## images list
    ##for filename in os.listdir(downloadsFolder):
        ##name, extension = os.path.splitext(downloadsFolder + filename)
       ## if extension in image_extensions:
          ##  images_to_compress.append(filename)

    ## compress and progress bar
##    for filename in tqdm(images_to_compress, desc="Compressing images"):
   ##     picture = Image.open(downloadsFolder + filename)
   ##     picture.save(downloadsFolder + "compressed_" + filename, optimize=True, quality=60)
            
from PIL import Image
import os
from tqdm import tqdm

downloadsFolder = "/Users/Gdi87/Downloads/"

def get_output_directory():
    while True:
        output_dir = input("Enter the output directory path for the compressed images: ")
        if os.path.isdir(output_dir):
            return output_dir
        else:
            print("Invalid directory!")

def get_compression_quality():
    while True:
        quality = input("Enter the compression quality percentage (0-100): ")
        if quality.isdigit() and 0 <= int(quality) <= 100:
            return int(quality)
        else:
            print("Invalid input! Please enter a number between 0 and 100.")

if __name__ == "__main__":
    outputFolder = get_output_directory()
    compression_quality = get_compression_quality()

    image_extensions = [".jpg", ".jpeg", ".png"]
    images_to_compress = []

    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in image_extensions:
            images_to_compress.append(filename)

    for filename in tqdm(images_to_compress, desc="Compressing images"):
        try:
            picture = Image.open(os.path.join(downloadsFolder, filename))
            output_path = os.path.join(outputFolder, "compressed_" + filename)
            picture.save(output_path, optimize=True, quality=compression_quality)
        except Exception as e:
            print(f"Error compressing image {filename}: {str(e)}")

    print("Image compression completed.")
