#!/usr/bin/env python3
import requests

def download_image(url):
    """Downloads the file from URL if it is a image
    :param url: string containing URL
    :returns: None"""

    if url.endswith(".jpg") or url.endswith(".png"):
        image = requests.get(url)
        if not image.ok:
            print("Unable to access the link");
            return;
        file_name = url.split("/")[-1]                  #last element would be file name
        with open(file_name, "wb") as image_file:
            image_file.write(image.content)
    else:
        print("The link is not an image")




if __name__ == "__main__":
    download_image("https://dgplug.org/assets/img/header.png")

