from time import sleep
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import sys
import shutil
import os
from os import listdir
from os.path import isfile, join
import re

### scrap.py ###
# download all images from a webpage, which name contains a given string.
# usage: py .\scrap.py URL NAME WAIT_TIME
# URL: url of the webpage
# NAME: only images containing this string will be downloaded
# WAIT_TIME: time to wait between each download (in seconds)

def scrap_images(URL) :
    print("Making the soup...")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    return soup.find_all("img")

def extract_images(URL,images,folder_name,img_number, wait_time) :
    total_images = len(images)
    scrapped_images = 0
    print(f"---Extracting {total_images} images--")
    printProgressBar(0,total_images, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(total_images) :
        url_ext = images[i].attrs['src'] 
        if folder_name.lower() in url_ext.lower() :
            scrapped_images += 1
            print(f"Image {url_ext} contains {folder_name} in its name, extracting...")
            full_url = urljoin(URL, url_ext)
            print(f"Requesting {full_url}, waiting for {wait_time} seconds")
            sleep(int(wait_time))
            r = requests.get(full_url, stream=True) 
            print(f"extracting images :{url_ext}...")
            if r.status_code == 200:
                print("status code : OK")
                with open(f"scraped/{folder_name}/{folder_name}{img_number + scrapped_images}.png", 'wb') as f: 
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    print(f"Images : {url_ext} copied in folder as image{i}.png")
                
            else :
                print(f"status error, code : {r.status_code}\n")
        else : 
            print(f"Image {url_ext} doesn't contain {folder_name} in its name, skipping...")
        printProgressBar(i + 1, len(images), prefix = 'Progress:', suffix = 'Complete', length = 50)
    print(f"-----Extraction complete, {scrapped_images}/{total_images} images extracted----")

    
def main() :
    if len(sys.argv) == 4:
        URL = sys.argv[1]
        folder_name = sys.argv[2]
        wait_time = sys.argv[3]
        print(f"Exctracting from URL : {URL}...")
        img_number = create_folder(folder_name)
        print(img_number)
        extract_images(URL,scrap_images(URL),folder_name,img_number, wait_time)
    else:
        print("### scrap.py ###")
        print("# download all images from a webpage, which name contains a given string.")
        print("# usage: py .\\scrap.py URL NAME WAIT_TIME")
        print("# URL: url of the webpage")
        print("# NAME: only images containing this string will be downloaded")
        print("# WAIT_TIME: time to wait between each download (in seconds)")
        

def create_folder(folder_name) :
    path = f"scraped/{folder_name}"
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder {folder_name} created")
        return 0
    else :
        print(f"Folder {folder_name} already exists")
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return sorted(map(lambda x: int(re.search("\\d+", x).group()), onlyfiles))[-1]

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f"\n\r{prefix} |{bar}| {percent}% {suffix}\n")
    # Print New Line on Complete
    if iteration == total: 
        print()


if __name__ == "__main__" : 
    main()
