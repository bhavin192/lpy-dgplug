#!/usr/bin/env python3
import requests

def validate_signature(magic_numbers):
    """Checks if the given bytes array of lenght 4 is matching with file signature of any image format
    :param magic_numbers: byte array from file (first 4 bytes)
    :returns: True if the given magic numbers are of image file"""

    #PNG -> 89 50 4E 47
    if magic_numbers == b'\x89\x50\x4E\x47':
        return True
    #JPG/JPEG -> FF D8 FF DB or FF D8 FF E0 or FF D8 FF E1
    if magic_numbers in [b'\xFF\xD8\xFF\xDB', b'\xFF\xD8\xFF\xE0', b'\xFF\xD8\xFF\xE1']:
        return True
    return False

def download_image(url):
    """Downloads the file from URL if it is a image
    :param url: string containing URL
    :returns: None"""

    if url.endswith(".jpg") or url.endswith(".png"):
        image = requests.get(url)
        if not image.ok:
            print("Unable to access the link");
            return
        #check if it is a real image
        if not validate_signature(image.content[:4]):
            print("Image is not an real image")
            return
        file_name = url.split("/")[-1]                  #last element would be file name
        with open(file_name, "wb") as image_file:
            image_file.write(image.content)
    else:
        print("The link is not an image")




if __name__ == "__main__":
    download_image("https://dgplug.org/assets/img/header.png")

